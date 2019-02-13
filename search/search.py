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
    visited=[]






def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    direction = {}
    cost = {}
    queue = util.PriorityQueue()
    visitedList = []
    (state, toDirection, toCost) = (problem.getStartState(), [], 0)
    value = heuristic(state, problem)
    visitedList.append((state, toCost+value))
    direction[state] = []
    cost[state] = 0
    while not problem.isGoalState(state):
        successors = problem.getSuccessors(state)
        for child in successors:
            stateChild = child[0]
            ChildDirection = child[1]
            Childcost = child[2]
            visitedExist = False
            total_cost = toCost + Childcost
            for (existingState, existingCost) in visitedList:
                if (stateChild == existingState) and (total_cost >= existingCost):
                    visitedExist = True
                    break

            if not visitedExist:
                direction[stateChild] = direction[state] + [ChildDirection]
                cost[stateChild] = total_cost
                value = heuristic(stateChild, problem)
                queue.push(stateChild, total_cost+value)
                visitedList.append((stateChild, total_cost+value))

        state = queue.pop()
        toCost = cost[state]

    return direction[state]









def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    direction = {}
    cost = {}
    queue = util.PriorityQueue()
    visitedList = []
    (state, toDirection, toCost) = (problem.getStartState(), [], 0)
    value = heuristic(state, problem)
    visitedList.append((state, value))
    direction[state] = []
    cost[state] = 0
    while not problem.isGoalState(state):
        successors = problem.getSuccessors(state)
        for child in successors:
            stateChild = child[0]
            ChildDirection = child[1]
            Childcost = child[2]
            visitedExist = False
            total_cost = toCost + Childcost
            for (existingState, existingCost) in visitedList:
                if (stateChild == existingState) and (total_cost >= existingCost):
                    visitedExist = True
                    break

            if not visitedExist:
                direction[stateChild] = direction[state] + [ChildDirection]
                cost[stateChild] = total_cost
                value = heuristic(stateChild, problem);
                queue.push(stateChild, value)
                visitedList.append((stateChild, value))

        state = queue.pop()
        toCost = cost[state]

    return direction[state]




# Abbreviations
astar = aStarSearch
gbfs = greedyBestFirstSearch
