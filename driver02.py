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
    start = tic()
    print("Time Started ", datetime.datetime.now().time())
   
    puzzle = NPuzzle(8, g = BreadthFirst.g, h = BreadthFirst.h)
    (solution, nodesExpanded) = graph_search(puzzle, False, False)
    print(solution)
    print(nodesExpanded)
    
    print("Time Ended ", datetime.datetime.now().time())
    print("Time ", tock(start))
    return

if __name__ == '__main__':
    driver()
