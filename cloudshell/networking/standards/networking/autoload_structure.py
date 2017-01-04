#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict


AVAILABLE_SHELL_TYPES = ["CS_Switch",
                         "CS_Router",
                         "CS_Controller"]


__all__ = ["GenericResource", "GenericChassis",
           "GenericModule", "GenericSubModule",
           "GenericPortChannel", "GenericPowerPort", "GenericPort"]


class AbstractResource(object):
    RELATIVE_PATH_TEMPLATE = ""

    def __init__(self, shell_name, name, unique_id):
        """  """

        self._name = name
        self.shell_name = shell_name
        self._cloudshell_model_name = "{shell_name}.{shell_model_name}".format(shell_name=self.shell_name,
                                                                               shell_model_name=self.__class__.__name__)
        self.unique_id = unique_id
        self.attributes = {}
        self.resources = {}

    def add_sub_resource(self, relative_id, sub_resource):
        """ Add sub resource """

        existing_sub_resources = self.resources.get(sub_resource.RELATIVE_PATH_TEMPLATE, defaultdict(list))
        existing_sub_resources[relative_id].append(sub_resource)
        self.resources.update({sub_resource.RELATIVE_PATH_TEMPLATE: existing_sub_resources})

    @property
    def cloudshell_model_name(self):
        """ Return the name of the CloudShell model """

        return self.__class__.__name__

    @cloudshell_model_name.setter
    def cloudshell_model_name(self, model_name):
        """ Set the name of the CloudShell model """

        self.__class__.__name__ = model_name

    @property
    def name(self):
        """ Return resource name """

        return self._name

    @name.setter
    def name(self, value):
        """ Set resource name """

        self._name = value

    @property
    def unique_identifier(self):
        """ Return resource uniq identifier """

        return self.unique_id

    @unique_identifier.setter
    def unique_identifier(self, value):
        """ Set resource uniq identifier """

        self.unique_id = value


class GenericResource(AbstractResource):
    RELATIVE_PATH_TEMPLATE = ""

    def __init__(self, shell_name, name, unique_id, shell_type="CS_Switch"):
        super(GenericResource, self).__init__(shell_name, name, unique_id)
        if shell_type in AVAILABLE_SHELL_TYPES:
            self.shell_type = shell_type
        else:
            raise Exception(self.__class__.__name__, "Unavailable shell type {shell_type}."
                                                     "Shell type should be one of: {avail}"
                            .format(shell_type=shell_type, avail=", ".join(AVAILABLE_SHELL_TYPES)))

    @property
    def contact_name(self):
        """ Return the name of a contact registered in the device """

        return self.attributes["{}.Contact Name".format(self.shell_name)] if "{}.Contact Name".format(
            self.shell_name) in self.attributes else None

    @contact_name.setter
    def contact_name(self, value):
        """ Set the name of a contact registered in the device """

        self.attributes["{}.Contact Name".format(self.shell_name)] = value

    @property
    def os_version(self):
        """ Return version of the Operating System """

        return self.attributes["{}.OS Version".format(self.shell_type)] if "{}.OS Version".format(
            self.shell_type) in self.attributes else None

    @os_version.setter
    def os_version(self, value):
        """ Set version of the Operating System """

        self.attributes["{}.OS Version".format(self.shell_type)] = value

    @property
    def system_name(self):
        """ Set device system name """

        return self.attributes["{}.System Name".format(self.shell_type)] if "{}.System Name".format(
            self.shell_type) in self.attributes else None

    @system_name.setter
    def system_name(self, value):
        """ Set device system name """

        self.attributes["{}.System Name".format(self.shell_type)] = value

    @property
    def vendor(self):
        """ Return The name of the device manufacture """

        return self.attributes["{}.Vendor".format(self.shell_type)] if "{}.Vendor".format(
            self.shell_type) in self.attributes else None

    @vendor.setter
    def vendor(self, value=""):
        """ Set The name of the device manufacture """

        self.attributes["{}.Vendor".format(self.shell_type)] = value

    @property
    def location(self):
        """ The device physical location identifier. For example Lab1/Floor2/Row5/Slot4 """

        return self.attributes["{}.Location".format(self.shell_type)] if "{}.Location".format(
            self.shell_type) in self.attributes else None

    @location.setter
    def location(self, value=""):
        """ Set The device physical location identifier """

        self.attributes["{}.Location".format(self.shell_type)] = value

    @property
    def model(self):
        """ Return the device model. This information is typically used for abstract resource filtering """

        return self.attributes["{}.Model".format(self.shell_type)] if "{}.Model".format(
            self.shell_type) in self.attributes else None

    @model.setter
    def model(self, value=""):
        """ Set the device model. This information is typically used for abstract resource filtering """

        self.attributes["{}.Model".format(self.shell_type)] = value


