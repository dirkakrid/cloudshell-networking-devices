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



class AddVlanFlow(object):
    def __init__(self, cli_handler, logger):
        self._cli_handler = cli_handler
        self._logger = logger
        self._mode = None
        self._command_actions = None

    def execute_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        self._logger.info(self.__class__.__name__, 'Add Vlan configuration started')
        with self._cli_handler.get_session(self._cli_handler.enable_mode) as session:
            self._command_actions.create_vlan(session, self._logger, vlan_range, port_mode, qnq, c_tag)
            self._command_actions.set_vlan_to_interface(session, self._logger, vlan_range, port_mode, port_name, qnq, c_tag)
            self._command_actions.verify_vlan_added(session, vlan_range, port_name)
            self._logger.info(self.__class__.__name__, 'Add Vlan configuration successfully completed')
            return 'Vlan configuration successfully completed'


class RemoveVlanFlow(object):
    def __init__(self, cli_handler, logger):
        self._cli_handler = cli_handler
        self._logger = logger
        self._mode = None
        self._command_actions = None

    def execute_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        self._logger.info(self.__class__.__name__, 'Remove Vlan configuration started')
        with self._cli_handler.get_session() as session:
            self._command_actions.remove_vlan_from_interface(session, self._logger, vlan_range, port_mode, port_name, qnq, c_tag)
            self._command_actions.verfiy(session, self._logger, vlan_range, port_name)
            self._logger.info(self.__class__.__name__, 'Remove Vlan configuration successfully completed')
            return 'Vlan configuration successfully completed'

class LoadFirmwareFlow(object):    
    def __init__(self, cli_handler, logger):
        self._cli_handler = cli_handler
        self._logger = logger
        self._mode = None
        self._command_actions = None

    def execute_flow(self, path, vrf, timeout):
        with self._cli_handler.get_session() as session:
            self._command_actions.install_firmware(session, self._logger, session, path, vrf)
            self._command_actions.reload(session, self._logger, session, timeout)
            self._command_actions.verfiy(session, self._logger, session)
            
            
class HealthCheckFlow(object):
    def __init__(self, cli_handler, logger):
        self._cli_handler = cli_handler
        self._logger = logger
        self._mode = None
        self._command_actions = None

    def execute_flow(self):
        with self._cli_handler.get_session() as session:
            self._command_actions.health_check(session)

class RunCommandFlow(object):
    def __init__(self, cli_handler, logger):
        self._cli_handler = cli_handler
        self._logger = logger
        self._mode = None
        self._command_actions = None
    
    def execute_flow(self, command):
        with self._cli_handler.get_session(self._mode) as session:
            self._command_actions.run_custom_command(session, command)
