# write tests for bfs
import pytest
from search import Graph 
import os
import random
currentdir = os.getcwd() #GitHub/project2/

# @pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    tiny_network = Graph(os.path.join(currentdir,"data/tiny_network.adjlist"))

    all_nodes = list(tiny_network.graph.nodes) #list of every node in tiny_network.adjlist
    traversal_results = tiny_network.bfs(start =all_nodes[0],end = None ) #will return order of traversal when end = None
    assert all_nodes.sort() == traversal_results.sort() #if bfs traversed graph correctly, it should have visited every node. 
    #If that happened, then the sorted traversal_results list and sorted all_nodes list should be identical. 
    #This implicitly also tests the correct number of nodes were returned. Test that is the case


    #The test above does not check the nodes were returned in the correct order
    

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
    tiny_network = Graph(os.path.join(currentdir,"data/tiny_network.adjlist"))
    length_3_paths = [] #this will contain length 3 paths that are the only possible length 3 paths between the starting node and end node. Therefore they are also the shortest paths. I will test that BFS can find this path
    max_tests = 100
    test_num = 0
    for starting_node in list(tiny_network.graph.nodes): #iterate through every node in the network or until max_tests condition is reached, whichever comes first
        if len(list(tiny_network.graph[starting_node])) == 1: #Go on to look for neighbors of starting nodes that only have one neighbor
            next_node = list(tiny_network.graph[starting_node])[0] #Grab the single neighbor of the starting node
            for third_node in list(tiny_network.graph[next_node]): #Because the starting node only had one outgoing neighbor, all outgoing neighbors of the next node (except for the starting node) will create a unique shortest path; the only possible path is the shortest (length 3) path. If BFS worked, it should find it
                if third_node != starting_node: #If third node happens to be the starting node, BFS would find a length 1 path from starting node -> starting node. Ignore these because that is too easy of a test
                    length_3_paths.append([starting_node,next_node,third_node]) #add the unique shortest path to the list
                    test_num += 1
            if test_num >= max_tests: #break so the tests don't take too long
                break

    for length_3_path in length_3_paths:
        starting_node = length_3_path[0]
        third_node = length_3_path[-1]
        assert tiny_network.bfs(starting_node,third_node) == length_3_path
    pass
