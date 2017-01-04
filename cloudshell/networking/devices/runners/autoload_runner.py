#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractproperty, ABCMeta

# from cloudshell.shell.core.context_utils import get_resource_name


class AutoloadRunner(object):
    __metaclass__ = ABCMeta

    def __init__(self, resource_config, shell_name, supported_os):
        """
        Facilitate SNMP autoload,
        :param supported_os:
        :param context:
        :param Cli cli:
        :param QualiSnmp snmp_handler:
        """

        self.shell_name = shell_name
        self.resource_config = resource_config
        self._supported_os = supported_os
        # self._resource_name = get_resource_name(self._context)

    @abstractproperty
    def snmp_handler(self):
        """ SNMP Handler property
        :return: SNMP handler
        """

        pass

    @abstractproperty
    def autoload_flow(self):
        """ Autoload flow property
        :return: AutoloadFlow object
        """

        pass

    def discover(self):
        """Enable and Disable SNMP communityon the device, Read it's structure and attributes: chassis, modules,
        submodules, ports, port-channels and power supplies

        :return: AutoLoadDetails object
        """
        return self.autoload_flow.execute_flow(self._supported_os,
                                               self.shell_name,
                                               self.resource_config.family,
                                               self.resource_config.name)
