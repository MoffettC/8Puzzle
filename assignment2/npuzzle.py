#Christopher Moffett and Margaret Lee 
#819886646               817587037

from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem

class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """
    def __init__(self, n, force_state=None, **kwargs):
        """"__init__(n, force_state, **kwargs)
        
        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.
        
        The parent's class constructor is then called with the TileBoard
        instance any any remaining arguments captured in **kwargs.
        """
        
        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments 
        # into a dictionary.  The dictionary can be accessed like any other 
        # dictionary, e.g. kwargs["keyname"], or passed to another function 
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).
        
        self.size = n
        self.tileBoard = TileBoard(self.size, False, force_state)
        super().__init__(self.tileBoard, **kwargs) #call parent class with tileboard?
          
        return
    
    def getInitialBoardState(self):
        return self.tileBoard.state_tuple()
    
    def generateDebugBoard(self, state):
        return TileBoard(self.size, False, state)

    def actions(self, state):
        "actions(state) - find a set of actions applicable to specified state"
        actionBoard = TileBoard(self.size, False, state) 
        actions = actionBoard.get_actions()
        return actions
    
    def result(self, state, action):
        "result(state, action)- apply action to state and return new state"
        actionBoard = TileBoard(self.size, False, state)
        newboard = actionBoard.move(action) 
        return newboard.state_tuple()
    
    def goal_test(self, state):
        "goal_test(state) - Is state a goal?"
        testBoard = TileBoard(self.size, False, state)
        if (testBoard.solved()):
            return True
        else:
            return False
