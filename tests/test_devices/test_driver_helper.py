# import unittest
#
# from mock import Mock
#
# from cloudshell.devices.driver_helper import get_snmp_parameters_from_command_context
# from cloudshell.snmp.snmp_parameters import SNMPV2Parameters, SNMPV3Parameters
#
#
# class MyTestCase(unittest.TestCase):
#     def test_it_creates_SNMPV3_instance_if_snmp_version_attribute_is_V3(self):
#         # Arrange
#         context = Mock()
#         context.resource = Mock()
#         context.resource.attributes = {'SNMP Version': '3', 'SNMP User': 'something',
#                                        'SNMP Password': 'secret', 'SNMP Private Key': 'key'}
#
#         # Act
#         result = get_snmp_parameters_from_command_context(context)
#
#         # Assert
#         self.assertIsInstance(result, SNMPV3Parameters)
#
#     def test_it_creates_SNMPV2_instance_if_snmp_version_attribute_is_V2(self):
#         # Arrange
#         context = Mock()
#         context.resource = Mock()
#         context.resource.attributes = {'SNMP Version': '2', 'SNMP Read Community': 'something'}
#
#         # Act
#         result = get_snmp_parameters_from_command_context(context)
#
#         # Assert
#         self.assertIsInstance(result, SNMPV2Parameters)
