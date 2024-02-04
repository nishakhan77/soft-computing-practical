import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
Y = np.array(([92], [86], [89]), dtype=float)
# scale units
X = X / np.amax(X, axis=0)
Y = Y / 100;


class NN(object):
    def __init__(self):
        self.inputsize = 2
        self.outputsize = 1
        self.hiddensize = 3

        self.W1 = np.random.randn(self.inputsize, self.hiddensize)
        self.W2 = np.random.randn(self.hiddensize, self.outputsize)

    def forward(self, X):
        self.z = np.dot(X, self.W1)  # Zinj=summation xiwij
        self.z2 = self.sigmoidal(self.z)  # zj=f(zinj)
        self.z3 = np.dot(self.z2, self.W2)  # yink= summation zjwjk
        op = self.sigmoidal(self.z3)  # yk=f(yink)
        return op;

    def sigmoidal(self, s):
        return 1 / (1 + np.exp(-s))


obj = NN()
op = obj.forward(X)
print("actual output" + str(op))
print("expected output" + str(Y))