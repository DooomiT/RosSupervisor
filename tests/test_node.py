import pytest
from src.Node.Node import Node

node = Node("test_name", "test/path", "test-tag", {"test-arg": "foo", "test-arg2": "bar"})

def testGetArgs():
    assert node.getArgs("test-arg") == "foo"
    assert node.getArgs("foo") == None

def testGetActivity():
    assert node.getActivity() == "init"

def testGetName():
    assert node.getName() == "test_name"