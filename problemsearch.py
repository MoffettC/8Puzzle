'''
Created on Feb 10, 2018

@author: mroch
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue , FIFOQueue
from explored import Explored
import time
        
def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """
    
    
    
    frontierNodes = PriorityQueue(min, Node.get_f)
    node = Node(problem, problem.getInitialBoardState())
    nodesExplored = 0
    
    exploredStates = Explored() #hash table to store states
    exploredStates.add(node)
     
    for node in node.expand(problem):
        if not exploredStates.exists(node): #its not a duplicate in explored
            frontierNodes.append(node) #get initial frontier nodes
        
    done = found = False
    
    while not done:
        node = frontierNodes.pop() #loop thru frontier states
        nodesExplored += 1
        exploredStates.add(node)
        
        if problem.goal_test(node.state): #if found, set true
            found = done = True

        else:                       #if not, then add the new frontier states to the queue
            for node in node.expand(problem):
                if not exploredStates.exists(node): #its not a duplicate in explored
                    #if not frontierNodes.__contains__(node): #not a duplicate in frontier, slow!
                    frontierNodes.append(node)

            if (frontierNodes.__len__ == 0): #if we run thru all frontier, search complete
                done = True
                
    if found:
        if (verbose):
            print("Moves to solution: ", node.path().__len__())
            print("Nodes Expanded: ", nodesExplored)
            
            move = 0
            solutionList = node.solution() 
            boardList = []
                
            for node in node.path():
                boardList.append(problem.generateDebugBoard(node.state))
                
            print("Initial State")    
            for board in boardList:
                counter = move + 1
                print(board)
                print()
                if (move < boardList.__len__()-1):
                    print("Move ", counter, " ", solutionList[move])
                move += 1            
        
        if (debug):
            print()
            print("Debug Info:")
            print(print_nodes(node.path()))
            print()
            
        return (node.solution(), nodesExplored) #returns solution node's path/solution
    else:
        if (verbose | debug):
            print("No solution found")
        return ("No solution found", nodesExplored)     

