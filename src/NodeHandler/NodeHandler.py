from yaml import load, dump

# In order to use LibYAML based parser and emitter -> CParser and CEmitter. For instance
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from src.Node.Node import Node

import subprocess
import logging
logger = logging.getLogger(__name__)


class NodeHandler:
    def __init__(self, node_specification_yml) -> None:
        # read and parse node_specification
        node_specification_file = open(node_specification_yml, 'r')
        node_specification = load(node_specification_file, Loader)
        node_specification_file.close()
        # Create Nodes
        self.nodes = {}
        try:
            for node in node_specification['Nodes'].values():
                new_node = Node(node['name'], node['path'],
                                node['tag'], node['args'])
                self.nodes[node['name']] = new_node
                logger.info("added Node")
                logger.debug(new_node)

        except:
            print(f"wrong YAML structure in {node_specification_yml}")
        
        logger.info("initialised")
        logger.debug(f"__init__: node_specification_yml = {node_specification_yml}")

    def getNodeActivities(self) -> dict:
        activities = {}
        for node_name in self.nodes:
            activities[self.nodes[node_name].getName()] = self.nodes[node_name].getActivity()
        logger.info("returning activities")
        logger.debug(activities)
        return activities

    #TODO: overthink wf
    def handle(self, node_name, argument_key):
        for node_name in self.nodes:
            if self.nodes[node_name].getName() == node_name:
                argument = self.nodes[node_name].getArg(argument_key)
                #TODO: maybe handle for correct arguments?
                if argument:
                    self.nodes[node_name].setProcess(subprocess.Popen(argument ))
            else:
                logger.error(f"handle: Node {node_name} does not exist")
                return
        logger.info("handled")
        logger.debug(f"handle: node_name = {node_name}, argument_key = {argument_key}")
