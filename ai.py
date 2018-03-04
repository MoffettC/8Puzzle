
"""
ai - search & strategy module
implement a concrete Strategy class and AlphaBetaSearch
"""
import abstractstrategy

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
        redVal = 0
        blackVal = 0
        redPieces =  self.curGame.piece_types('r')
        blackPieces =  self.curGame.piece_types('b')
        
        for piece in redPieces:
            if  self.curGame.isking(piece):
                redVal += 2
                
        for piece in blackPieces:
            if  self.curGame.isking(piece):
                blackVal += 2
        
        return (redVal, blackVal)
    
    def play(self, board):
        """"play - Make a move
        Given a board, return (newboard, action) where newboard is
        the result of having applied action to board and action is
        determined via a game tree search (e.g. minimax with alpha-beta
        pruning).
        """
        
        raise NotImplementedError("Subclass must implement")

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
    def alphabeta(self, state):
        """alphbeta (state) 
        - Run an alphabeta search from the current state.  Returns best action.
        """ 
    # define other helper methods as needed
    
    
    
    