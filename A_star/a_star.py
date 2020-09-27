from queue import PriorityQueue
from math import sqrt

""" this algorithm is a more general a* algorithm, where it fidns a path on an infinite plane with no obsticles/walls and 
    all edges has weight = 1, this is a template to change and molde to fitt different implementations of a*"""

def h(pos, goalpos):
    #computes h(n) by calculating distance between the to vectors/nodes [X1,Y1], [goalX, goalY] 
    #return sqrt((goalpos[0]-pos[0])**2 + (goalpos[1]-pos[1])**2)
    #manhattan distance between curren node and goal node
    return abs(goalpos[0]-pos[0])+abs(goalpos[1]-pos[1])

def print_path(current, came_frome):
    #saves a list with the nodes backwards
    total_path = []
    total_path.append(current)
    while True:
        current = came_frome[(current[0],current[1])]
        if current == None:
            break
        total_path.append(current)
    print("the nodes in the path: ",total_path, "\n")



def Astar(start, goal, h):
    #the path finding algorithm
    current = start
    current_table_name = (current[0],current[1]) #table_name is a name that represent the node in dicts and sets, has form (x,y)
    open_set = PriorityQueue()  #priority queue with fscore and pos to the nodes in the frontier
    open_set_tracker = {} #to keep track of the open set, with table_name
    closed_set = []  #a list that keeps track of closed nodes
    g_score = {}   #dict that  keeps track of g_score to the nodes, table_name is the key, and g-score the value
    came_frome = {} #dict that keeps track of the nodes parents, used to draw the shortes path
    f_score = {} # dict of fscore to the node, table_name as the key, f-score as value

    g_score[current_table_name] = 0
    came_frome[current_table_name] = None
    f_score[current_table_name] = g_score[current_table_name] + h(current, goal)
    open_set.put((f_score[current_table_name],current)) #puts start node in the frontier
    open_set_tracker = {current_table_name}
    
    antall = 0
    #loop that explores the map until it finds goal or the fronitre is empty, will return false if it dose not find goal
    while not open_set.empty():
        antall += 1
        #picks out the node from the frontier with the least f_score form the pri-queue
        current = open_set.get()[1]
        current_table_name = (current[0],current[1])
        open_set_tracker.remove(current_table_name)
        closed_set.append(current_table_name)

        if current == goal:
            #we are done and have to print the path (backwards)
            print("total nodes expanded " ,antall, "\n") 
            print_path(current, came_frome)
            print("nodes in the closed set : ")
            print(closed_set)
            return True

        #print("openset")
        #print(open_set_tracker)
        for i in range(0,4):
        # finds all the neighburs
        # this for loop asumes that you can not move diagonaly and that the edgjes of the world/arrays are walls
        # else this loop will throw a index out of bounce error 
            neighbour = [current[0],current[1]]
            if i == 0:
                neighbour[0] = current[0]+1
            if i == 1:
                neighbour[1] = current[1]+1
            if i == 2:
                neighbour[0] = current[0]-1
            if i == 3:
                neighbour[1] = current[1]-1
            
            neighbour_table_name = (neighbour[0],neighbour[1])
            #calculate a g_score of the node
            temp_g_score = g_score.get(current_table_name) + 1 # siden det bare er 1 for første oppgave, må endres i senere opp
            #if the calculated g_score is lower than its current g_score update it
            if temp_g_score < g_score.get(neighbour_table_name, float('inf')):
                came_frome[neighbour_table_name] = current
                g_score[neighbour_table_name] = temp_g_score
                #updates f_score
                f_score[neighbour_table_name] = g_score[neighbour_table_name] + h(neighbour, goal)
                #if the node is not in the frontier put it in
                if neighbour_table_name not in open_set_tracker:
                    open_set.put((f_score[neighbour_table_name],neighbour))
                    open_set_tracker.add(neighbour_table_name)
                    #print(current)
                    #print(open_set_tracker)
    return False


# test of the Astar algorithm
Astar([2,2],[7,7],h)

