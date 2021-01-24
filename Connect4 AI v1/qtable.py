"""
**CREATES QTABLES**

BY JAKE LEROUX

2020-2021(c)
"""
import numpy
from numpy import exp
from numpy import array
from numpy import random as rn
from numpy import dot
from numpy import reshape
import random
import math

class random_array():
    def __init__(self):
        """
        HARDCODED SIZE FOR NOW
        """
        self.x = 1
        self.i = 1
        self.size = 1
        self.q = ""
        self.change = random.randint(self.x,self.i)
        self.first_layer = rn.random((1,2)) -self.change * self.size
        self.change = random.randint(self.x,self.i)
        self.second_layer = rn.random((1,2)) -self.change * self.size
        self.change = random.randint(self.x,self.i)
        self.third_layer = rn.random((1,2)) -self.change * self.size
        self.change = random.randint(self.x,self.i)
        self.fourth_layer = rn.random((1,2)) -self.change * self.size
        self.change = random.randint(self.x,self.i)
        self.fifth_layer = rn.random((1,2)) -self.change * self.size
    def __sigmoid_der(self, x):
        return x * (1-x)
    def __sigmoid(self, x):
        return 1/ (1 + exp(-x))
    def __sigmoid_up(self, x):
        return x / (1-x)
    def start_qval(self):
        self.call1 = dot(self.first_layer.T, self.second_layer * self.__sigmoid_der(self.third_layer))
        self.check = dot(exp(self.fourth_layer.T, self.fifth_layer * self.__sigmoid(self.call1)), self.call1)
        self.update = self.__sigmoid_up(dot(self.call1.T, self.check))
        abs(self.update)
        self.q = self.update
        return self.q

def create():
    """
    creates random qtable

    []
    in 5x5 grid
    []
    """
    stat = random_array()
    stat.start_qval()
    return stat.update

def setval(x,i):
    """
    sets random generation value for qtable

    x to i

    x,i 
    """
    random_array().x = x
    random_array().i = i
def size(x):
    """
    reduces array len

    3 is recommended

    x
    """
    random_array().size = x
def sepr(x):
    """
    splits qtable into list

    [5,5] = {[5,1] * 5}
    """
    c = numpy.array(x).flatten().tolist()
    return c

def __sigmoid(x):
    return 1/ (1 + exp(-x))

def think(inputs, x):
    return __sigmoid(dot(inputs, x))

def __sigmoid_derivative(x):
    return x * (1 -x)

def train(x):
    """
    Trains/updates qtable

    qtable.train(x)
    """
    training_set_inputs = array([[0,1,1,0,0],[1,0,1,1,1],[1,0,1,0,1],[0,1,1,1,0],[1,1,0,0,0]])
    training_Set_outputs = array([[0+1+1+0+0]]).T
    number_of_training_iterations = 1

    for interation in range(number_of_training_iterations):
        output = think(training_set_inputs, x)
        error = training_Set_outputs - output
        adjustment = dot(training_set_inputs.T, error * __sigmoid_derivative(output))
        x += adjustment
        return x