import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, name, path, tag, args) -> None:
        self.name = name
        self.path = path
        self.tag = tag
        self.args = args
        self.activity = "init"
        logger.info("initialised")
        logger.debug(f"name: {name}, path:{path}, tag:{tag}, args:{args}")

    def __str__(self):
        return(f"name: {self.name}\activity:{self.activity}\npath:{self.path}\ntag:{self.tag}\nargs:{self.args}")

    def getArgs(self, argument_key) -> str or None:
        if argument_key in self.args.keys():
            argument = self.args['argument_key_name']
            logger.info("returning argument")
            logger.debug(f"getArgs: argument = {argument}")
            return argument
        else:
            logger.error(f"argument_key {argument_key} does not exist")
            return None

    def getActivity(self):
        """getActivity function

        Returns:
            string describing the activity from the Node (init, running, stopped)
        """
        # TODO: evaluate activity from process strace -p $process_id output check
        logger.info("returning activity")
        logger.debug(f"getActivity: activity={self.activity}")
        return self.activity

    def getName(self):
        """getName function

        Returns:
            string contains the name from the Node
        """
        logger.info("returning name")
        logger.debug(f"getName: name = {self.name}")
        return self.name
