
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv
from backtrack import backtracking_search
from csp_lib.backtrack_util import forward_checking

for puzzle in [easy1, harder1]:
    s  = Sudoku(puzzle)  # construct a Sudoku problem
    
    if puzzle == easy1:
        AC3(s) 
        s.display(s.infer_assignment())
    else:
        solved = backtracking_search(s, select_unassigned_variable=mrv, inference = forward_checking) is not None
    
    print("\n\n") #separate
