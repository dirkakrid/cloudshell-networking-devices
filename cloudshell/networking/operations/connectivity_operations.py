import traceback
from abc import abstractmethod

import jsonpickle

from cloudshell.networking.apply_connectivity.models.connectivity_request import ConnectivityActionRequest
from cloudshell.networking.apply_connectivity.models.connectivity_result import ConnectivitySuccessResponse, \
    ConnectivityErrorResponse


def serialize_connectivity_result(result, unpicklable=False):
    """Serializes output as JSON and writes it to console output wrapped with special prefix and suffix

    :param result: Result to return
    :param unpicklable: If True adds JSON can be deserialized as real object.
                        When False will be deserialized as dictionary
    """

    json = jsonpickle.encode(result, unpicklable=unpicklable)
    result_for_output = str(json)
    return result_for_output


class ConnectivityOperations(object):
    APPLY_CONNECTIVITY_CHANGES_ACTION_REQUIRED_ATTRIBUTE_LIST = ['type', 'actionId',
                                                                 ('connectionParams', 'mode'),
                                                                 ('actionTarget', 'fullAddress')]

    def __init__(self):
        pass

    @property
    @abstractmethod
    def logger(self):
        pass

    def add_vlan_action(self, action):
        """Handle apply connectivity changes request json, trigger add or remove vlan methods,
        get responce from them and create json response

        :param ConnectivityActionRequest action: ConnectivityActionRequest
        :return: Success or Error result
        :rtype: ConnectivityActionResult
        """

        self.logger.info('Action: ', action.__dict__)
        self._validate_request_action(action)
        try:
            qnq = False
            ctag = ''
            for attribute in action.connectionParams.vlanServiceAttributes:
                if attribute.attributeName.lower() == 'qnq':
                    request_qnq = attribute.attributeValue
                    if request_qnq.lower() == 'true':
                        qnq = True
                elif attribute.attributeName.lower() == 'ctag':
                    ctag = attribute.attributeValue
            result = self.add_vlan(action.connectionParams.vlanId,
                                   action.actionTarget.fullName,
                                   action.connectionParams.mode.lower(),
                                   qnq,
                                   ctag)
            action_result = ConnectivitySuccessResponse(action, result)
        except Exception as e:
            self.logger.error('Add vlan failed: {0}'.format(traceback.format_exc()))
            action_result = ConnectivityErrorResponse(action, ', '.join(map(str, e.args)))

        return action_result

    def remove_vlan_action(self, action):
        """Handle apply connectivity changes request json, trigger add or remove vlan methods,
        get responce from them and create json response

        :param ConnectivityActionRequest action: ConnectivityActionRequest
        :return: Success or Error result
        :rtype: ConnectivityActionResult
        """

        self.logger.info('Action: ', action.__dict__)
        self._validate_request_action(action)
        try:
            result = self.remove_vlan(action.connectionParams['vlanId'],
                                      action.actionTarget.fullName,
                                      action.connectionParams.mode.lower())
            action_result = ConnectivitySuccessResponse(action, result)
        except Exception as e:
            self.logger.error('Remove vlan failed: {0}'.format(traceback.format_exc()))
            action_result = ConnectivityErrorResponse(action, ', '.join(map(str, e.args)))

        return action_result

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

    @abstractmethod
    def add_vlan(self, vlan_range, port_list, port_mode, qnq, ctag):
        pass

    @abstractmethod
    def remove_vlan(self, vlan_range, port_list, port_mode):
        pass