class GenericChassis(AbstractResource):
    RELATIVE_PATH_TEMPLATE = "CH"

    @property
    def model(self):
        """ Return the chassis model """

        return self.attributes[
            "{}.GenericChassis.Model".format(self.shell_name)] if "{}.GenericChassis.Model".format(
            self.shell_name) in self.attributes else None

    @model.setter
    def model(self, value=""):
        """ Set the chassis model """

        self.attributes["{}.GenericChassis.Model".format(self.shell_name)] = value

    @property
    def serial_number(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericChassis.Serial Number".format(self.shell_name)] if "{}.GenericChassis.Serial Number".format(
            self.shell_name) in self.attributes else None

    @serial_number.setter
    def serial_number(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}.GenericChassis.Serial Number".format(self.shell_name)] = value


class GenericModule(AbstractResource):
    RELATIVE_PATH_TEMPLATE = "M"

    @property
    def model(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericModule.Model".format(self.shell_name)] if "{}.GenericModule.Model".format(
            self.shell_name) in self.attributes else None

    @model.setter
    def model(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}.GenericModule.Model".format(self.shell_name)] = value

    @property
    def version(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericModule.Version".format(self.shell_name)] if "{}.GenericModule.Version".format(
            self.shell_name) in self.attributes else None

    @version.setter
    def version(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}.GenericModule.Version".format(self.shell_name)] = value

    @property
    def serial_number(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericModule.Serial Number".format(self.shell_name)] if "{}.GenericModule.Serial Number".format(
            self.shell_name) in self.attributes else None

    @serial_number.setter
    def serial_number(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}.GenericModule.Serial Number".format(self.shell_name)] = value


class GenericSubModule(AbstractResource):
    RELATIVE_PATH_TEMPLATE = "SM"

    @property
    def model(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericSubModule.Model".format(self.shell_name)] if "{}.GenericSubModule.Model".format(
            self.shell_name) in self.attributes else None

    @model.setter
    def model(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}.GenericSubModule.Model".format(self.shell_name)] = value

    @property
    def version(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericSubModule.Version".format(self.shell_name)] if "{}.GenericSubModule.Version".format(
            self.shell_name) in self.attributes else None

    @version.setter
    def version(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}.GenericSubModule.Version".format(self.shell_name)] = value

    @property
    def serial_number(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericSubModule.Serial Number".format(self.shell_name)] if "{}.GenericSubModule.Serial Number".format(
            self.shell_name) in self.attributes else None

    @serial_number.setter
    def serial_number(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}.GenericSubModule.Serial Number".format(self.shell_name)] = value


