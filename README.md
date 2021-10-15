# RosSupervisor
## Description
Created to handle multiple ROS2 Nodes. Therefore multiple Nodes can be specified in a .yml file. This project provides a NodeHandler, NodeWatcher and NodeDatamanger. Those can be used to supervise your ROS2 System.

## Requirements

## Usage

## YAML Structure
```yaml
Nodes:
    Node1:
        name: Node1
        path: test/node1
        tag: Node1
        args:
            build: cd test/node3 && colcon build
            source: source test/node1/install/setup.bash
            start: ros2 launch Node1
    Node2:
        name: Node2
        path: test/node2
        tag: Node2
        args:
            build: cd test/node3 && colcon build
            source: source test/node2/install/setup.bash
            start: ros2 launch Node2
    Node3:
        name: Node3
        path: test/node3
        tag: Node3
        args:
            build: cd test/node3 && colcon build
            source: source test/node3/install/setup.bash
            start: ros2 launch Node3
```

## Contribution

## Future updates
* Add update arguments to fetch code from git automatically (specific branch)