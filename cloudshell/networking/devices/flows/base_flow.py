

class BaseFlow(object):
    def __init__(self, cli_handler, logger):
        self._cli_handler = cli_handler
        self._logger = logger
        self._command_actions = None
