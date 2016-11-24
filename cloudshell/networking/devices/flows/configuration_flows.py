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
        # with self._cli_handler.get_session() as session:
        #     self._command_actions.install_firmware(session, self._logger, session, path, vrf)
        #     self._command_actions.reload(session, self._logger, session, timeout)
        #     self._command_actions.verfiy(session, self._logger, session)


class RunCommandFlow(BaseFlow):
    def __init__(self, cli_handler, logger):
        super(RunCommandFlow, self).__init__(cli_handler, logger)

    @abstractmethod
    def execute_flow(self, command):
        pass
