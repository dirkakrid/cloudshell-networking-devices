import os
import platform
from abc import abstractmethod
import re
from cloudshell.networking.cisco.cisco_command_modes import get_session_type
from cloudshell.networking.driver_helper import get_cli_connection_attributes
from cloudshell.shell.core.context_utils import get_resource_name
from cloudshell.networking.operations.interfaces.state_operations_interface import StateOperationsInterface


class StateOperations(StateOperationsInterface):
    def __init__(self, cli, logger, api, context):
        self._cli = cli
        self._logger = logger
        self._api = api
        self._context = context
        self._resource_name = get_resource_name(context)
        self._session_type = get_session_type(context)
        self._default_mode = None
        self._connection_attributes = get_cli_connection_attributes(api=api, context=context)

    def health_check(self):
        """Handle apply connectivity changes request json, trigger add or remove vlan methods,
        get responce from them and create json response

        :return Serialized DriverResponseRoot to json
        :rtype json
        """

        self._logger.info('Start health check on {} resource'.format(self._resource_name))
        success = False
        api_response = 'Online'
        try:
            with self._cli.get_session(session_type=self._session_type, command_mode=self._default_mode,
                                       connection_attrs=self._connection_attributes, logger=self._logger) as session:
                session.send_command('')
                success = True
        except Exception:
            pass

        result = 'Health check on resource {}'.format(self._resource_name)
        if success:
            result += ' passed.'
        else:
            api_response = 'Error'
            result += ' failed.'

        try:
            self._api.SetResourceLiveStatus(self._resource_name, api_response, result)
        except Exception as e:
            self._logger.error('Cannot update {} resource status on portal'.format(self._resource_name))

        self._logger.info('Health check on {} resource completed'.format(self._resource_name))
        return result

    @abstractmethod
    def shutdown(self):
        pass

    def reload(self, session, logger):
        pass
