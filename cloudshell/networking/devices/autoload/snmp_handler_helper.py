from abc import abstractmethod, ABCMeta
from threading import Lock

from cloudshell.networking.devices.driver_helper import get_snmp_parameters_from_command_context
from cloudshell.snmp.quali_snmp import QualiSnmp


class SNMPHandlerCreator(object):
    __metaclass__ = ABCMeta
    __LOCK = Lock()

    def __init__(self, logger, context):
        self._logger = logger
        self._context = context
        self._snmp_parameters = get_snmp_parameters_from_command_context(context)

    def __enter__(self):
        self.__LOCK.acquire()
        self.enable_snmp()
        return self.create_snmp_handler()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disable_snmp()
        self.__LOCK.release()

    def create_snmp_handler(self):
        snmp = QualiSnmp(logger=self._logger, snmp_parameters=self._snmp_parameters)
        return snmp

    @abstractmethod
    def enable_snmp(self):
        pass

    @abstractmethod
    def disable_snmp(self):
        pass
