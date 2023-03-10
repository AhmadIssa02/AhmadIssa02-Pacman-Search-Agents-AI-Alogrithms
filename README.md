Question 1)
In this question, we applied DFS, which is an algorithm that searches the graph in a depth first manner, which means it checks the first neighbor of each node and keeps going deeper and deeper until it reaches the last node, then it checks the next neighbor and so on.
In DFS, we use a stack that manages the elements in a first in last out order. 
Our fronteir represents our stack.
we loop through the fronteir till its empty, then for every neighbor, we check if its visited or not as we do not want to revisit previously visited nodes (to avoid getting stuck in a cycle). 
I kept a list of visited nodes and thats how I checked whether an element was previously visited or not. 
I kept track of the list of actions as I pushed the action list with every element we visit and added the new action we need to take for every new element we visit. This way, each element is pushed with the list of actions to reach it. 

DFS managed to find the goal node after expanding 14 nodes and with a cost of 10 in the tiny maze. 
DFS managed to find the goal node after expanding 140 nodes and with a cost of 130 in the medium maze. 
DFS managed to find the goal node after expanding 391 nodes and with a cost of 210 in the big maze. 

Question 2)
In this question, we are asked to apply BFS, which is a function that searches the graph in a breadth first manner, meaning it vsits every layer one at a time and expands until it reaches the last element. 
In BFS, we use a queue as it manages the elements in a first in first out order. 
The code is exactly like DFS, but we use a queue instead of a stack. 

BFS managed to find the goal node after expanding 16 nodes and with a cost of 10 in the tiny maze. 
BFS managed to find the goal node after expanding 268 nodes and with a cost of 68 in the medium maze. 
BFS managed to find the goal node after expanding 618 nodes and with a cost of 210 in the big maze. 

Question 3)
Uniform Cost Search (UCS) is a search algorithm used for finding the shortest path between a starting node and a goal node in a weighted graph. It is a variant of Dijkstra's algorithm, but unlike Dijkstra's algorithm, UCS considers the cost of each path taken to the current node, rather than the distance from the starting node.

In UCS, nodes are expanded in increasing order of their path cost from the start node. The algorithm maintains a priority queue of nodes to be expanded, where the priority of each node is its path cost from the start node. Initially, the priority queue contains only the start node with a priority of zero.

At each step, the algorithm dequeues the node with the lowest priority (i.e., the node with the lowest path cost from the start node) from the priority queue and expands it, considering all its neighboring nodes. If a neighboring node has not been visited before, the algorithm adds it to the priority queue with a priority equal to the sum of the cost of the path to reach that node from the start node and the cost of the edge between the current node and the neighboring node. If the neighboring node has already been visited, the algorithm updates its priority in the priority queue if the new path cost is lower than the old path cost.

The algorithm terminates when the goal node is dequeued from the priority queue, or when the priority queue becomes empty (which indicates that there is no path from the start node to the goal node).

In UCS, we need to keep track of the total cost needed to reach a certain node, which is why I pushed the cumulative cost alongside the state of the node as the priority of the queue. 

UCS managed to find the goal node after expanding 15 nodes and with a cost of 8 in the tiny maze. 
UCS managed to find the goal node after expanding 269 nodes and with a cost of 68 in the medium maze. 
UCS managed to find the goal node after expanding 620 nodes and with a cost of 210 in the big maze. 
UCS managed to find the goal node after expanding 682 nodes and with a cost of 54 in the open maze. 

Question 4)
A star is a heuristic search algorithm that combines the cost of the path from the start node to the current node (g-value) and the heuristic estimate of the cost from the current node to the goal node (h-value) to determine the next node to explore. It uses a function which is the addition of these two values (f = h +g). The algorithm maintains a priority queue of nodes to explore, with the node with the lowest estimated cost (f-value) being explored first. During the search, the algorithm updates the g-value of each explored node to reflect the actual cost of the path from the start node to that node.

A* is guaranteed to find the shortest path from the start node to the goal node, as long as the heuristic function used is admissible (never overestimates the actual cost to reach the goal) and consistent (satisfies the triangle inequality).

In this function I wrote a condition which checks whethere my heuristic is consistent or not 
It is not consistent when heuristic(state) > (neighborCost + heuristic(neighborState). 

A Star managed to find the goal node after expanding 14 nodes and with a cost of 8 in the tiny maze. 
A Star managed to find the goal node after expanding 222 nodes and with a cost of 68 in the medium maze. 
A Star managed to find the goal node after expanding 550 nodes and with a cost of 210 in the big maze. 
A Star managed to find the goal node after expanding 534 nodes and with a cost of 54 in the open maze. 

Question 5)
In this question, we are asked to run the BFS algorithm but with a different goal node, instead of one goal node being our goal, we need to go to all four corners, which is why I added a list alongside the getStartState function. This list will save the previously visited corners. In the getSuccessors function, I made sure to push this list of visited corners alongside each successor to maintain consistency. Also, if the successor is a corner, I would add that corner to the list of visited corners. 

BFS managed to find the four corners after expanding 410 nodes and with a cost of 28 in the tiny corners maze.
BFS managed to find the four corners after expanding 2381 nodes and with a cost of 106 in the medium corners maze. 
BFS managed to find the four corners after expanding 9757 nodes and with a cost of 162 and takes 3.8 seconds in the big corners maze. 


Question 6)
Here we need to run aStar algorithm in the corners problem but with a heuristic. This heuristic should consider the distances to all the corners. 
In the corners heuristic function, I tried using different heuristics that would return a distance estimate of the next corner, I made sure these heuristics are consistent using the consistent condition in the astar algorithm (i.e heuristic(state) > (neighborCost + heuristic(neighborState) ). I tried the Octile distance, Chebyshev distance, Euclidean distance, but the Manhattan distance was the heuristic that produced the best results. 

I calculated the Manhattan distance for each corner and returned the max value to retun an estimate of how far a node is from the furthest corner. My algorithm was able to find the goal after expanding 1352 nodes and in around 0.1 seconds.


Question 7)

In this question, we needed to find the best path for a graph with randomly placed food dots. our heuristic should keep in mind the distances for all those food dots. Hince, we used the dictionary "problem.heuristicInfo()". In this dictionary, I saved the distances for every node with every food in the graph. This way I saved time recalculating these distances. Then, I returned the maximum distance from all the food dots just like I did in the previous question using the manhattan distance. This algorithm managed to find the best path after expanding 4111 nodes only and in less than 2 seconds. 


Question 8)
In this problem, we are asked to follow the closest dot. In order to do that I ran BFS on every state until I found the first dot, which is the closest one. In here, I just needed to run BFS and change the isGoalState function, in here the goal is any dot in the food list, which gets updated by default every time we visit a node. This way, when bfs run on each state, it checks its closest neighbors first, if the neighbor is food, it returns true.     

