from abc import ABCMeta, abstractmethod


class CliHandlerInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def cli_operations(self, command_mode_type):
        pass
