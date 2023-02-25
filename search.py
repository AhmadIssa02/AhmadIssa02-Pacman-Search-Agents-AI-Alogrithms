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
import pacman
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
    visited = set()#explored nodes
    actions = [] #actions to reach the goal, will be returned
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}
    #indicating that this is the start node (it has not parents)
    stack = util.Stack()
    stack.push(start)
    while not stack.isEmpty():
        node = stack.pop()
        
        if problem.isGoalState((node['state'])):
            return actions  #if the start node is the goal, return the empty list of actions
        
        if (node['state']) not in visited:
            visited.add((node['state'])) #add the node to the explored nodes

        for neighbor in problem.getSuccessors((node['state'])):
            neighbor = {'state': neighbor[0], 'action':neighbor[1], 'cost':neighbor[2], 'parentNode': node}
            #adding the parent node to the neighbor in order to get the path
            if problem.isGoalState(neighbor['state']):
                actions.append(neighbor['action'])
                neighbor = node
                #following the path to the start node
                while 'parentNode' in node:
                    actions.append(node['action'])
                    node = node['parentNode']
                actions.reverse()
                return actions
            
            if (neighbor['state']) not in visited:
                stack.push(neighbor)
          
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    actions = [] 
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}
    queue = util.Queue()
    queue.push(start)
    while not queue.isEmpty():
        node = queue.pop()

        if problem.isGoalState((node['state'])):
            return actions
        
        if (node['state']) not in visited:
            visited.add((node['state']))

        for neighbor in problem.getSuccessors((node['state'])):
            neighbor = {'state': neighbor[0], 'action':neighbor[1], 'cost':neighbor[2], 'parentNode': node}
            if problem.isGoalState(neighbor['state']):
                actions.append(neighbor['action'])
                neighbor = node
                while 'parentNode' in node:
                    actions.append(node['action'])
                    node = node['parentNode']
                actions.reverse()
                return actions
            
            if (neighbor['state']) not in visited:
                queue.push(neighbor)

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = set() 
    actions = []    
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}   
    pQueue = util.PriorityQueue()
    pQueue.push(start,0)
    while not pQueue.isEmpty():
        node = pQueue.pop()    
        visited.add(node['state'])

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
    #print(heuristic(problem.getStartState(), problem))
    visited = set()
    actions = []
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}
    pQueue = util.PriorityQueue()
    f = heuristic(problem.getStartState(), problem) + start['cost']
    pQueue.push(start,f)
    while not pQueue.isEmpty():
        node = pQueue.pop()
        if node['state'] not in visited:
            visited.add(node['state'])
        if problem.isGoalState((node['state'])):
            while 'parentNode' in node:
                actions.append(node['action'])
                node = node['parentNode']
            actions.reverse()
            return actions
 
        
        for neighbor in problem.getSuccessors((node['state'])):
           neighbor = {'state': neighbor[0], 'action':neighbor[1], 'cost':neighbor[2], 'parentNode': node}
        #    if problem.isGoalState(neighbor['state']):
        #         actions.append(neighbor['action'])
        #         neighbor = node
        #         while 'parentNode' in node:
        #             actions.append(node['action'])
        #             node = node['parentNode']
        #         actions.reverse()
        #         return actions
           if (neighbor['state']) not in visited:
            g = node['cost'] + neighbor['cost']
            f = (heuristic(neighbor['state'], problem) + g)   
            pQueue.push(neighbor, f)
            visited.add(neighbor['state'])


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch