from abc import abstractmethod, ABCMeta


class CommandActions(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def copy(self, session, logger, path, configuration, vrf):
        pass

    @abstractmethod
    def override_startup(self, session, path, restore_method, configuration, vrf):
        pass

    @abstractmethod
    def override_running(self, session, path, restore_method, configuration, vrf):
        pass

    @abstractmethod
    def verify_config_applied(self, session, logger):
        pass

    @abstractmethod
    def create_vlan(self, session, logger, vlan_range, port_mode, qnq, c_tag):
        pass

    @abstractmethod
    def set_vlan_to_interface(self, session, logger, vlan_range, port_mode, port_name, qnq, c_tag):
        pass

    @abstractmethod
    def verify_vlan_added(self, session, logger):
        pass

    @abstractmethod
    def remove_vlan_from_interface(self, session, logger, vlan_range, port_mode, port_name, qnq, c_tag):
        pass

    @abstractmethod
    def verify_vlan_removed(self, session, logger, vlan_range, port_name):
        pass

    @abstractmethod
    def install_firmware(self, session, logger, path, vrf):
        pass

    @abstractmethod
    def reload(self, session, logger, timeout):
        pass

    @abstractmethod
    def verify_firmware(self, session, logger):
        pass

    @abstractmethod
    def health_check(self, session, logger):
        pass

    @abstractmethod
    def run_custom_command(self, session, logger, command):
        pass
