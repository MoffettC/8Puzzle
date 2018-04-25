
from statistics import (stdev, mean)
from ml_lib.learning import (err_ratio, train_and_test)
import random

def cross_validation(learner, dataset, k=10):
    """Perform k-fold cross_validation
    Run k trials where each trial has a different (k-1)/k percentage
    of the data as training data and 1/k as test data.
    
    Returns tuple (mean_err, std_err, fold_errors, models)
    """
    
    """Do k-fold cross_validate and return their mean.
    That is, keep out 1/k of the examples for testing on each of k runs.
    Shuffle the examples first; if trials>1, average over several shuffles.
    Returns Training error, Validation error"""
    
#     if k is None:
#         k = len(dataset.examples)

    foldData = []
    fold_errT = 0   # fold error on training data
    fold_errV = 0   # fold error on validation data
    
    n = len(dataset.examples)
    examples = dataset.examples
    
    for fold in range(k):   # for each fold
        # Shuffle all data            
        #random.shuffle(dataset.examples)
        
        # Split into train and test
        # Note that this is not a canonical cross validation where
        # every pieces of data is used for training and testing
        # due to the shuffling above.
        train_data, val_data = train_and_test(dataset, fold * (n / k),
                                              (fold + 1) * (n / k))
        
        dataset.examples = train_data
        h = learner(dataset)
        
        # predict and accumulate the error rate on 
        # the training and validation data
        fold_errT += err_ratio(h, dataset, train_data)
        fold_errV += err_ratio(h, dataset, val_data)
        
        foldData.append(err_ratio(h, dataset, val_data)) #validation error
        
        # Reverting back to original once test is completed
        dataset.examples = examples
        
    # Return average per fold rates
    return mean(foldData), stdev(foldData), foldData

