'''
Created on Apr 15, 2018

@author: mroch
'''

from ml_lib.learning import (DataSet, 
                             DecisionTreeLearner, NeuralNetLearner)
from std_cv import cross_validation
import random
from copy import deepcopy
    
def learn(dataset):
    
    random.shuffle(dataset.examples)

    dataList = cross_validation(DecisionTreeLearner, dataset)
    print("")
    print("Decision Tree: " + dataset.name)
    print("Mean: %.3f" % (dataList[0]))
    print("StdDv: %.3f" % dataList[1]) 
    formattedList = ['%.3f' % e for e in dataList[2]]
    print("Fold Errors: ", formattedList)  
    
    if (dataset.name != "orings"):
        dataset.attributes_to_numbers()
    dataList = cross_validation(NeuralNetLearner, dataset)
    print("")
    print("Neural Net: " + dataset.name)
    print("Mean: %.3f" % (dataList[0]))
    print("StdDv: %.3f" % dataList[1]) 
    formattedList = ['%.3f' % e for e in dataList[2]]
    print("Fold Errors: ", formattedList)  

def main():
    dset = DataSet(name = "iris")
    learn(dset)
    
    dset = DataSet(name = "orings")
    #learn(dset)
    
    dset = DataSet(name = "restaurant")
    learn(dset)
    
    dset = DataSet(name = "zoo")
    learn(dset)
    
    dset = DataSet(name = "abalone")
    learn(dset)
    
if __name__ == '__main__':
    main()
