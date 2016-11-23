from abc import abstractmethod, ABCMeta


class CommandActions(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def copy(self, session, logger, path, configuration, vrf, action_map=None, error_map=None):
        pass

    @abstractmethod
    def override_startup(self, session, logger, path, vrf, action_map=None, error_map=None):
        pass

    @abstractmethod
    def override_running(self, session, path, vrf, action_map=None, error_map=None):
        pass

    @abstractmethod
    def verify_config_applied(self, session, logger, action_map=None, error_map=None):
        pass

    @abstractmethod
    def create_vlan(self, session, logger, vlan_range, port_mode, qnq, c_tag, action_map=None, error_map=None):
        pass

    @abstractmethod
    def set_vlan_to_interface(self, session, logger, vlan_range, port_mode, port_name, qnq, c_tag, action_map=None, error_map=None):
        pass

    @abstractmethod
    def verify_vlan_added(self, session, logger, action_map=None, error_map=None):
        pass

    @abstractmethod
    def remove_vlan_from_interface(self, session, logger, vlan_range, port_mode, port_name, qnq, c_tag, action_map=None, error_map=None):
        pass

    @abstractmethod
    def verify_vlan_removed(self, session, logger, vlan_range, port_name, action_map=None, error_map=None):
        pass

    @abstractmethod
    def install_firmware(self, session, logger, path, vrf, action_map=None, error_map=None):
        pass

    @abstractmethod
    def reload(self, session, logger, timeout, action_map=None, error_map=None):
        pass

    @abstractmethod
    def verify_firmware(self, session, logger, action_map=None, error_map=None):
        pass

    @abstractmethod
    def health_check(self, session, logger, action_map=None, error_map=None):
        pass

    @abstractmethod
    def run_custom_command(self, session, logger, command, action_map=None, error_map=None):
        pass
