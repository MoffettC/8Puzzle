#Christopher Moffett and Margaret Lee 
#819886646               817587037

'''
driver for graph search problem
Created on Feb 10, 2018

@author: mroch
'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies
import datetime

def tic():
    "Return current time representation"
    return time.time()

def tock(t):
    "Return time elapsed in sec since t where t is the output of tic()"
    return time.time() - t
    
def driver() :
    stepsList = []
    nodesList = []
    timeList = []
    
    i = 0
    trials = 1
    while i < trials:
        start = tic()
        puzzle = NPuzzle(8, g = Manhattan.g, h = Manhattan.h)
        (solution, nodesExpanded) = graph_search(puzzle, True, True)
    
        stepsList.append(solution.__len__())
        nodesList.append(nodesExpanded)
        timeList.append(tock(start))
        print("Trial ", i, " Complete")
        i += 1
    
    print("DFC")
    print("Mean Steps: ", mean(stepsList), " Std Dev Steps: ", stdev(stepsList))
    print("Mean Nodes Expanded: ", mean(nodesList), " Std Dev Nodes Expanded: ", stdev(nodesList))
    print("Mean Time: ", mean(timeList), " Std Dev Time: ", stdev(timeList))

    return

if __name__ == '__main__':
    driver()