class GenericPort(AbstractResource):
    RELATIVE_PATH_TEMPLATE = "P"

    @property
    def mac_address(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPort.MAC Address".format(self.shell_name)] if "{}.GenericPort.MAC Address".format(
            self.shell_name) in self.attributes else None

    @mac_address.setter
    def mac_address(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}.GenericPort.MAC Address".format(self.shell_name)] = value

    @property
    def l2_protocol_type(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPort.L2 Protocol Type".format(self.shell_name)] if "{}.GenericPort.L2 Protocol Type".format(
            self.shell_name) in self.attributes else None

    @l2_protocol_type.setter
    def l2_protocol_type(self, value):
        """
        Such as POS, Serial
        :type value: str
        """
        self.attributes["{}.GenericPort.L2 Protocol Type".format(self.shell_name)] = value

    @property
    def ipv4_address(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPort.IPv4 Address".format(self.shell_name)] if "{}.GenericPort.IPv4 Address".format(
            self.shell_name) in self.attributes else None

    @ipv4_address.setter
    def ipv4_address(self, value):
        """

        :type value: str
        """
        self.attributes["{}.GenericPort.IPv4 Address".format(self.shell_name)] = value

    @property
    def ipv6_address(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPort.IPv6 Address".format(self.shell_name)] if "{}.GenericPort.IPv6 Address".format(
            self.shell_name) in self.attributes else None

    @ipv6_address.setter
    def ipv6_address(self, value):
        """

        :type value: str
        """
        self.attributes["{}.GenericPort.IPv6 Address".format(self.shell_name)] = value

    @property
    def port_description(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPort.Port Description".format(self.shell_name)] if "{}.GenericPort.Port Description".format(
            self.shell_name) in self.attributes else None

    @port_description.setter
    def port_description(self, value):
        """
        The description of the port as configured in the device.
        :type value: str
        """
        self.attributes["{}.GenericPort.Port Description".format(self.shell_name)] = value

    @property
    def bandwidth(self):
        """
        :rtype: float
        """
        return self.attributes[
            "{}.GenericPort.Bandwidth".format(self.shell_name)] if "{}.GenericPort.Bandwidth".format(
            self.shell_name) in self.attributes else None

    @bandwidth.setter
    def bandwidth(self, value):
        """
        The current interface bandwidth, in MB.
        :type value: float
        """
        self.attributes["{}.GenericPort.Bandwidth".format(self.shell_name)] = value

    @property
    def mtu(self):
        """
        :rtype: float
        """
        return self.attributes[
            "{}.GenericPort.MTU".format(self.shell_name)] if "{}.GenericPort.MTU".format(
            self.shell_name) in self.attributes else None

    @mtu.setter
    def mtu(self, value):
        """
        The current MTU configured on the interface.
        :type value: float
        """
        self.attributes["{}.GenericPort.MTU".format(self.shell_name)] = value

    @property
    def duplex(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPort.Duplex".format(self.shell_name)] if "{}.GenericPort.Duplex".format(
            self.shell_name) in self.attributes else None

    @duplex.setter
    def duplex(self, value):
        """
        The current duplex configuration on the interface. Possible values are Half or Full.
        :type value: str
        """
        self.attributes["{}.GenericPort.Duplex".format(self.shell_name)] = value

    @property
    def adjacent(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPort.Adjacent".format(self.shell_name)] if "{}.GenericPort.Adjacent".format(
            self.shell_name) in self.attributes else None

    @adjacent.setter
    def adjacent(self, value):
        """
        The adjacent device (system name) and port, based on LLDP or CDP protocol.
        :type value: str
        """
        self.attributes["{}.GenericPort.Adjacent".format(self.shell_name)] = value

    @property
    def protocol_type(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPort.Protocol Type".format(self.shell_name)] if "{}.GenericPort.Protocol Type".format(
            self.shell_name) in self.attributes else None

    @protocol_type.setter
    def protocol_type(self, value="0"):
        """
        Default values is Transparent (="0")
        :type value: str
        """
        self.attributes["{}.GenericPort.Protocol Type".format(self.shell_name)] = value

    @property
    def auto_negotiation(self):
        """
        :rtype: bool
        """
        return self.attributes[
            "{}.GenericPort.Auto Negotiation".format(self.shell_name)] if "{}.GenericPort.Auto Negotiation".format(
            self.shell_name) in self.attributes else None

    @auto_negotiation.setter
    def auto_negotiation(self, value):
        """
        The current auto negotiation configuration on the interface.
        :type value: bool
        """
        self.attributes["{}.GenericPort.Auto Negotiation".format(self.shell_name)] = value


