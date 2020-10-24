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

def depthFirstSearch(problem):
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

    #DFS uses LIFO which is impelementd via Stack from util.py to define the firnge
    # then the fringe which is a queue will take the states examine them and remove them looking for the goal
    # Using successors the next states, child node, will be expanded as well as their actions and cost



    fringe = util.Stack()
    start = problem.getStartState() #Starting state (5,5)
    actions = []
    cost = 0
    visited = []

    fringe.push((start,actions,cost))

    while fringe.isEmpty() is False:
        #This loop stops when fringe is empty and allow to go over all states until finding the goal

        currentState, actions, cost = fringe.pop() #assgin the names of the fringe components

        #Check if current state has been visitied

        if currentState in visited:
            continue

        else: visited.append(currentState) #if it's visited start with another state

        #Check if current state is the goal state (1,1), if yes, returning the actions

        if problem.isGoalState(currentState):
            return actions

        #Go to next states with successors. Note: next states has state, actions, and cost inside it
        nextStates = problem.getSuccessors(currentState)

        #This loop push the new state to the fringe

        for state, direction, cost in nextStates:
            fringe.push((state,actions+[direction], cost))
    return [] #Action are returned if goal state is found

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
# BFS uses FIFO and thus Queue from util.py is utilized and this is the only diff from previous code

    fringe = util.Queue()
    start = problem.getStartState()
    actions = []
    cost = 0
    visited = []
    fringe.push((start, actions, cost))

    while fringe.isEmpty() is False:

        currentState, actions, cost = fringe.pop()

        #Check visited states

        if currentState in visited:
            continue
        else: visited.append(currentState)

        #Check goal

        if problem.isGoalState(currentState):
            return actions

        #Get Successors

        nextStates = problem.getSuccessors(currentState)

        #unpack nextState
        for state, direcation, cost in nextStates:
            fringe.push((state, actions+[direcation], cost))
    return []


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #UCS tracks the cost thus using PriorityQueue, UCS aims for lowest cost which means the lowest priorty value

    start = problem.getStartState()
    actions = []
    visited = []
    cost = 0
    fringe = util.PriorityQueue()

    #Here priority value, which is cost, is pushed as a main argument
    fringe.push((start,actions),0)

    while fringe.isEmpty() is False:
        currentState, actions = fringe.pop() #The first item

        #Check visited
        if currentState in visited:
            continue
        else: visited.append(currentState)

        #Check goal
        if problem.isGoalState(currentState):
            return actions

        #Get Successors
        nextStates = problem.getSuccessors(currentState)

        #unpack
        for state, direction, cost in nextStates:
            totalActions = actions + [direction] #all actions including the last one
            cost = problem.getCostOfActions(totalActions) #gives total cost of actions
            fringe.push((state,totalActions), cost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, manhattanDistance=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # A* uses similar process such as USC but includes a heuristic
    # The heuristic used is the manhattanDistance which computes the distance to the next state

    start = problem.getStartState()
    actions = []
    visited = []
    fringe = util.PriorityQueue()

    fringe.push((start,actions),nullHeuristic(start,problem))

    while fringe.isEmpty() is False:
        currentState, actions = fringe.pop()

        #Check visited
        if currentState in visited:
            continue
        else: visited.append(currentState)

        #Check goal

        if problem.isGoalState(currentState):
            return actions

        #Get Successors

        nextStates = problem.getSuccessors(currentState)

        #Unpack
        for state, direction, cost in nextStates:
            totalActions = actions + [direction] #Get all action including last one
            costOfActions = problem.getCostOfActions(totalActions) #cost of all actions
            #hValue = manhattanDistance(state,problem) #Get huristic value using manhatten distance
            hValue = (abs(start[0]-state[0])+abs(start[1]-state[1]))
            fValue = costOfActions + hValue # f value = huristic + cost of action
            fringe.push((state,totalActions), fValue)
    return []



    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
