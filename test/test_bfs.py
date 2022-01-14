# write tests for bfs
import pytest
from search import Graph 
import os
import random
currentdir = os.getcwd() #GitHub/project2/
print('hello')
print(currentdir)

# @pytest.fixture
def test_bfs_traversal():
    """
    Test 1: 
    Instantiate a simple graph where the order of traversal is clear. Then have the bfs algorithm traverse it starting with 
    a few different start nodes and assert the expected outcome.

    Test 2:
    Same as test 1, except the graph here contains a few cyclical connections. Test that the bfs algorithm handles this properly and does not get tied up in an endless cycle
    Again, I assert the order of traversal is what is expected from a breadth-first search starting with two different starting nodes.


    Test 3:
    tiny_network.adjlist is a connected graph. Therefore, traversing it should return every node. Test that the bfs algorithm returns every node in the network by checking
    the sorted list of traversed nodes is the same as the sorted list of all nodes.
    """


    ############# Test 1 #############
    # Here I test that bfs traverses a graph in the expected breadth-first manner and returns the expected nodes in the correct order

    test_dict = {
    "A":["B","C","H"],
    "B":["E","D"],
    "C":["F","G"]
    }

    test_graph = Graph(input_dict = test_dict) #Instantiate Graph using dictionary I created. This graph is simpler than tiny_network so it is easy to assert the order of traversal a priori
    assert test_graph.bfs(start = "A", end = None) == ["A","B","C","H","E","D","F","G"]
    assert test_graph.bfs(start = "B", end = None) == ["B","E","D"]
    assert test_graph.bfs(start = "C", end = None) == ["C","F","G"]
    assert test_graph.bfs(start = "H", end = None) == ["H"]



    ############# Test 2 #############
    #Similar to test 1, except here I test the bfs algoritm outputs correct order of traversal for a graph with cyclical connections
    #The traversal output should not cycle endlessly because nodes are not re-added to the queue after being visited
    test_dict2 = {
    "B":["E","D"],
    "C":["F","G"],
    "D":["H"],
    "G":["K"],
    "H":["B"],
    "K":["C"]
    }
    #cyclical connection between B->D->H->B
    #cyclical connection between C->G->K->C
    

    test_graph = Graph(input_dict = test_dict2)
    assert test_graph.bfs(start = "C", end = None) == ["C","F","G","K"]
    assert test_graph.bfs(start = "B", end = None) == ["B","E","D","H"]

    print(currentdir == 'here')

    ############# Test 2 #############
    tiny_network = Graph(filename = "./data/tiny_network.adjlist")
    all_nodes = list(tiny_network.graph.nodes)
    all_nodes.sort() #sort the nodes in place
    traversal_results = tiny_network.bfs(start = all_nodes[0], end = None) #Get order of traversal starting with an arbitrary node
    traversal_results.sort() #sort traversed nodes in place
    assert all_nodes == traversal_results #the sorted list of all nodes in the network should be identical to the sorted list of traversed nodes, because the graph is connected

def test_bfs():
    """
    Test 1:
    0) This test uses tiny_network.adjlist
    1) Begin iterating through every node in the graph. Select nodes that only have one outgoing neighbor
    2) Save the starting node, its only neighbor, and one of the second node's neighbors (as long as it is not the starting node) in a list.
        2a) The path between these three nodes must be the shortest path between the start and third node because the start node only had one neighbor. 
        2b) Therefore, there is only one path between the first and second node. Therefore, the only alternate paths between the second and third node besides the direct one must be longer
        2c) As such, this led to the identifcation of the shortest path (whose length is 3) between the start and end node. 
        2d) Additionally, because the starting node only has one neighbor, there is only one possible seocnd node. Therefore, there is no other possible path of the same length between the start and end node
        2e) So this method will identify shortest paths with no alternative shortest path. In this test, I assert that bfs led to the exact same path between start and end nodes identified with this method
        2f) since these paths are the shortest paths betwen the start and end node, and there are no other paths of the same length BFS might happen to return instead.
    3) Append this path to the length_3_paths list and repeat with other possible third nodes (if the second node had more than one outgoing neighbor that was not the starting node). 
    4) Repeat until all starting nodes have been iterated or until max_tests has been reached, whichever comes first

    Test 2:
    Repeat Test 1 with citation_network.adjlist

    Test 3:
    Instantiate a directed graph I made from a dictionary, and therefore I know what pairs of nodes do not have a path a priori. 
    I then assert run bfs on 5 pairs of nodes who do not have paths and test this returns None as expected.

    """

    
    def find_shortest_path(Graph_object):
        length_3_paths = [] #this will contain length 3 paths that are the shortest possible paths between the start and end node. Additionally, there are no other possible paths of the same length between the start and end node. I will test that BFS can find them
        max_tests = 100
        test_num = 0
        for starting_node in list(Graph_object.graph.nodes): #iterate through every node in the network or until max_tests condition is reached, whichever comes first
            if len(list(Graph_object.graph[starting_node])) == 1: #Go on to look for neighbors of starting nodes that only have one neighbor
                next_node = list(Graph_object.graph[starting_node])[0] #Grab the single neighbor of the starting node
                for third_node in list(Graph_object.graph[next_node]): #Because the starting node only had one outgoing neighbor, all outgoing neighbors of the next node (except for the starting node) will create a unique shortest path; this is the only possible length 3 path between the start and third node, and there is no possible shorter path. If BFS worked, it should find it
                    if third_node != starting_node: #If third node happens to be the starting node, BFS would find a length 1 path from starting node -> starting node. Ignore these because that is too easy of a test
                        length_3_paths.append([starting_node,next_node,third_node]) #add the unique shortest path to the list
                        test_num += 1
                if test_num >= max_tests: #break so the tests don't take too long
                    break

        for length_3_path in length_3_paths:
            starting_node = length_3_path[0]
            third_node = length_3_path[-1]
            assert Graph_object.bfs(starting_node,third_node) == length_3_path #test that BFS finds the shortest path, which is the same as the length_3_path


    ######### Test 1 #############
    tiny_network = Graph(filename = os.path.join(currentdir,"data/tiny_network.adjlist"))
    find_shortest_path(tiny_network) #test bfs finds the shortest paths identified in find_shortest_path in the tiny_network

    ######### Test 2 #############
    citation_network = Graph(filename = os.path.join(currentdir,"data/citation_network.adjlist")) #repeat Test 1 with larger citation network as an added test
    find_shortest_path(citation_network) #test bfs finds the shortest paths identified in find_shortest_path in the citation_network

    ######### Test 3 #############

    test_dict = {
    "A":["B","C","H"],
    "B":["E","D"],
    "C":["F","G"]
    }

    test_graph = Graph(input_dict = test_dict) #Instantiate Graph using dictionary I created, and therefore know what paths do not exist a priori

    assert test_graph.bfs(start = "B", end = "C") == None #There is no path betwen these two nodes so bfs should return None
    assert test_graph.bfs(start = "B", end = "G") == None #There is no path betwen these two nodes so bfs should return None
    assert test_graph.bfs(start = "C", end = "B") == None #There is no path betwen these two nodes so bfs should return None
    assert test_graph.bfs(start = "C", end = "H") == None #There is no path betwen these two nodes so bfs should return None
    assert test_graph.bfs(start = "G", end = "F") == None #There is no path betwen these two nodes so bfs should return None
