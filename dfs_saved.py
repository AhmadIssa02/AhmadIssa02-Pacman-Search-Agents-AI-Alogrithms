    visited = []
    actions = []
    start = (problem.getStartState(), actions)
    print( " I am start ", start)
    stack = util.Stack()
    stack.push(start)
        
    while stack.isEmpty() == False:
        node = stack.pop()
        print( " I am node ", node)
        if(node != start):
            actions.append(node[1])

        if problem.isGoalState((node[0])):
            ###pass the goal state to the function###
            print("I am the goal")
            return actions
        
        if (node[0]) not in visited:
            visited.append((node[0]))
            ######visit the node######
        
        for neighbor in problem.getSuccessors((node[0])):
            if (neighbor[0]) not in visited:
                stack.push(neighbor)   
    print("actions", actions)

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
          