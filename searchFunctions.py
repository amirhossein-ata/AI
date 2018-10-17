import util

from game import Directions , Actions

UNREACHABLE_GOAL_STATE = [Directions.STOP]


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s]


def right_hand_maze_search(problem):
    """
    Q1: Search using right hand rule

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's next states:", problem.getNextStates(problem.getStartState())

    :param problem: instance of SearchProblem
    :return: list of actions
    """

    "*** YOUR CODE HERE ***"

    w=Directions.WEST
    s=Directions.SOUTH
    e=Directions.EAST
    n=Directions.NORTH
    
    startState = problem.getStartState()
    nextStates= problem.getNextStates(startState)
    
    
    
    state=startState
    result=[]
    counter = 0
    lastDirection = ''
    while(not problem.isGoalState(state)):
        nextStates = problem.getNextStates(state)
        if(len(nextStates)==1):
            lastDirection=nextStates[0][1]
            state=nextStates[0][0]
            if(lastDirection)=='West':
                result.append(w)
            elif(lastDirection)=='South':
                result.append(s)
            elif(lastDirection)=='East':
                result.append(e)
            else:
                result.append(n)
            counter +=1
        else:
            if (lastDirection == 'West'):

                if 'North' in [i[1] for i in nextStates]:
                    result.append(n)
                    lastDirection="North"
                    for i in nextStates:
                        if(i[1] == 'North'):
                            state=i[0]

                    counter +=1
                else:

                    if 'West' in [i[1] for i in nextStates]:
        
                        result.append(w)
                        lastDirection="West"
                        for i in nextStates:
                            if(i[1] == 'West'):
                                state=i[0] 
                                
                        counter +=1
                        
                    elif 'South' in [i[1] for i in nextStates]:
                        result.append(s)
                        lastDirection="South"
                        for i in nextStates:
                            if(i[1] == 'South'):
                                state=i[0] 

                        
                        counter +=1

            elif(lastDirection == 'North'):

                if 'East' in [i[1] for i in nextStates]:
                    result.append(e)
                    lastDirection="East"
                    for i in nextStates:
                        if(i[1] == 'East'):
                            state=i[0] 

        
                    counter +=1

                else:
                    if 'North' in [i[1] for i in nextStates]:
                        result.append(n)
                        lastDirection="North"
                        for i in nextStates:
                            if(i[1] == 'North'):
                                state=i[0] 

            
                        counter +=1

                    else:
                        result.append(w)
                        lastDirection="West"
                        for i in nextStates:
                            if(i[1] == 'West'):
                                state=i[0] 

                        
                        counter +=1



            elif lastDirection =='East':
                if 'South' in [i[1] for i in nextStates]:
                
                    result.append(s)
                    lastDirection="South"
                    for i in nextStates:
                        if(i[1] == 'South'):
                            state=i[0] 

            
                    counter +=1

                else:
                    
                    if 'East' in [i[1] for i in nextStates]:
                        result.append(e)
                        lastDirection="East"
                        for i in nextStates:
                            if(i[1] == 'East'):
                                state=i[0] 

            
                        counter +=1

                    elif 'North' in [i[1] for i in nextStates]:
                        result.append(n)
                        lastDirection="North"
                        for i in nextStates:
                            if(i[1] == 'North'):
                                state=i[0] 

            
                        counter +=1

            else:
                if 'West' in [i[1] for i in nextStates]:
        
                    result.append(w)
                    lastDirection="West"
                    for i in nextStates:
                        if(i[1] == 'West'):
                            state=i[0] 
                            
                    counter +=1
                else:

                    if 'South' in [i[1] for i in nextStates]:
                
                        result.append(s)
                        lastDirection="South"
                        for i in nextStates:
                            if(i[1] == 'South'):
                                state=i[0] 

                
                        counter +=1

                    elif 'East' in [i[1] for i in nextStates]:
                        result.append(e)
                        lastDirection="East"
                        for i in nextStates:
                            if(i[1] == 'East'):
                                state=i[0] 

            
                        counter +=1


    return result

def dfs(problem):
    """
    Q2: Search the deepest nodes in the search tree first.
    """

    "*** YOUR CODE HERE ***"
    visited={}
    parenthoodDictionary={}
    stack=util.Queue()
    startState = problem.getStartState()
    parenthoodDictionary[startState]=[]
    visited[startState] = True
    stack.push(startState)
    result = []


    while(not stack.isEmpty()):

        state = stack.pop()
        nextStates = problem.getNextStates(state)
            

        for i in nextStates:

            if(not parenthoodDictionary.has_key(i[0])):
                parenthoodDictionary[i[0]]=[]
                parenthoodDictionary[i[0]]=state                    
                stack.push(i[0])

        if(problem.isGoalState(state)):
           
            result =  getPath(problem,startState,state,parenthoodDictionary)
            return result
            

        
    return [Directions.STOP]

def getPath(problem,startState,goal,parenthoodDictionary):
    w=Directions.WEST
    s=Directions.SOUTH
    e=Directions.EAST
    n=Directions.NORTH
    result = []
    state = goal
  
    while(state != startState):
        childx,childy=state[0],state[1]
        state = parenthoodDictionary[state]
        
        parentx,parenty = state[0],state[1]
        action = Actions.vectorToDirection((childx -parentx , childy - parenty))
        result.insert(0,action)            

    return result



def bfs(problem):
    """
    Q3: Search the shallowest nodes in the search tree first.
    """

    "*** YOUR CODE HERE ***"
    
    visited={}
    parenthoodDictionary={}
    queue = util.Queue()
    startState = problem.getStartState()
    parenthoodDictionary[startState]=[]
    # visited[startState] = True
    queue.push(startState)
    result = []


    while(not queue.isEmpty()):

        state = queue.pop()
        nextStates = problem.getNextStates(state)
            

        for i in nextStates:

            if(not parenthoodDictionary.has_key(i[0])):
                parenthoodDictionary[i[0]]=[]
                parenthoodDictionary[i[0]]=state                    
                queue.push(i[0])
        

    
        if(problem.isGoalState(state)):
           
            result =  getPath(problem,startState,state,parenthoodDictionary)
            return result           
            break

        
    return [Directions.STOP]

def ucs_get_path(problem,startState,goal,parenthoodDictionary):
    w=Directions.WEST
    s=Directions.SOUTH
    e=Directions.EAST
    n=Directions.NORTH
    result = []
    state = goal

    while(state != startState):
        childx,childy=state[0],state[1]
        state = parenthoodDictionary[state][0]
        
        parentx,parenty = state[0],state[1]
        action = Actions.vectorToDirection((childx -parentx , childy - parenty))
        result.insert(0,action)            
    return result

def ucs(problem):
    
    """
    Q6: Search the node of least total cost first.
    """

    "*** YOUR CODE HERE ***"
    visited={}
    parenthoodDictionary={}
    queue = util.PriorityQueue()
    startState = problem.getStartState()
    visited[startState] = True
    parenthoodDictionary[startState]=[startState,0]
    queue.push(startState,0)
    result = []
    while(queue):
        state = queue.pop()
        nextStates = problem.getNextStates(state)

        parent_cost = parenthoodDictionary[state][1]
        for i in nextStates:
            cost = problem.cost_function(i)

            if(not parenthoodDictionary.has_key(i[0])):
            
                parenthoodDictionary[i[0]]=[]
                parenthoodDictionary[i[0]]=[state,cost+parent_cost]
                queue.push(i[0],parenthoodDictionary[i[0]][1])
        
     

        if(problem.isGoalState(state)):
            result =  ucs_get_path(problem,startState,state,parenthoodDictionary)
            break

    
    return result