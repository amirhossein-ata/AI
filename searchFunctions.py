import util

from game import Directions

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
    
    for i in nextStates:
        print("direction is :",i[1] ,"and state is : ",i[0])
    
    state=startState
    result=[]
    counter = 0
    lastDirection = ''
    while(not problem.isGoalState(state)):
        nextStates = problem.getNextStates(state)
        if(len(nextStates)==1):
            print("got no choice dude!")
            print(nextStates[0][1])
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
                    print("nextStates : " , nextStates)
                    print('last direction is : '+lastDirection + 'going North ' , state)
                    counter +=1
                else:

                    if 'West' in [i[1] for i in nextStates]:
        
                        result.append(w)
                        lastDirection="West"
                        for i in nextStates:
                            if(i[1] == 'West'):
                                state=i[0] 
                                
                        print("nextStates : " , nextStates)
                        print('last direction is : '+lastDirection + 'going West ' , state)
                        counter +=1
                        
                    elif 'South' in [i[1] for i in nextStates]:
                        result.append(s)
                        lastDirection="South"
                        for i in nextStates:
                            if(i[1] == 'South'):
                                state=i[0] 

                        print("nextStates : " , nextStates)            
                        print('last direction is : '+lastDirection + 'going South ' , state) 
                        
                        counter +=1

            elif(lastDirection == 'North'):

                if 'East' in [i[1] for i in nextStates]:
                    result.append(e)
                    lastDirection="East"
                    for i in nextStates:
                        if(i[1] == 'East'):
                            state=i[0] 

                    print("nextStates : " , nextStates)            
                    print('last direction is : '+lastDirection + 'going east ' , state)
        
                    counter +=1

                else:
                    if 'North' in [i[1] for i in nextStates]:
                        result.append(n)
                        lastDirection="North"
                        for i in nextStates:
                            if(i[1] == 'North'):
                                state=i[0] 

                        print("nextStates : " , nextStates)            
                        print('last direction is : '+lastDirection + 'going north ' , state)
            
                        counter +=1

                    else:
                        result.append(w)
                        lastDirection="West"
                        for i in nextStates:
                            if(i[1] == 'West'):
                                state=i[0] 

                        print("nextStates : " , nextStates)            
                        print('last direction is : '+lastDirection + 'going west ' , state)
                        
                        counter +=1



            elif lastDirection =='East':
                if 'South' in [i[1] for i in nextStates]:
                
                    result.append(s)
                    lastDirection="South"
                    for i in nextStates:
                        if(i[1] == 'South'):
                            state=i[0] 

                    print("nextStates : " , nextStates)            
                    print('last direction is : '+lastDirection + 'going south ' , state)
            
                    counter +=1

                else:
                    
                    if 'East' in [i[1] for i in nextStates]:
                        result.append(e)
                        lastDirection="East"
                        for i in nextStates:
                            if(i[1] == 'East'):
                                state=i[0] 

                        print("nextStates : " , nextStates)            
                        print('last direction is : '+lastDirection + 'going east ' , state)
            
                        counter +=1

                    elif 'North' in [i[1] for i in nextStates]:
                        result.append(n)
                        lastDirection="North"
                        for i in nextStates:
                            if(i[1] == 'North'):
                                state=i[0] 

                        print("nextStates : " , nextStates)            
                        print('last direction is : '+lastDirection + 'going north ' , state)
            
                        counter +=1

            else:
                if 'West' in [i[1] for i in nextStates]:
        
                    result.append(w)
                    lastDirection="West"
                    for i in nextStates:
                        if(i[1] == 'West'):
                            state=i[0] 
                            
                    print("nextStates : " , nextStates)
                    print('last direction is : '+lastDirection + 'going West ' , state)
                    counter +=1
                else:

                    if 'South' in [i[1] for i in nextStates]:
                
                        result.append(s)
                        lastDirection="South"
                        for i in nextStates:
                            if(i[1] == 'South'):
                                state=i[0] 

                        print("nextStates : " , nextStates)            
                        print('last direction is : '+lastDirection + 'going south ' , state)
                
                        counter +=1

                    elif 'East' in [i[1] for i in nextStates]:
                        result.append(e)
                        lastDirection="East"
                        for i in nextStates:
                            if(i[1] == 'East'):
                                state=i[0] 

                        print("nextStates : " , nextStates)            
                        print('last direction is : '+lastDirection + 'going east ' , state)
            
                        counter +=1


    return result

