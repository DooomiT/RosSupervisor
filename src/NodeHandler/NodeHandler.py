from yaml import load, dump

# In order to use LibYAML based parser and emitter -> CParser and CEmitter. For instance
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from src.Node.Node import Node

import logging
logger = logging.getLogger(__name__)


class NodeHandler:
    def __init__(self, node_specification_yml) -> None:
        # read and parse node_specification
        node_specification_file = open(node_specification_yml, 'r')
        node_specification = load(node_specification_file, Loader)
        node_specification_file.close()
        # Create Nodes
        self.nodes = []
        try:
            for node in node_specification['Nodes'].values():
                new_node = Node(node['name'], node['path'],
                                node['tag'], node['args'])
                self.nodes.append(new_node)
                logger.info("added Node")
                logger.debug(new_node)

        except:
            print(f"wrong YAML structure in {node_specification_yml}")
        
        logger.info("initialised")
        logger.debug(f"__init__: node_specification_yml = {node_specification_yml}")

    def getNodeActivities(self) -> dict:
        activities = {}
        for node in self.nodes:
            activities[node.getName()] = node.getActivity()
        logger.info("returning activities")
        logger.debug(activities)
        return activities
