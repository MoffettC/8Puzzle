from basicsearch_lib.board import Board 
from random import *
from copy import deepcopy
from math import sqrt

"Chris Moffett 819886646 CS550"
class TileBoard(Board):

    def __init__(self, n, force_state=None):
        
        if (not sqrt(n+1).is_integer()):
            print("Input does not create a square board, please input correct size (IE: 8, 15, 24)")
            return
        
        self.isEven = False
        if (sqrt(n+1).is_integer() % 2 == 0):
            self.isEven = True            
        
        self.size = int(sqrt(n+1))
        super().__init__(self.size, self.size)

        self.n = n
        self.force_state = force_state
        self.currentPos = [0, 0]
        self.isSolvable = False;
        self.inversionNum = 0;
        
        self.build_list()
        self.check_solvable() 
        self.build_board()
        
        return
               
    def build_list(self):
        if (self.force_state == None):           
            self.numList = [None]             
            for x in range (1, self.n+1):
                self.numList.append(x)  #generate random number up to n in list              
            shuffle(self.numList)       #shuffle list

        else:
            self.numList = self.force_state
            self.isSolvable = True #assume player force state is solvable
        return

    def check_solvable(self):
        isEvenRowFound = False
        while not self.isSolvable:                      #check if puzzle is solvable
            for i in range(len(self.numList)):          
                if (self.numList[i] != None):           
                    for j in range(i+1, self.n+1):
                        if (self.numList[j] != None):
                            if (self.numList[i] > self.numList[j]): #compares each index with all indexes furth down in list (ignoring None value for both)
                                #print("%s > %s" % (self.numList[i], self.numList[j]))
                                self.inversionNum += 1  #if second value is less than it is inverted number
                        elif (not isEvenRowFound):
                            isEvenRowFound = True                 
                            self.evenRow = (j // self.size) + 1 #if puzzle is even, even row must be added to inversion number?
                            print("row is %s" % self.evenRow)
                            
            if (self.isEven):
                self.inversionNum += self.evenRow
                            
            print("Inversion number is: %s" % self.inversionNum)       
            if (self.inversionNum % 2 != 0):
                print("Puzzle not solvable, resuffling")
                isEvenRowFound = False
                shuffle(self.numList)
                self.inversionNum = 0;
            else:
                self.isSolvable = True
        return

    def build_board(self): 
        ctr = 0
        for row in range(0, Board.get_rows(self)):
            for col in range(0, Board.get_cols(self)):          
                Board.place(self, row, col, self.numList[ctr])
                if (self.numList[ctr] == None): #if null spot then save current player pos
                    self.currentPos[0] = row
                    self.currentPos[1] = col
                ctr+=1
                
    def __eq__(self, other_object):
        if isinstance(self, other_object.__class__):
            return self.board == other_object.board #compare obj repr for equality
        return False
    
    def state_tuple(self):
        flat_list = []
        for sublist in self.board:
            for item in sublist:
                flat_list.append(item) #append each sublist item into the tuple
        return tuple(flat_list)
    
    def get_actions(self):
        #create list of tuples as moves
        self.possMoves = []
        
        #iterate thru poss moves           
        if ((self.currentPos[0] - 1) >= 0): # UP
            self.possMoves.append([-1, 0])
        if ((self.currentPos[0] + 1) < Board.get_rows(self)): # DOWN
            self.possMoves.append([1, 0])
    
        if ((self.currentPos[1] - 1) >= 0): #LEFT
            self.possMoves.append([0, -1]) 
        if ((self.currentPos[1] + 1) < Board.get_cols(self)): #RIGHT
            self.possMoves.append([0, 1])

            
        return self.possMoves
    
    def move(self, offset):
        "create clone board"
        updated_board = deepcopy(self) 
        
        "get new position"
        newRow = offset[0] + self.currentPos[0]
        newCol = offset[1] + self.currentPos[1]
   
        "switch spots on board"
        temp = updated_board.get(newRow, newCol)
        updated_board.place(newRow, newCol, None)
        updated_board.place(self.currentPos[0], self.currentPos[1], temp)
        
        "update current pos"
        updated_board.currentPos[0] = newRow
        updated_board.currentPos[1] = newCol
        
        return updated_board
    
    def solved(self): #check if blank is in center of puzzle and all numbers are in order
        self.isSolved = True
        self.currList = self.state_tuple()
        self.currList = list(self.currList)
        
        for i in range(len(self.currList)):          
            if (self.currList[i] != None):           
                for j in range(i+1, self.n+1):
                    if (self.currList[j] != None):
                        if (self.currList[i] > self.currList[j]): 
                            self.isSolved = False 
        
        self.medianIndex = len(self.currList) // 2
        if (self.currList[self.medianIndex] != None):
            self.isSolved = False
        
        return self.isSolved