class GenericPowerPort(AbstractResource):
    RELATIVE_PATH_TEMPLATE = "PP"

    @property
    def model(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPowerPort.Model".format(self.shell_name)] if "{}.GenericPowerPort.Model".format(
            self.shell_name) in self.attributes else None

    @model.setter
    def model(self, value):
        """
        The device model. This information is typically used for abstract resource filtering.
        :type value: str
        """
        self.attributes["{}.GenericPowerPort.Model".format(self.shell_name)] = value

    @property
    def serial_number(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPowerPort.Serial Number".format(self.shell_name)] if "{}.GenericPowerPort.Serial Number".format(
            self.shell_name) in self.attributes else None

    @serial_number.setter
    def serial_number(self, value):
        """

        :type value: str
        """
        self.attributes["{}.GenericPowerPort.Serial Number".format(self.shell_name)] = value

    @property
    def version(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPowerPort.Version".format(self.shell_name)] if "{}.GenericPowerPort.Version".format(
            self.shell_name) in self.attributes else None

    @version.setter
    def version(self, value):
        """
        The firmware version of the resource.
        :type value: str
        """
        self.attributes["{}.GenericPowerPort.Version".format(self.shell_name)] = value

    @property
    def port_description(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPowerPort.Port Description".format(
                self.shell_name)] if "{}.GenericPowerPort.Port Description".format(
            self.shell_name) in self.attributes else None

    @port_description.setter
    def port_description(self, value):
        """
        The description of the port as configured in the device.
        :type value: str
        """
        self.attributes["{}.GenericPowerPort.Port Description".format(self.shell_name)] = value


class GenericPortChannel(AbstractResource):
    RELATIVE_PATH_TEMPLATE = "PC"

    @property
    def associated_ports(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPortChannel.Associated Ports".format(
                self.shell_name)] if "{}.GenericPortChannel.Associated Ports".format(
            self.shell_name) in self.attributes else None

    @associated_ports.setter
    def associated_ports(self, value):
        """ Ports associated with this port channel.
        The value is in the format ???[portResourceName],??????, for example ???GE0-0-0-1,GE0-0-0-2???
        :type value: str
        """
        self.attributes["{}.GenericPortChannel.Associated Ports".format(self.shell_name)] = value

    @property
    def ipv4_address(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPortChannel.IPv4 Address".format(
                self.shell_name)] if "{}.GenericPortChannel.IPv4 Address".format(
            self.shell_name) in self.attributes else None

    @ipv4_address.setter
    def ipv4_address(self, value):
        """

        :type value: str
        """
        self.attributes["{}.GenericPortChannel.IPv4 Address".format(self.shell_name)] = value

    @property
    def ipv6_address(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPortChannel.IPv6 Address".format(
                self.shell_name)] if "{}.GenericPortChannel.IPv6 Address".format(
            self.shell_name) in self.attributes else None

    @ipv6_address.setter
    def ipv6_address(self, value):
        """

        :type value: str
        """
        self.attributes["{}.GenericPortChannel.IPv6 Address".format(self.shell_name)] = value

    @property
    def port_description(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPortChannel.Port Description".format(
                self.shell_name)] if "{}.GenericPortChannel.Port Description".format(
            self.shell_name) in self.attributes else None

    @port_description.setter
    def port_description(self, value):
        """
        The description of the port as configured in the device.
        :type value: str
        """
        self.attributes["{}.GenericPortChannel.Port Description".format(self.shell_name)] = value

    @property
    def protocol_type(self):
        """
        :rtype: str
        """
        return self.attributes[
            "{}.GenericPortChannel.Protocol Type".format(
                self.shell_name)] if "{}.GenericPortChannel.Protocol Type".format(
            self.shell_name) in self.attributes else None

    @protocol_type.setter
    def protocol_type(self, value="0s"):
        """
        Default values is Transparent (="0")
        :type value: str
        """
        self.attributes["{}.GenericPortChannel.Protocol Type".format(self.shell_name)] = value
