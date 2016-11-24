#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.networking.devices.flows.action_flows import RunCommandFlow
from cloudshell.networking.devices.runners.interfaces.state_operations_interface import StateOperationsInterface
from cloudshell.shell.core.context_utils import get_resource_name


class StateOperations(StateOperationsInterface):
    def __init__(self, logger, api, context):
        self._logger = logger
        self._api = api
        self._context = context
        self._resource_name = get_resource_name(context)
        self.cli_handler = None
        self._health_check_flow = RunCommandFlow(self.cli_handler, logger)

    def health_check(self):
        """Handle apply connectivity changes request json, trigger add or remove vlan methods,
        get response from them and create json response

        :return Serialized DriverResponseRoot to json
        :rtype json
        """

        self._logger.info('Start health check on {} resource'.format(self._resource_name))
        api_response = 'Online'

        result = 'Health check on resource {}'.format(self._resource_name)
        try:
            self._health_check_flow.execute_flow()
            result += ' passed.'
        except Exception:
            api_response = 'Error'
            result += ' failed.'

        try:
            self._api.SetResourceLiveStatus(self._resource_name, api_response, result)
        except Exception:
            self._logger.error('Cannot update {} resource status on portal'.format(self._resource_name))

        self._logger.info('Health check on {} resource completed'.format(self._resource_name))
        return result

    def shutdown(self):
        pass