def dfs(problem):
    """
    Q2: Search the deepest nodes in the search tree first.
    """

    "*** YOUR CODE HERE ***"

    visited={}
    parenthoodDictionary={}
    stack=[]
    startState = problem.getStartState()
    visited[startState] = True
    stack.append(startState)
    result = []
    parents=[]
    lastState=startState
    while(stack):
        state = stack.pop()
        if(not parenthoodDictionary.has_key(state)):
            parenthoodDictionary[state]=[]
        # print(queue)

        if(len(state) == 2) :
            nextStates = problem.getNextStates(state)
            for i in nextStates:
                parenthoodDictionary[i]=[]
            
            for i in nextStates:    
                if (not visited.has_key(i[0])):
                    visited[i[0]] = False
            for i in nextStates:
                if (not visited[i[0]]):
                    parenthoodDictionary[i].append(state)     
                    parenthoodDictionary[state].append(i)     

        else:
            nextStates = problem.getNextStates(state[0])
            for i in nextStates:
                parenthoodDictionary[i]=[]
            for i in nextStates:
                if (not visited.has_key(i[0])):
                    visited[i[0]] = False
            for i in nextStates:
                if (not visited[i[0]]):
                    parenthoodDictionary[i].append(state)                    
                    parenthoodDictionary[state].append(i)                    



            if(problem.isGoalState(state[0])):
                print('hoooooooooooooooooooooooooooora')
                result =  getPath(problem,state,parenthoodDictionary)
                break

     
        for i in nextStates:
            if (not visited[i[0]]):
                visited[i[0]] = True                
                stack.append(i)
    
    return result      


def getPath(problem,goal,parenthoodDictionary):
    w=Directions.WEST
    s=Directions.SOUTH
    e=Directions.EAST
    n=Directions.NORTH
    result = []
    state = goal
    startState = problem.getStartState()
    while(state != startState):
        if(state[1] == 'West'):
            result.insert(0,w)
        elif state[1] == 'East':
            result.insert(0,e)
        elif state[1] == 'South':
            result.insert(0,s)
        elif state[1] == 'North':
            result.insert(0,n)            
      
        state = parenthoodDictionary[state][0]
            
    print(result)
    return result



def bfs(problem):
    """
    Q3: Search the shallowest nodes in the search tree first.
    """

    "*** YOUR CODE HERE ***"
    
    visited={}
    parenthoodDictionary={}
    queue=[]
    startState = problem.getStartState()
    visited[startState] = True
    queue.append(startState)
    result = []
    parents=[]
    lastState=startState
    while(queue):
        state = queue.pop(0)
        if(not parenthoodDictionary.has_key(state)):
            parenthoodDictionary[state]=[]
        # print(queue)

        if(len(state) == 2) :
            nextStates = problem.getNextStates(state)
            for i in nextStates:
                parenthoodDictionary[i]=[]
            
            for i in nextStates:
                if (not visited.has_key(i[0])):
                    visited[i[0]] = False
            for i in nextStates:
                if (not visited[i[0]]):
                    parenthoodDictionary[i].append(state)     
                    parenthoodDictionary[state].append(i)     

        else:
            nextStates = problem.getNextStates(state[0])
            for i in nextStates:
                parenthoodDictionary[i]=[]
            for i in nextStates:
                if (not visited.has_key(i[0])):
                    visited[i[0]] = False
            for i in nextStates:
                if (not visited[i[0]]):
                    parenthoodDictionary[i].append(state)                    
                    parenthoodDictionary[state].append(i)                    



            if(problem.isGoalState(state[0])):
                print('hoooooooooooooooooooooooooooora')
                result =  getPath(problem,state,parenthoodDictionary)
                break

        
        for i in nextStates:
            if (not visited[i[0]]):
                visited[i[0]] = True                
                queue.append(i)
    
    return result
def ucs(problem):
    
    """
    Q6: Search the node of least total cost first.
    """

    "*** YOUR CODE HERE ***"
    
    visited={}
    parenthoodDictionary={}
    queue=[]
    startState = problem.getStartState()
    visited[startState] = True
    queue = util.PriorityQueue
    print(problem.cost_function(startState))
    
    result = []
    parents=[]
    lastState=startState
    while(queue):
        state = queue.pop(0)
        if(not parenthoodDictionary.has_key(state)):
            parenthoodDictionary[state]=[]
        # print(queue)

        if(len(state) == 2) :
            nextStates = problem.getNextStates(state)
            for i in nextStates:
                parenthoodDictionary[i]=[]
            
            for i in nextStates:
                if (not visited.has_key(i[0])):
                    visited[i[0]] = False
            for i in nextStates:
                if (not visited[i[0]]):
                    parenthoodDictionary[i].append(state)     
                    parenthoodDictionary[state].append(i)     

        else:
            nextStates = problem.getNextStates(state[0])
            for i in nextStates:
                parenthoodDictionary[i]=[]
            for i in nextStates:
                if (not visited.has_key(i[0])):
                    visited[i[0]] = False
            for i in nextStates:
                if (not visited[i[0]]):
                    parenthoodDictionary[i].append(state)                    
                    parenthoodDictionary[state].append(i)                    



            if(problem.isGoalState(state[0])):
                print('hoooooooooooooooooooooooooooora')
                result =  getPath(problem,state,parenthoodDictionary)
                break

        
        for i in nextStates:
            if (not visited[i[0]]):
                visited[i[0]] = True                
                queue.append(i)
    
    return result