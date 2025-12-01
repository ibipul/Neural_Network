from gradengine.components import Node

def test_node():
    """
    Test the Node class from gradengine.components
    :return:
    """
    n = Node(5.0)
    assert n.data == 5.0
    assert n.grad == 0.0
    assert repr(n) == "Node(data=5.0)"