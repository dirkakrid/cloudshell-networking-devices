#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from abc import abstractmethod

from cloudshell.shell.core.context_utils import get_resource_name
from cloudshell.networking.devices.operations.interfaces import StateOperationsInterface


class StateOperations(StateOperationsInterface):
    def __init__(self, logger, api, context):
        self._cli_handler = None
        self._logger = logger
        self._api = api
        self._context = context
        self._resource_name = get_resource_name(context)
        self._health_check_flow = None

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
            self._health_check_flow.execute_flow(self._cli_handler, self._logger)
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

    @abstractmethod
    def shutdown(self):
        pass

    def reload(self, cli_session, sleep_timeout=500):
        pass

    def _wait_device_down(self, timeout=10):
        """ 

        :param timeout (int): during this time device should goes down
        :return: is_device_down (boolean): status is device went down
        """
        if not self._session_type:
            raise Exception(self.__class__.__name__,
                            "[wait_device_down] Device accessibility failed. Unable to get session")

        is_device_down = False
        
        try:
            with self._cli.get_session(new_sessions=self._session_type, command_mode=self._default_mode,
                                       logger=self._logger) as session:

                start_time = time.time()
                while (time.time() - start_time) < int(timeout):
                    session.send_command("")
                    time.sleep(1)
        except:
            self._logger.debug("Device successfully went down")
            is_device_down = True
        finally:
            return is_device_down

    def _wait_device_up(self, timeout=300):
        """ 

        :param timeout (int): during this time device should wake up
        :return: boolean: status is device woke up
        """

        if not self._session_type:
            raise Exception(self.__class__.__name__,
                            "[wait_device_up] Device accessibility failed. Unable to get session")

        start_time = time.time()
        while (time.time() - start_time) < int(timeout):
            try:
                with self._cli.get_session(new_sessions=self._session_type, command_mode=self._default_mode,
                                           logger=self._logger) as session:
                    session.send_command("")
                    self._logger.debug("Device successfully woke up")
                    return True
            except:
                time.sleep(5)

        return False
