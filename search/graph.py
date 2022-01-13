import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, init_dict=None, filename = None):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        if filename:
            self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
        else:
            self.graph = nx.DiGraph(init_dict)
    def __trace_path(self,parent,start,end=None):
        """
        This method traces back the path to find the end node by utilizing a dictionary `parent`, whose values
        are the parent nodes to the keys. Specifically, the method:
        1. Initiates a list, `path`, with only the end node inside the list. If there was no end node, the if statement would be skipped and the method would return None
        Within a While Loop:
        2. Finds the parent of the end node by accessing `parent` using the end node as a key.
        3. Appending the parent of the end node to the end of `path`
        4. While loop exits if the parent of the end node is the start node
        5. Otherwise, the next parent node is found by accessing `parent` using the most recent node (found at the end of `path`)
        6. Append that parent node to `path`
        7. While loop exits if that parent node is the start node
        8. Repeat 5-8 until start node is added to the end of `path`
        9. Reverse `path` from having the order end-> start to having the order start->end
        
        If end == None, there is no path, and this method will return None. However, if end == None,
        this method will never be called because the `bfs` method only calls __trace_path once the end node was found.
    
        
        This method is only meant to be accessed from within the bfs method

        """
        if end: #True if end != None
            path = [end] #if there was an end node, initialize the list with it inside.
            
            while path[-1] != start: #once path contains all nodes from end->start exit the loop
                parent_node = parent[path[-1]] #Parent node of the key is the value returned
                path.append(parent_node)
            return path[::-1] #reverse path so it has order start->end then return it

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        parent = {}
        visited = [start] #initialize visited list
        
        
        queue = deque([start]) #initialize deque object with start node already inserted
        #using a deque object instead of a list because popping an item from the front of a list in python has complexity O(N), because the rest of the list needs to be shifted afterwards.
        #while deque objects are built to pop an item from the front of a list with O(1)

        
        
        #The below while loop will do the following:
        # 1. Mark the first node in the queue as the current node and dequeue it
        # 2. If the current node is the end node, break the loop by returning the path, which will be the shortest path because of BFS
        # 3. If the current node is not the end node, iterative through the current node's outgoing neighbors, adding unvisited ones to the end of the queue and marking them as visited. Mark them as visited here because all nodes in the graph will be visited unless the end node is reached and the if statement condition prevents nodes from appearing in the visited list more than once
        # 4. Repeat 1-3 until the end node is found or the queue becomes empty
        # 5. If the end node is found, return the shortest path
        # 6. If the queue becomes empty, there must not be a path. Return None
        while queue: #non-empty lists are True in Python. While loop will continue until queue runs out
            current_node = queue.popleft() #dequeue node at index 0 and mark it as current node

            if current_node == end: #if current node is the end node break the loop by returning the shortest path
                path = self.__trace_path(parent,start,end)
                return path
            else:
                for out_neighbor in self.graph[current_node]: #iterate through all outgoing neighbors from current node
                    if out_neighbor not in visited: 
                        parent[out_neighbor] = current_node #current_node is parent node of out_neighbor. This dictionary will be used to backtrace the shortest path in the __trace_path method
                        queue.append(out_neighbor) #add outgoing neighbor to queue if it has not already been visited
                        visited.append(out_neighbor)
        if end == None: 
            return visited #the visited list contains the order of traversal
        return None #if queue becomes empty a path was not found. Return None to indicative there is no path. 
            #This line could have been skipped and the method would return None by default if nothing else was returned. But it is clearer to explicitly return None

    


