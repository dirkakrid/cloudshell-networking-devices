from cloudshell.networking.devices.driver_helper import get_api, get_snmp_parameters_from_command_context
from cloudshell.shell.core.context_utils import get_resource_name, get_attribute_by_name


class AutoloadOperations(object):
    def __init__(self, cli, logger, supported_os, context):
        """
        Facilitate SNMP autoload,

        :param cli:
        :param logger:
        :param supported_os:
        :param context:
        :param Cli cli:
        :param QualiSnmp snmp_handler:
        """

        self._cli = cli
        self._logger = logger
        self._context = context
        self._autoload_flow = None
        self._enable_snmp = get_attribute_by_name(context=context, attribute_name='Enable SNMP').lower() == 'true'
        self._disable_snmp = get_attribute_by_name(context=context, attribute_name='Disable SNMP').lower() == 'true'
        self._snmp_parameters = get_snmp_parameters_from_command_context(context)
        self._resource_name = get_resource_name(context)

    def discover(self):
        """Enable and Disable SNMP communityon the device, Read it's structure and attributes: chassis, modules,
        submodules, ports, port-channels and power supplies

        :return: AutoLoadDetails object
        """

        return self._autoload_flow.execute_flow(self._enable_snmp, self._disable_snmp, self._snmp_parameters)
