'''
Constraint propagation
'''

def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    
    """   
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    cps.neighbors[x] is the neighbors of variable x
    
    done = False
    
    while not done:
        
        for v in csp.variables:                     #initial pruning based off of given numbers
            if 1 == len(csp.curr_domains[v]):       #if location has 1 domain (initial value already set)
                val = csp.curr_domains[v][0]   
                
                for x in csp.neighbors[v]:          #go thru neighbors of already set domain
                    if val in csp.curr_domains[x]:  #if neighbors have number in domain
                        csp.prune(x, val, None)     #removes that number from domain
        
        done = True                
        for v in csp.variables:
            if 1 != len(csp.curr_domains[v]): #repeat AC3 until finished, works only on easy
                done = False
