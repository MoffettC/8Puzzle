
"""
ai - search & strategy module
implement a concrete Strategy class and AlphaBetaSearch
"""
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
        for row in boardTuple:
            col = 0;
            for piece in row:
                if CheckerBoard.isplayer(self.maxplayer, piece):
                    val += 1
                    if  CheckerBoard.isking(piece):
                        val += 2
                    if (row == 3 & col == 4) | (row == 4 & col == 3):
                        val += 3
                if CheckerBoard.isplayer(self.minplayer, piece):
                    val -= 1
                    if  CheckerBoard.isking(piece):
                        val -= 2
                    if (row == 3 & col == 4) | (row == 4 & col == 3):
                        val -= 3                      
                col += 1 
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
#         self.board = state
#         initialVal = self.strategy.utility(self.strategy, self.board) #eval board

        v = self.maxvalue(state, self.plies, alpha = float("-inf"), beta = float("inf"))
        actions =  self.strategy.curGame.get_actions(self.maxP) #maxplayer will always be the side that called it  
#         for a in actions:
#             if 
        return 
        
        #move down tree, eval child boards, one of these initial moves is a best action
        #repeat until hitting max plies, prune along the way
        #return best action
         
    # define other helper methods as needed   
    def maxvalue(self, depth, state, alpha, beta):
        self.depthLvl += 1
        isDone = CheckerBoard.is_terminal(self.strategy.curGame)
        if isDone[0]:
            v = self.strategy.utility(self.strategy.curGame.board)
        elif self.depthLvl == depth:
            return v    
        else:
            v = float('-inf')
            actions = self.strategy.curGame.get_actions(self.maxP)
            for a in actions:
                newboard = self.strategy.curGame.move(a)
                v = max(v, self.minvalue(newboard, depth, alpha, beta))
                if v >= beta:
                    break
                else:
                    alpha = beta(beta, v) 
        return v
    
    def minvalue(self, depth, state, alpha, beta):
        self.depthLvl += 1
        isDone = CheckerBoard.is_terminal(self.strategy.curGame)
        if isDone[0]:
            v = self.strategy.utility(self.strategy.curGame.board)
        elif self.depthLvl == depth:
            return v
        else:
            v  = float("inf")
            actions = self.strategy.curGame.get_actions(self.minP)
            for a in actions:
                newboard = self.strategy.curGame.move(a)
                v = min(v, self.maxvalue(newboard, depth, alpha, beta))
                if v <= alpha:
                    break
                else:
                    beta = alpha(alpha, v) 
        return v
