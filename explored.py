#Christopher Moffett and Margaret Lee 
#819886646               817587037

'''
Created on Feb 8, 2018

@author: mroch
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        self.exploredSet = []
        self.size = 100000 #buckets
        i = 0
        while i < self.size:
            self.exploredSet.append([])
            i=i+1

        return
        
    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        key = hash(state) % self.size
        bucket = self.exploredSet[key]
        for exploredState in bucket:
            if exploredState == state:
                return True
        
        return False

    
    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        key = hash(state) % self.size
        self.exploredSet[key].append(state) #add as long as its not a duplicate
        
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError

        return
            
