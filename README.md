![BuildStatus](https://github.com/shirondru/Project2/.github/workflows/test.yml/badge.svg?event=push)

# Project 2
Breadth-first search

Breadth-first search (BFS) is an algorithm for searching a graph in a layer-by-layer manner; all nodes in a given layer are visited before to moving to the next layer, and this ensures the shortest path between a pair of nodes (if it exists) will be found by BFS. BFS works by, starting with the starting node, adding unvisited neighboring nodes to a queue and visiting them. As these neighbors are visited, add their unvisited neighbors to the queue. This produces a queue with nodes in the current layer at the front, and subsequent layers at the end. If searching for the shortest path between a pair of nodes, the search can be terminated once the target node has been found, and the path to that node can be backtraced if each node's parent node is documented.