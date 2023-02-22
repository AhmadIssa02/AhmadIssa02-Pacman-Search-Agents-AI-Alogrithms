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