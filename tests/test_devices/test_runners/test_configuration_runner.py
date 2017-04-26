import unittest

import mock

from cloudshell.devices.runners.configuration_runner import ConfigurationRunner


class TestConfigurationRunner(unittest.TestCase):
    def setUp(self):
        self.logger = mock.MagicMock()
        self.resource_config = mock.MagicMock()
        self.api = mock.MagicMock()

        class TestedConfigurationRunner(ConfigurationRunner):
            def cli_handler(self):
                pass

            def file_system(self):
                pass

            def restore_flow(self):
                pass

            def save_flow(self):
                pass

        self.connectivity_runner = TestedConfigurationRunner(logger=self.logger,
                                                            resource_config=self.resource_config,
                                                            api=self.api)

    def test_abstract_methods(self):
        """Check that instance can't be instantiated without implementation of the all abstract methods"""
        class TestedClass(ConfigurationRunner):
            pass

        with self.assertRaisesRegexp(TypeError, "Can't instantiate abstract class TestedClass with abstract methods "
                                                "cli_handler, file_system, restore_flow, save_flow"):
            TestedClass(logger=self.logger,
                        resource_config=self.resource_config,
                        api=self.api)
