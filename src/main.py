from os import getcwd, path

from yaml.nodes import Node
from src.NodeHandler.NodeHandler import NodeHandler

import logging
logger = logging.getLogger(__name__)


def setup() -> None:
    node_specification_path = path.join(getcwd(), "node-specification.yml")
    node_handler = NodeHandler(node_specification_path)


if __name__ == "__main__":
    import logging.config
    logger_config = path.join(getcwd(), 'logger.conf')
    logging.config.fileConfig(logger_config, disable_existing_loggers=False)
    setup()
