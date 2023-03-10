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

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #print(heuristic(problem.getStartState(), problem))
    visited = set()
    actions = []
    pQueue = util.PriorityQueue()
    g = 0
    f = heuristic(problem.getStartState(), problem) + g #f = g + h, where g is the actual cumulative cost and h is the heuristic 
    
    pQueue.push((problem.getStartState(),actions, g),f)
    print("start state" , problem.getStartState())
    while not pQueue.isEmpty():
        node = pQueue.pop()
        #print("node", node)
        state = node[0]
        actions = node[1]
        cost = node[2]
        #print("state", state)
        if(problem.isGoalState(state)):
            return actions
            

        for neighbor in problem.getSuccessors(state):
            #print("neighbor",neighbor)
            neighborState = neighbor[0]
            neighborAction = neighbor[1]
            neighborCost = neighbor[2]
            #print("neighbor state", neighborState)
            if problem.isGoalState(neighborState):
                return actions + [neighborAction]
            
            if (neighborState) not in visited:
                g = cost + neighborCost #g is the actual cumulative cost
                #print("neighbor State" , neighborState)
                f = (heuristic(neighborState, problem) + g)    
                pQueue.push((neighborState, actions+[neighborAction], g), f)
                visited.add(neighborState)


def cornersHeuristic(state: Any, problem: CornersProblem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).
    """
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)

    "*** YOUR CODE HERE ***"
    def chebyshevDistance(point1, point2):
        """    Computes the Chebyshev distance between two points.     """
        return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))
    
    # remaining_corners = list(filter(lambda x: x not in state.visited_corners, corners))
    # if not remaining_corners:
    #     return 0  # We've visited all the corners, so the distance is zero
    # nearest_corner = min(remaining_corners, key=lambda x: chebyshevDistance(state.current_position, x))

    # # Add up the estimated distances to the remaining corners and return the result
    # estimated_distances = [chebyshevDistance(nearest_corner, corner) for corner in remaining_corners]
    # return max(estimated_distances)
    corner_distances = [abs(state[0][0] - corner[0]) + abs(state[0][1] - corner[1]) for corner in corners if corner not in state[1]]
    
    return max(corner_distances)


def cornersHeuristic(state: Any, problem: CornersProblem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).
    """
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)
    def octileDistance(p1, p2):
        dx = abs(p1[0] - p2[0])
        dy = abs(p1[1] - p2[1])
        return max(dx, dy) + 0.414 * min(dx, dy)
    position, visited_corners = state

    # Check if all corners have been visited
    if len(visited_corners) == len(corners):
        return 0

    # Calculate distances from current position to unvisited corners
    unvisited_corners = [corner for corner in corners if corner not in visited_corners]
    distances = [octileDistance(position, corner) for corner in unvisited_corners]

    # Return the sum of the minimum distances
    return sum(distances)
    return 0 # Default to trivial solution


 gs = problem.startingGameState
    foodList = foodGrid.asList()
    foodCount = len(foodList)
    max_dis = 0
    part_max_dis = 0
    #print("foodCount:", foodCount)
    

    # for i in range(foodCount):
    #     for ii in range(foodCount-i-1):
    #         dis = mazeDistance(foodList[i],foodList[ii+1],gs)
    #         if dis > max_dis:
    #             max_dis = dis
    #             furthest1 = foodList[i]
    #             furthest2 = foodList[ii+1]
    #             part1 = mazeDistance(position,foodList[i],gs)
    #             part2 = mazeDistance(position,foodList[ii+1],gs)
    #             if part1 > part2:
    #                 part_max_dis = part2
    #             else:
    #                 part_max_dis = part1
    
    # return max_dis+part_max_dis 
    