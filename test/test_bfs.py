# write tests for bfs
import pytest
from search import graph
import os
currentdir = os.getcwd() #GitHub/project2/

@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    tiny_network = graph.Graph(os.path.join(currentdir,"data/tiny_network.adjlist"))

    all_nodes = list(tiny_network.graph.nodes) #list of every node in tiny_network.adjlist
    traversal_results = tiny_network.bfs(start =all_nodes[0],end = None ) #will return order of traversal when end = None
    assert all_nodes.sort() == traversal_results.sort() #if bfs traversed graph correctly, it should have visited every node. 
    #If that happened, then the sorted traversal_results list and sorted all_nodes list should be identical. 
    #This implicitly also tests the correct number of nodes were returned. Test that is the case


    #The test above does not check the nodes were returned in the correct order
    pass

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass
