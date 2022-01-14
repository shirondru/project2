# write tests for bfs
import pytest
from search import Graph 
import os
import random
currentdir = os.getcwd() #GitHub/project2/

# @pytest.fixture
def test_bfs_traversal():
    """
    
    """


    ############# Test 1 #############
    # Here I test that bfs traverses a graoh in the expected breadth-first manner and returns nodes in the correct order

    test_dict = {
    "A":["B","C","H"],
    "B":["E","D"],
    "C":["F","G"]
    }

    test_graph = Graph(input_dict = test_dict) #Instantiate Graph using dictionary I created. This graph is simpler than tiny_network so it is easy to assert the order of traversal a priori
    assert test_graph.bfs(start = "A") == ["A","B","C","H","E","D","F","G"]
    assert test_graph.bfs(start = "B") == ["B","E","D"]
    assert test_graph.bfs(start = "C") == ["C","F","G"]
    assert test_graph.bfs(start = "H") == ["H"]
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
    3) Append this path to the length_3_paths list and repeat with other possible third nodes. 
    4) Repeat until all starting nodes have been iterated or until max_tests has been reached, whichever comes first

    Test 2:
    Repeat Test 1 with citation_network.adjlist

    Test 3:
    Instantiate a directed graph I made from a dictionary, and therefore I know what pairs of nodes do not have a path a priori. 
    I then assert run bfs on 5 pairs of nodes who do not have paths and test this returns None as expected.

    """

    ######### Test 1 #############
    def find_shortest_path(Graph_object):

        
        length_3_paths = [] #this will contain length 3 paths that are the shortest possible paths between the start and end node. Additionally, there are no other possible paths of the same length between the start and end node. I will test that BFS can find them
        max_tests = 100
        test_num = 0
        for starting_node in list(Graph_object.graph.nodes): #iterate through every node in the network or until max_tests condition is reached, whichever comes first
            if len(list(Graph_object.graph[starting_node])) == 1: #Go on to look for neighbors of starting nodes that only have one neighbor
                next_node = list(Graph_object.graph[starting_node])[0] #Grab the single neighbor of the starting node
                for third_node in list(Graph_object.graph[next_node]): #Because the starting node only had one outgoing neighbor, all outgoing neighbors of the next node (except for the starting node) will create a unique shortest path; the only possible path is the shortest (length 3) path. If BFS worked, it should find it
                    if third_node != starting_node: #If third node happens to be the starting node, BFS would find a length 1 path from starting node -> starting node. Ignore these because that is too easy of a test
                        length_3_paths.append([starting_node,next_node,third_node]) #add the unique shortest path to the list
                        test_num += 1
                if test_num >= max_tests: #break so the tests don't take too long
                    break

        for length_3_path in length_3_paths:
            starting_node = length_3_path[0]
            third_node = length_3_path[-1]
            assert Graph_object.bfs(starting_node,third_node) == length_3_path

    tiny_network = Graph(filename = os.path.join(currentdir,"data/tiny_network.adjlist"))
    find_shortest_path(tiny_network)




    ######### Test 2 #############
    citation_network = Graph(filename = os.path.join(currentdir,"data/citation_network.adjlist")) #repeat Test 1 with larger citation network as an added test
    find_shortest_path(citation_network)


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
