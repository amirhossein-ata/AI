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


def getPath(problem,startState,goal,parenthoodDictionary):
    w=Directions.WEST
    s=Directions.SOUTH
    e=Directions.EAST
    n=Directions.NORTH
    result = []
    state = goal
    # print(startState)
    print(problem.getStartState())
    print(goal)
  
    while(state != startState):
        print('state is : ',state)
        childx,childy=state[0],state[1]
        state = parenthoodDictionary[state]
        print('state pp is : ',state)
        
        parentx,parenty = state[0],state[1]
        action = Actions.vectorToDirection((childx -parentx , childy - parenty))
        result.insert(0,action)            
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
    parenthoodDictionary[startState]=[]
    visited[startState] = True
    queue.append(startState)
    result = []


    while(queue):

        state = queue.pop(0)
        nextStates = problem.getNextStates(state)
            

        for i in nextStates:

            if(not parenthoodDictionary.has_key(i[0])):
                parenthoodDictionary[i[0]]=[]
            
            if (not visited.has_key(i[0])):
                visited[i[0]] = False
            
            if (not visited[i[0]]):
                parenthoodDictionary[i[0]]=state                    
        

        if(problem.isGoalState(state)):
           
            print('hoooooooooooooooooooooooooooora' , state)   
            result =  getPath(problem,startState,state,parenthoodDictionary)
           
            break

        
        for i in nextStates:
            if (not visited[i[0]]):
                visited[i[0]] = True
                queue.append(i[0])
    
    print('omad biron?')
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

    queue.push(startState,0)
    result = []
    while(queue):
        state = queue.pop()
        if(not parenthoodDictionary.has_key(state)):
            parenthoodDictionary[state]=[]
        # print(queue)

        # print(parenthoodDictionary[state])
        if(len(state) == 2) :
            nextStates = problem.getNextStates(state)
            for i in nextStates:
                parenthoodDictionary[i]=[]
            
            for i in nextStates:
                if (not visited.has_key(i[0])):
                    visited[i[0]] = False

            for i in nextStates:
                cost = problem.cost_function(i)
                if (not visited[i[0]]):
                    parenthoodDictionary[i].append(state)     
                    parenthoodDictionary[i].append(cost)
                    parenthoodDictionary[state].append(i)     

        else:
            nextStates = problem.getNextStates(state[0])
            for i in nextStates:
                parenthoodDictionary[i]=[]
           
            for i in nextStates:
                if (not visited.has_key(i[0])):
                    visited[i[0]] = False

            cost_of_father = parenthoodDictionary[state][1]
            # print('fathers cooooooooooost is :',cost_of_father)
            for i in nextStates:
                cost = problem.cost_function(i)
                if (not visited[i[0]]):
                    parenthoodDictionary[i].append(state)
                    parenthoodDictionary[i].append(cost+cost_of_father)
                    parenthoodDictionary[state].append(i)                    



            if(problem.isGoalState(state[0])):
                print('hoooooooooooooooooooooooooooora')
                result =  getPath(problem,state,parenthoodDictionary)
                break

        parent_cost = 0       
        print(parenthoodDictionary[state]) 
        if(len(parenthoodDictionary[state]) > 1):
            if(not isinstance(parenthoodDictionary[state][1],tuple)):
                parent_cost = parenthoodDictionary[state][1]
        for i in nextStates:
            child_cost = problem.cost_function(i)
            print('paaaaarent cost is : ',parent_cost,type(parent_cost) ,' child cost is : ',child_cost,type(child_cost))
            total_cost = parent_cost + child_cost
            print('so in total : ',parent_cost + child_cost)
            if (not visited[i[0]]):
                visited[i[0]] = True                
                queue.push(i,total_cost)
    
    return result