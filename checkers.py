'''
Created on Feb 22, 2015

@author: mroch
'''

import time
import datetime

import checkerboard
# tonto - Professor Roch's not too smart strategy
# You are not given source code to this, but compiled .pyc files
# are available for Python 3.5 and 3.6 (fails otherwise).
# This will let you test some of your game logic without having to worry
# about whether or not your AI is working and let you pit your player
# against another computer player.
#
# Decompilation is cheating, don't do it.
import tonto

# human - human player, prompts for input    
import human
import ai
import boardlibrary # might be useful for debugging

def elapsed(earlier, later):
    """elapsed - Convert elapsed time.time objects to duration string
    
    Useful for tracking move and game time.  Example pseudocode:
    
    gamestart = time.time()
    
    while game not over:
        movestart = time.time()
        ...  logic ...
        current = time.time() 
        print("Move time: {} Game time: {}".format(
            elapsed(movestart, current), elapsed(gamestart, current))
    
    
    """
    return time.strftime('%H:%M:%S', time.gmtime(later - earlier))
           

def Game(red=human.Strategy, black=ai.Strategy, 
         maxplies=5, init=None, verbose=True, firstmove=0):
    """Game(red, black, maxplies, init, verbose, turn)
    Start a game of checkers
    red,black - Strategy classes (not instances)
    maxplies - # of turns to explore (default 10)
    init - Start with given board (default None uses a brand new game)
    verbose - Show messages (default True)
    firstmove - Player N starts 0 (red) or 1 (black).  Default 0. 
    """

    # Don't forget to create instances of your strategy,
    # e.g. black('b', checkerboard.CheckerBoard, maxplies)
    
    checkerGame = checkerboard.CheckerBoard()
    
    redplayer = red('r', checkerGame, maxplies)
    blackplayer = black('b', checkerGame, maxplies)

    results = redplayer.play(checkerGame) #initial move
    checkerGame = results[0]
    won = False
    
    while (not won): #repeat player moves until won
        x = checkerGame.is_terminal()
        won = x[0]

        results = blackplayer.play(checkerGame)
        checkerGame = results[0]
        x = checkerGame.is_terminal()
        won = x[0]
        if won:
            break
        
        results = redplayer.play(checkerGame)
        checkerGame = results[0]
        x = checkerGame.is_terminal()
        won = x[0]
    
    print("Finished")
    return


if __name__ == "__main__":
    Game()  
        
        
        


        
                    
            
        

    
    
