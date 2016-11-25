from cloudshell.networking.devices.flows.action_flows import RunCommandFlow
from cloudshell.networking.devices.runners.interfaces.run_command_runner_interface import RunCommandInterface


class RunCommandRunner(RunCommandInterface):
    def __init__(self, logger):
        """Create RunCommandOperations

        :param logger: QsLogger object
        :return:
        """

        self._cli_handler = None
        self._logger = logger
        self._run_command_flow = RunCommandFlow(self._cli_handler, self._logger)

    def run_custom_command(self, custom_command):
        return self._run_command_flow.execute_flow(custom_command=custom_command)

    def run_custom_config_command(self, custom_command):
        return self._run_command_flow.execute_flow(custom_command=custom_command, is_config=True)
