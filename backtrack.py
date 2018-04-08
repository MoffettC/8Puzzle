

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    
    # See Figure 6.5] of your book for details
    assignment = csp.curr_domains
    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        if csp.goal_test == True:
            return True;
        var = select_unassigned_variable(assignment, csp) 
        
        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                
                assignment.assign(var, value)
                inferences = inference(csp, var, value, assignment, csp.suppose(var, value))
                
                if inferences != False:
                    assignment.assign(var, value)
                    result = backtrack(assignment)
                    
                    if result != False:
                        return result
            assignment.prune(var, value)
    
        return False

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result

