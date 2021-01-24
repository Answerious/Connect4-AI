#Made by Jake Leroux 2021-2022(c);
#Algorithm made by Jake Leroux { JADAL };
import json
import math
import random
import re
import sys
import numpy
from numpy import array, dot, exp
from numpy import random as rn
from numpy import reshape

data = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0
}

class qtable():
    def __init__(self):
        self.new = []
        self.object = []
        self.call = []
        self.layer = rn.random((5,5))
        self.new.append(self.layer)
        self.val = data
    def operation(self):
        a = [str(d) for d in str(self.new)] #(sep='\n')
        x = [x.strip(' ') for x in a]
        z = [ i for i in x if i.isdigit() ]
        c = [z[i:i + 25] for i in range(0, len(z), 25)]
        a = c[1:(len(c)%2)+1]
        b = [str(d) for d in str(a)]
        z = [ i for i in b if i.isdigit() ]
        chunks = [z[x:x+5] for x in range(0, len(z), 5)]
        base = chunks[4:]
        for n in base:
            x = (n)
            self.cal = max(x)
        for position,char in enumerate(x):
            if char==self.cal:
                self.row = (position+1)
        data[self.row] += 1
    def __sigmoid_der(self, x):
        return x * (1-x)
    def __sigmoid(self, x):
        return 1/ (1 + exp(-x))
    def __sigmoid_up(self, x):
        return x / (1-x)
    def training(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for interation in range(number_of_training_iterations):
            output = self.think(training_set_inputs)
            error = training_set_outputs-output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_der(output))
            self.layer += adjustment
    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.layer))
    def active(self):
        number_of_training_iterations = 400
        training_set_inputs = array([[0,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[0,0,1,1,1],[1,1,0,0,0]])
        training_set_outputs = array([0+1+1+0+1])
        self.training(training_set_inputs, training_set_outputs, number_of_training_iterations)
        self.new = []
        self.new.append(self.layer)
        self.operation()
    def stats(self):
        self.operation()
        for i in range(25):
            self.active()
        self.val = (json.dumps(data, indent=5))
        self.dump = self.row

def getdata():
    qtable1 = qtable()
    qtable1.stats()
    return qtable1.val

def selective():
    qtable1 = qtable()
    qtable1.stats()
    return qtable1.dump