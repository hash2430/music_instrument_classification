# input: test set, model
# output: performance sheet

#from NotRunnables import *
from NotRunnables import Path, Normalize

import numpy as np

class Test():
    dir = ""

    def __init__(self, dir):
        self.dir = dir

    def test(self, train_X_mean, train_X_std, model):
        # load test data
        test_mean_mfcc_file = Path.mean_mfcc_file(self.dir, Path.data[2])
        test_X = np.load(test_mean_mfcc_file)

        # normalize test data
        test_X = test_X.T
        test_X = Normalize.normalize(test_X, train_X_mean, train_X_std)

        # generate labels
        test_Y = Path.test_Y

        # apply model
        test_Y_hat = model.predict(test_X)

        # record accuracy
        file = Path.report(self.dir)
        file = open(file, 'a')
        test_data_size = test_Y_hat.shape[0]
        acc = np.sum((test_Y_hat == test_Y))/ test_data_size*100.0
        acc = "Test Accuracy: " + str(acc) + '%'
        file.write(acc)
        return acc