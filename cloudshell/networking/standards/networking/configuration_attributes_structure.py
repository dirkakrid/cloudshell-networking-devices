#!/usr/bin/python
# -*- coding: utf-8 -*-


class GenericNetworkingResource(object):
    def __init__(self, shell_name=None, name=None, supported_os=None, namespace=True):
        """ Init method

        :param shell_name: Shell Name
        :type shell_name: str
        :param name: Resource Name
        :type name: str
        :param supported_os: list of supported OS
        :type supported_os: list
        :param namespace: determine is namespace for attributes should be use(True - with namespace, False - without)
        :type namespace: bool
        """

        self.attributes = {}
        self.shell_name = shell_name
        self.name = name
        self.supported_os = supported_os
        self.fullname = None
        self.address = None  # The IP address of the resource
        self.family = None  # The resource family
        self.namespace = namespace

        if namespace:
            self.namespace_prefix = "{}".format(self.shell_name)
        else:
            self.namespace_prefix = ""

    def create_from_context(self, context):
        """
        Creates an instance of Networking Resource by given context
        :param context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :return:
        :rtype GenericNetworkingResource
        """
        result = GenericNetworkingResource(shell_name=self.shell_name,
                                           name=context.resource.name,
                                           supported_os=self.supported_os,
                                           namespace=self.namespace)
        result.address = context.resource.address
        result.family = context.resource.family
        result.fullname = context.resource.fullname

        for attr_name, attr_value in context.resource.attributes.iteritems():
            result.attributes[attr_name] = attr_value
        return result

    @property
    def backup_location(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Backup Location".format(self.namespace_prefix), None)

    @property
    def backup_type(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Backup Type".format(self.namespace_prefix), None)

    @property
    def backup_user(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Backup User".format(self.namespace_prefix), None)

    @property
    def backup_password(self):
        """
        :rtype: string
        """
        return self.attributes.get("{}Backup Password".format(self.namespace_prefix), None)

    @property
    def vrf_management_name(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}VRF Management Name".format(self.namespace_prefix), None)

    @property
    def user(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}User".format(self.namespace_prefix), None)

    @property
    def password(self):
        """
        :rtype: string
        """
        return self.attributes.get("{}Password".format(self.namespace_prefix), None)

    @property
    def enable_password(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Enable Password".format(self.namespace_prefix), None)

    @property
    def power_management(self):
        """
        :rtype: bool
        """
        return self.attributes.get("{}Power Management".format(self.namespace_prefix), None)

    @property
    def sessions_concurrency_limit(self):
        """
        :rtype: float
        """
        return self.attributes.get("{}Sessions Concurrency Limit".format(self.namespace_prefix), None)

    @property
    def snmp_read_community(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}SNMP Read Community".format(self.namespace_prefix), None)

    @property
    def snmp_write_community(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}SNMP Write Community".format(self.namespace_prefix), None)

    @property
    def snmp_v3_user(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}SNMP V3 User".format(self.namespace_prefix), None)

    @property
    def snmp_v3_password(self):
        """
        :rtype: string
        """
        return self.attributes.get("{}SNMP V3 Password".format(self.namespace_prefix), None)

    @property
    def snmp_v3_private_key(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}SNMP V3 Private Key".format(self.namespace_prefix), None)

    @property
    def snmp_version(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}SNMP Version".format(self.namespace_prefix), None)

    @property
    def enable_snmp(self):
        """
        :rtype: bool
        """
        return self.attributes.get("{}Enable SNMP".format(self.namespace_prefix), None)

    @property
    def disable_snmp(self):
        """
        :rtype: bool
        """
        return self.attributes.get("{}Disable SNMP".format(self.namespace_prefix), None)

    @property
    def console_server_ip_address(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Console Server IP Address".format(self.namespace_prefix), None)

    @property
    def console_user(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Console User".format(self.namespace_prefix), None)

    @property
    def console_port(self):
        """
        :rtype: float
        """
        return self.attributes.get("{}Console Port".format(self.namespace_prefix), None)

    @property
    def console_password(self):
        """
        :rtype: string
        """
        return self.attributes.get("{}Console Password".format(self.namespace_prefix), None)

    @property
    def cli_connection_type(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}CLI Connection Type".format(self.namespace_prefix), None)

    @property
    def cli_tcp_port(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}CLI TCP Port".format(self.namespace_prefix), None)
