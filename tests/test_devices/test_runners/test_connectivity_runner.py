# from unittest import TestCase
#
# from cloudshell.networking.devices.runners.connectivity_runner import ConnectivityRunner
# from mock import MagicMock
#
# from tests.operations import TEST_REQUEST
#
#
# class TestConnectivityOperations(TestCase):
#     def setUp(self):
#         logger = MagicMock()
#         self.handler = ConnectivityRunner(logger)
#         self.handler.add_vlan_flow = MagicMock()
#         self.handler.add_vlan_flow.execute_flow.return_value = 'vlan added'
#         self.handler.remove_vlan_flow = MagicMock()
#         self.handler.remove_vlan_flow.execute_flow.return_value = 'vlan removed'
#
#     def get_request(self):
#         return TEST_REQUEST
#
#     def test_can_handle_request_with_multiple_actions(self):
#         response = self.handler.apply_connectivity_changes(self.get_request())
#         self.assertIsNotNone(response)
#
#
#
