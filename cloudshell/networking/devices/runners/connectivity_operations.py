from threading import Thread
import jsonpickle
from cloudshell.core.driver_response import DriverResponse
from cloudshell.core.driver_response_root import DriverResponseRoot
from cloudshell.networking.apply_connectivity.models.connectivity_result import ConnectivityErrorResponse, \
    ConnectivitySuccessResponse
from cloudshell.networking.devices.json_request_helper import JsonRequestDeserializer
from cloudshell.networking.devices.networking_utils import serialize_to_json
from cloudshell.networking.devices.runners.interfaces.connectivity_operations_interface import \
    ConnectivityOperationsInterface


class ConnectivityOperations(ConnectivityOperationsInterface):
    APPLY_CONNECTIVITY_CHANGES_ACTION_REQUIRED_ATTRIBUTE_LIST = ['type', 'actionId',
                                                                 ('connectionParams', 'mode'),
                                                                 ('actionTarget', 'fullAddress')]

    def __init__(self, logger):
        self._logger = logger
        self.add_vlan_flow = None
        self.remove_vlan_flow = None

    def apply_connectivity_changes(self, request):
        """Handle apply connectivity changes request json, trigger add or remove vlan methods,
        get responce from them and create json response
        :param request: json with all required action to configure or remove vlans from certain port
        :return Serialized DriverResponseRoot to json
        :rtype json
        """

        if request is None or request == '':
            raise Exception('ConnectivityOperations', 'request is None or empty')

        holder = JsonRequestDeserializer(jsonpickle.decode(request))

        if not holder or not hasattr(holder, 'driverRequest'):
            raise Exception('ConnectivityOperations', 'Deserialized request is None or empty')

        driver_response = DriverResponse()
        add_vlan_thread_list = []
        remove_vlan_thread_list = []
        driver_response_root = DriverResponseRoot()

        for action in holder.driverRequest.actions:
            self._logger.info('Action: ', action.__dict__)
            self._validate_request_action(action)
            if action.type == 'removeVlan':
                remove_vlan_thread = Thread(target=self.remove_vlan, args=(action,))
                remove_vlan_thread_list.append(remove_vlan_thread)
                remove_vlan_thread.start()
            elif action.type == 'setVlan':
                add_vlan_thread = Thread(target=self.add_vlan, args=(action,))
                add_vlan_thread_list.append(add_vlan_thread)
                add_vlan_thread.start()
            else:
                continue
        results = [r.join() for r in remove_vlan_thread_list]
        results.extend([r.join() for r in add_vlan_thread_list])
        driver_response.actionResults = results
        driver_response_root.driverResponse = driver_response
        return serialize_to_json(driver_response_root).replace('[true]', 'true')

    def _validate_request_action(self, action):
        """Validate action from the request json, according to APPLY_CONNECTIVITY_CHANGES_ACTION_REQUIRED_ATTRIBUTE_LIST
        """
        is_fail = False
        fail_attribute = ''
        for class_attribute in self.APPLY_CONNECTIVITY_CHANGES_ACTION_REQUIRED_ATTRIBUTE_LIST:
            if type(class_attribute) is tuple:
                if not hasattr(action, class_attribute[0]):
                    is_fail = True
                    fail_attribute = class_attribute[0]
                if not hasattr(getattr(action, class_attribute[0]), class_attribute[1]):
                    is_fail = True
                    fail_attribute = class_attribute[1]
            else:
                if not hasattr(action, class_attribute):
                    is_fail = True
                    fail_attribute = class_attribute

        if is_fail:
            raise Exception('ConnectivityOperations',
                            'Mandatory field {0} is missing in ApplyConnectivityChanges request json'.format(
                                fail_attribute))

    def _get_port_name(self, action):
        return action.actionTarget.fullName

    def add_vlan(self, action):
        qnq = False
        ctag = ''
        for attribute in action.connectionParams.vlanServiceAttributes:
            if attribute.attributeName.lower() == 'qnq':
                request_qnq = attribute.attributeValue
                if request_qnq.lower() == 'true':
                    qnq = True
            elif attribute.attributeName.lower() == 'ctag':
                ctag = attribute.attributeValue
        try:
            action_result = self.add_vlan_flow(self._cli_handler, self._logger)(action.connectionParams.vlanId,
                                               action.actionTarget.fullName,
                                               action.connectionParams.mode.lower(),
                                               qnq,
                                               ctag)
            return ConnectivitySuccessResponse(action, action_result)
        except Exception as e:
            return ConnectivityErrorResponse(action, e.message)

    def remove_vlan(self, action):
        try:

            result = self.remove_vlan_flow(action.connectionParams.vlanId,
                                           action.actionTarget.fullName,
                                           action.connectionParams.mode.lower())
            ConnectivitySuccessResponse(action, result)
        except Exception as e:
            ConnectivityErrorResponse(action, e.message)
