#dfs
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
       
#ucs
    visited = set() 
    actions = []    
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}   
    pQueue = util.PriorityQueue()
    pQueue.push(start,0)
    while not pQueue.isEmpty():
        node = pQueue.pop()    
        #print(node['state'], node['cost'])
        visited.add(node['state'])
        if problem.isGoalState((node['state'])):
            actions.append(neighbor['action'])
            neighbor = node
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
               

  

#ucs
    visited = set() 
    actions = []    
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}   
    pQueue = []
    pQueue.append([start,0])
    while len(pQueue) > 0:
        pQueue.sort(key=lambda x: x[1])
        node = pQueue[-1]
        visited.add(node[0])
        if problem.isGoalState((node[0])):
            actions.append(neighbor[1])
            neighbor = node
            while 'parentNode' in node:
                actions.append(node[1])
                node = node[4]
            actions.reverse()
            return actions
            
        for neighbor in problem.getSuccessors((node['state'])):
            neighbor = {'state': neighbor[0], 'action':neighbor[1], 'cost':neighbor[2], 'parentNode': node}
            if (neighbor[0]) not in visited:
                pQueue.append([neighbor,neighbor[2]])


#bfs      
   visited = set()
    actions = [] 
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}
    queue = util.Queue()
    queue.push(start)
    while not queue.isEmpty():
        node = queue.pop()
        print("node popped", node['state'])
        if problem.isGoalState((node['state'])):
            return actions
        
        if (node['state']) not in visited:
            print("node visited", node['state'])
            visited.add((node['state']))

        for neighbor in problem.getSuccessors((node['state'])):
            neighbor = {'state': neighbor[0], 'action':neighbor[1], 'cost':neighbor[2], 'parentNode': node}
            print("hello")
            if problem.isGoalState(neighbor['state']):
                print("goal found", neighbor['state'])
                actions.append(neighbor['action'])
                neighbor = node
                while 'parentNode' in node:
                    actions.append(node['action'])
                    node = node['parentNode']
                actions.reverse()
                return actions
            
            if (neighbor['state']) not in visited:
                print("neighbor pushed", neighbor['state'])
                queue.push(neighbor)


class CornersProblem(search.SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function
    """

    def __init__(self, startingGameState: pacman.GameState):
        """
        Stores the walls, pacman's starting position and corners.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print('Warning: no food in corner ' + str(corner))
        self._expanded = 0 # DO NOT CHANGE; Number of search nodes expanded
        # Please add any code here which you would like to use
        # in initializing the problem
        "*** YOUR CODE HERE ***"
        self.visitedCorners = []
        

    def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state
        space)
        """
        "*** YOUR CODE HERE ***"
        return (self.startingPosition,)

    def isGoalState(self, state: Any):
        """
        Returns whether this search state is a goal state of the problem.
        """
        "*** YOUR CODE HERE ***"

        if(state[0] in self.corners ):
            # and state not in self.visitedCorners
            print("isGoalState", state)
            # addedTuple = state[0]
            # newTuple = state[1] + addedTuple
            # state[1] = newTuple
            # state[1].append(state[0])
            # self.visitedCorners.append(state)
            # print("isGoalState", state)
        return (self.visitedCorners.__len__() == 4)

    def getSuccessors(self, state: Any):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'action' is the action required to get there, and 'stepCost'
            is the incremental cost of expanding to that successor
        """
        print("state", state)
        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            # Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            #   x,y = currentPosition
            #   dx, dy = Actions.directionToVector(action)
            #   nextx, nexty = int(x + dx), int(y + dy)
            #   hitsWall = self.walls[nextx][nexty]

            "*** YOUR CODE HERE ***"
            x,y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                successors.append(((nextx, nexty), action, 1))

        self._expanded += 1 # DO NOT CHANGE
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        if actions == None: return 999999
        x,y= self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)



#astar
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #print(heuristic(problem.getStartState(), problem))
    visited = set()
    actions = []
    start = {'state':problem.getStartState(),'action': actions, 'cost':0}
    pQueue = util.PriorityQueue()
    f = heuristic(problem.getStartState(), problem) + start['cost']#f = g + h, where g is the actual cost and h is the heuristic 
    pQueue.push(start,f)
    while not pQueue.isEmpty():
        node = pQueue.pop()
        if node['state'] not in visited:
            visited.add(node['state'])
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
                g = node['cost'] + neighbor['cost'] #g is the actual cumulative cost
                f = (heuristic(neighbor['state'], problem) + g)  
                pQueue.push(neighbor, f)
                visited.add(neighbor['state'])

