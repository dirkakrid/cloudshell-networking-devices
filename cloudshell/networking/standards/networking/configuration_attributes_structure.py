#!/usr/bin/python
# -*- coding: utf-8 -*-


class GenericNetworkingResource(object):
    def __init__(self, shell_name, name=None):
        """   """

        self.attributes = {}
        self.shell_name = shell_name
        self.name = name
        self.fullname = None
        self.address = None  # The IP address of the resource
        self.family = None  # The resource family

    def create_from_context(self, context):
        """
        Creates an instance of Networking Resource by given context
        :param context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :return:
        :rtype BaseEntity
        """
        result = GenericNetworkingResource(shell_name=self.shell_name, name=context.resource.name)
        result.address = context.resource.address
        result.family = context.resource.family
        result.fullname = context.resource.fullname

        for attr_name, attr_value in context.resource.attributes.iteritems():
            result.attributes["{0}.{1}".format(self.shell_name, attr_name)] = attr_value
        return result

    @property
    def backup_location(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.Backup Location".format(self.shell_name)] if "{}.Backup Location".format(
            self.shell_name) in self.attributes else None

    @property
    def backup_type(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.Backup Type".format(self.shell_name)] if "{}.Backup Type".format(
            self.shell_name) in self.attributes else None

    @property
    def backup_user(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.Backup User".format(self.shell_name)] if "{}.Backup User".format(
            self.shell_name) in self.attributes else None

    @property
    def backup_password(self):
        """
        :rtype: string
        """
        return self.attributes[
            "{}.Backup Password".format(self.shell_name)] if "{}.Backup Password".format(
            self.shell_name) in self.attributes else None

    @property
    def vrf_management_name(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.VRF Management Name".format(self.shell_name)] if "{}.VRF Management Name".format(
            self.shell_name) in self.attributes else None

    @property
    def user(self):
        """
        :rtype: str
        """
        return self.attributes["{}.User".format(self.shell_name)] if "{}.User".format(
            self.shell_name) in self.attributes else None

    @property
    def password(self):
        """
        :rtype: string
        """
        return self.attributes["{}.Password".format(self.shell_name)] if "{}.Password".format(
            self.shell_name) in self.attributes else None

    @property
    def enable_password(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.Enable Password".format(self.shell_name)] if "{}.Enable Password".format(
            self.shell_name) in self.attributes else None

    @property
    def power_management(self):
        """
        :rtype: bool
        """
        return self.attributes[
            "{}.Power Management".format(self.shell_name)] if "{}.Power Management".format(
            self.shell_name) in self.attributes else None

    @property
    def sessions_concurrency_limit(self):
        """
        :rtype: float
        """
        return self.attributes[
            "{}.Sessions Concurrency Limit".format(self.shell_name)] if "{}.Sessions Concurrency Limit".format(
            self.shell_name) in self.attributes else None

    @property
    def snmp_read_community(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.SNMP Read Community".format(self.shell_name)] if "{}.SNMP Read Community".format(
            self.shell_name) in self.attributes else None

    @property
    def snmp_write_community(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.SNMP Write Community".format(self.shell_name)] if "{}.SNMP Write Community".format(
            self.shell_name) in self.attributes else None

    @property
    def snmp_v3_user(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.SNMP V3 User".format(self.shell_name)] if "{}.SNMP V3 User".format(
            self.shell_name) in self.attributes else None

    @property
    def snmp_v3_password(self):
        """
        :rtype: string
        """
        return self.attributes[
            "{}.SNMP V3 Password".format(self.shell_name)] if "{}.SNMP V3 Password".format(
            self.shell_name) in self.attributes else None

    @property
    def snmp_v3_private_key(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.SNMP V3 Private Key".format(self.shell_name)] if "{}.SNMP V3 Private Key".format(
            self.shell_name) in self.attributes else None

    @property
    def snmp_version(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.SNMP Version".format(self.shell_name)] if "{}.SNMP Version".format(
            self.shell_name) in self.attributes else None

    @property
    def enable_snmp(self):
        """
        :rtype: bool
        """
        return self.attributes[
            "{}.Enable SNMP".format(self.shell_name)] if "{}.Enable SNMP".format(
            self.shell_name) in self.attributes else None

    @property
    def disable_snmp(self):
        """
        :rtype: bool
        """
        return self.attributes[
            "{}.Disable SNMP".format(self.shell_name)] if "{}.Disable SNMP".format(
            self.shell_name) in self.attributes else None

    @property
    def console_server_ip_address(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.Console Server IP Address".format(self.shell_name)] if "{}.Console Server IP Address".format(
            self.shell_name) in self.attributes else None

    @property
    def console_user(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.Console User".format(self.shell_name)] if "{}.Console User".format(
            self.shell_name) in self.attributes else None

    @property
    def console_port(self):
        """
        :rtype: float
        """
        return self.attributes[
            "{}.Console Port".format(self.shell_name)] if "{}.Console Port".format(
            self.shell_name) in self.attributes else None

    @property
    def console_password(self):
        """
        :rtype: string
        """
        return self.attributes[
            "{}.Console Password".format(self.shell_name)] if "{}.Console Password".format(
            self.shell_name) in self.attributes else None

    @property
    def cli_connection_type(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.CLI Connection Type".format(self.shell_name)] if "{}.CLI Connection Type".format(
            self.shell_name) in self.attributes else None

    @property
    def cli_tcp_port(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.CLI TCP Port".format(self.shell_name)] if "{}.CLI TCP Port".format(
            self.shell_name) in self.attributes else None
