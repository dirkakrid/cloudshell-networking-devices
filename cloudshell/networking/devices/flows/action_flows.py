#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod


class BaseFlow(object):
    def __init__(self, cli_handler, logger):
        self._cli_handler = cli_handler
        self._logger = logger
        self._command_actions = None


class SaveConfigurationFlow(BaseFlow):
    def __init__(self, cli_handler, logger):
        super(SaveConfigurationFlow, self).__init__(cli_handler, logger)

    @abstractmethod
    def execute_flow(self, folder_path, configuration_type, vrf_management_name=None):
        pass


class RestoreConfigurationFlow(BaseFlow):
    def __init__(self, cli_handler, logger):
        super(RestoreConfigurationFlow, self).__init__(cli_handler, logger)

    @abstractmethod
    def execute_flow(self, path, restore_method, configuration, vrf):
        pass


class AddVlanFlow(BaseFlow):
    def __init__(self, cli_handler, logger):
        super(AddVlanFlow, self).__init__(cli_handler, logger)

    @abstractmethod
    def execute_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        pass


class RemoveVlanFlow(BaseFlow):
    def __init__(self, cli_handler, logger):
        super(RemoveVlanFlow, self).__init__(cli_handler, logger)

    @abstractmethod
    def execute_flow(self, vlan_range, port_name, port_mode, action_map=None, error_map=None):
        pass


class LoadFirmwareFlow(BaseFlow):
    def __init__(self, cli_handler, logger):
        super(LoadFirmwareFlow, self).__init__(cli_handler, logger)

    @abstractmethod
    def execute_flow(self, path, vrf, timeout):
        pass


class RunCommandFlow(BaseFlow):
    def __init__(self, cli_handler, logger):
        super(RunCommandFlow, self).__init__(cli_handler, logger)

    def execute_flow(self, custom_command="", is_config=False):
        """ Run custom command

        :param custom_command: command for execution on device
        :param is_config: if True then run command in configuration mode
        :return: command execution output
        """

        responses = []
        if isinstance(custom_command, str):
            commands = [custom_command]
        elif isinstance(custom_command, tuple):
            commands = list(custom_command)
        else:
            commands = custom_command

        if is_config:
            mode = self._cli_handler.config_mode
            if not mode:
                raise Exception(self.__class__.__name__,
                                "CliHandler configuration is missing. Config Mode has to be defined")
        else:
            mode = self._cli_handler.enable_mode
            if not mode:
                raise Exception(self.__class__.__name__,
                                "CliHandler configuration is missing. Enable Mode has to be defined")

        with self._cli_handler.get_cli_service(mode) as session:
            for cmd in commands:
                responses.append(session.send_command(command=cmd))
        return '\n'.join(responses)
