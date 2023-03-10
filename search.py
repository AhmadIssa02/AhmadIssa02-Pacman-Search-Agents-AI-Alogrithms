# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState(), type(problem.getStartState()))
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    Frontier = util.Stack()
    visited = []
    Frontier.push((problem.getStartState(), []))
    while not Frontier.isEmpty():
        node = Frontier.pop()
        state = node[0]
        actions = node[1]
        for neighbor in problem.getSuccessors(state):
            neighborState = neighbor[0]
            action = neighbor[1]
            if neighborState not in visited:
                if problem.isGoalState(neighborState):
                    return actions + [action]
                Frontier.push((neighborState, actions + [action]))
                visited.append(neighborState)
       
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    Frontier = util.Queue()
    visited = []
    Frontier.push((problem.getStartState(), []))
    while Frontier.isEmpty() == 0:
        node = Frontier.pop()
        state = node[0]
        actions = node[1]
        for neighbor in problem.getSuccessors(state):
            neighborState = neighbor[0]
            action = neighbor[1]
            if neighborState not in visited:
                if problem.isGoalState(neighborState):
                    return actions + [action]
                Frontier.push((neighborState, actions + [action]))
                visited.append( neighborState )
 

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = set() 
    actions = []    
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}   
    pQueue = util.PriorityQueue()
    pQueue.push(start,0) #0 is the initial cost of the start node, it will be increased as the search goes on
    while not pQueue.isEmpty():
        node = pQueue.pop()    
        visited.add(node['state'])
        
        #here we are applying the goal test when expanding the node not when pushing it to the queue
        #this is because we want to make sure that the goal is the node with the least cost, not the first one we find

        if problem.isGoalState((node['state'])):
            while 'parentNode' in node:
                actions.append(node['action'])
                node = node['parentNode']
            actions.reverse()
            return actions
            
        for neighbor in problem.getSuccessors((node['state'])):
            neighbor = {'state': neighbor[0], 'action':neighbor[1], 'cost':neighbor[2], 'parentNode': node}
            if (neighbor['state']) not in visited:
                neighbor['cost'] = node['cost'] + neighbor['cost']
                pQueue.push(neighbor, neighbor['cost'])
                visited.add(neighbor['state'])
               

  
            



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []
    actions = []
    pQueue = util.PriorityQueue()
    g = 0
    f = heuristic(problem.getStartState(), problem) + g #f = g + h, where g is the actual cumulative cost and h is the heuristic 
    pQueue.push((problem.getStartState(),actions, g),f) #push the start node to the queue with the heuristic being its priority
    while not pQueue.isEmpty():
        node = pQueue.pop()
        state = node[0]
        actions = node[1]
        cost = node[2]
        if(problem.isGoalState(state)):
            return actions

        for neighbor in problem.getSuccessors(state):
            neighborState = neighbor[0]
            neighborAction = neighbor[1]
            neighborCost = neighbor[2]
            if problem.isGoalState(neighborState):
                #print("heuristic = ", heuristic(neighborState,problem))
                return actions + [neighborAction]
            
            if (neighborState) not in visited:
                if heuristic(state, problem) > (neighborCost + heuristic(neighborState, problem)):#checking if my heuristic is consistent
                    print("heuristic is inconsistent")
                g = cost + neighborCost #g is the actual cumulative cost
                f = (heuristic(neighborState, problem) + g)    
                pQueue.push((neighborState, actions+[neighborAction], g), f)
                visited.append(neighborState)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
