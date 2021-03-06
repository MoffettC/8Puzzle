
"""
ai - search & strategy module
implement a concrete Strategy class and AlphaBetaSearch
"""
#Christopher Moffett and Margaret Lee 
#819886646               817587037
import abstractstrategy
from checkerboard import CheckerBoard

class Strategy(abstractstrategy.Strategy):
    def __init__(self, player, game, maxplies):
        """"Initialize a strategy
        player is the player represented by this strategy
        game is a class or instance that supports the class or instance method
            game.other_player(player) which finds the name 
                of the other player
        maxplies is the maximum number of plies before a cutoff is applied
        """
        
        # Useful for initializing any constant values or structures
        # used to evaluate the utility of a board
        self.maxplayer = player
        self.minplayer = game.other_player(player)
        self.maxplies = maxplies
        self.curGame = game
    
    def utility(self, board):
        "Return the utility of the specified board"
        val = 0
        
        boardTuple = board
        rowCtr = 0
        for row in boardTuple:
            col = 0;
            for piece in row:
                if CheckerBoard.isplayer(self.maxplayer, piece):
                    val += 1
                    if  CheckerBoard.isking(piece): #if a king 
                        val += 2
                    if (row == 3 & col == 4) | (row == 4 & col == 3): #if player has control of center
                        val += 3
                    val += board.disttoking(self.maxplayer, rowCtr) #if player closer to king row
                    
                if CheckerBoard.isplayer(self.minplayer, piece): #same heuristics but for other player
                    val -= 1
                    if  CheckerBoard.isking(piece):
                        val -= 2
                    if (row == 3 & col == 4) | (row == 4 & col == 3):
                        val -= 3 
                    val += board.disttoking(self.minplayer, rowCtr)                     
                col += 1 
            rowCtr += 1
        return val
    
    def play(self, board):
        """"play - Make a move
        Given a board, return (newboard, action) where newboard is
        the result of having applied action to board and action is
        determined via a game tree search (e.g. minimax with alpha-beta
        pruning).
        """
        search = AlphaBetaSearch(self, self.maxplayer, self.minplayer, self.maxplies)
        bestMove = search.alphabeta(board)
        newboard = board.move(bestMove) #apply bestMove to a clone of board
        
        return (newboard, bestMove)

class AlphaBetaSearch:
    """AlphaBetaSearch
    Conduct alpha beta searches from a given state.
    Example usage:
    # Given an instance of a class derived from AbstractStrategy, set up class
    # to determine next move, maximizing utility with respect to red player 
    # and minimiizing 
    with respect to black player.  Search 3 plies.
    search = AlphaBetaSearch(strategy, 'r', 'b', 3)
    # To find the move, run the alphabeta
     method
    best_move = search.alphabeta(some_checker_board)
    """
    def __init__(self, strategy, maxplayer, minplayer, maxplies=3, verbose=False): 
        """"AlphaBetaSearch 
        Initialize a class capable of alphabeta search strategy - implementation of AbstractStrategy class
        maxplayer - name of player that will maximize the utility function
        minplayer - name of player that will minimize the utility function
        maxplies - Maximum ply depth to search
        verbose - Output debugging information
        """
        self.strategy = strategy
        self.maxP = maxplayer
        self.minP = minplayer
        self.plies = maxplies
        self.depthLvl = 0
        
    def alphabeta(self, state):
        """alphbeta (state) 
        - Run an alphabeta search from the current state.  Returns best action.
        """ 

        v = self.maxvalue(self.plies, state, alpha = float("-inf"), beta = float("inf"))
        actions =  state.get_actions(self.maxP) #maxplayer will always be the side that called it
        
        for a in actions: #find actions that would apply the best move from current state
            newboard = state.move(a)
            x = self.strategy.utility(newboard)
            if x >= v:
                return a
         
    # define other helper methods as needed   
    def maxvalue(self, depth, state, alpha, beta):
        self.depthLvl += 1
        isDone = CheckerBoard.is_terminal(state)
        
        if isDone[0]:
            v = self.strategy.utility(state) #if terminal state
            
        elif self.depthLvl >= depth: #if cutoff depth hit
            v = float('-inf')
            actions = state.get_actions(self.maxP) 
            for a in actions: #choose move at depth
                newboard = state.move(a)
                w = self.strategy.utility(newboard)
                v = max(v, w)

        else:                       #if neither, then continue searching
            v = float('-inf')
            actions = state.get_actions(self.maxP)
            for a in actions:
                newboard = state.move(a)
                v = max(v, self.minvalue(depth, newboard, alpha, beta))
                if v >= beta:
                    break
                else:
                    alpha = min(beta, v) 
        return v
    
    def minvalue(self, depth, state, alpha, beta):
        self.depthLvl += 1
        isDone = CheckerBoard.is_terminal(state)
        
        if isDone[0]:
            v = self.strategy.utility(state) #if terminal state
            
        elif self.depthLvl >= depth: #if cutoff depth hit
            v = float('inf')
            actions = state.get_actions(self.maxP) 
            for a in actions:   #choose move at depth
                newboard = state.move(a)
                w = self.strategy.utility(newboard)
                v = min(v, w)

        else:                       #if neither, then keep searching
            v  = float("inf")
            actions = state.get_actions(self.minP)
            for a in actions:
                newboard = state.move(a)
                v = min(v, self.maxvalue(depth, newboard, alpha, beta))
                if v <= alpha:
                    break
                else:
                    beta = max(alpha, v) 
        return v
