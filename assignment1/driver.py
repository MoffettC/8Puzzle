from boardtypes import TileBoard

"Chris Moffett 819886646 CS550"

if __name__ == '__main__':
    #b = TileBoard(8)
    b = TileBoard(8, [1, 2, 3, 4, None, 5, 6, 7, 8])
    #d = TileBoard(8, [1, 2, 3, 4, None, 5, 6, 7, 8])
    #print(b.__eq__(d))
    solved = b.solved()
    
    while not solved:
        print(b)
        
        moves = b.get_actions()
        moveLabels = [(x) for x in range (len(moves))]
        
        for (label, move) in zip(moveLabels, moves):
            print("%s:%s " % (label, move))
            
        print("Enter Moves [Row, Col]:")        
        prompt = ""
        playerMove = input(prompt)       
        playerMove = int(playerMove)
        
        while playerMove not in moveLabels:
            if (prompt.isalnum()):
                playerMove = input(int(prompt))
                prompt = "No move, try again: "
                print(playerMove)
            
        b = b.move(moves[playerMove])
        
        solved = b.solved()
        
    if (solved):
        print(b)
        print("Puzzle solved!")
        print(b.state_tuple())