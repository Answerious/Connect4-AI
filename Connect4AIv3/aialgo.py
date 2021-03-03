import numpy as np
from numpy import random as rn
from numpy import dot
from numpy import array
from numpy import exp
from numpy import reshape
import ctypes
from ctypes import *
import json

STORED = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0
}
    
def startsynaptic():
    file = ('matrixgen.so')
    open = ctypes.CDLL(file)
    a = open.main()
    b = open.main2()
    c = open.main3()
    START = ("{0} {1} {2}".format(a,b,c))
    return START

class table():
    def __init__(self):
        LAYER = startsynaptic()
        DATA = LAYER.split()
        ELEMENT = [int(d) for d in DATA]
        self.val = STORED
        self.DATA = []
        for i in ELEMENT:
            self.layer = rn.random((5,5)) +(i)
            self.DATA.append(self.layer)
    def operation(self):
        STEPA = [str(d) for d in str(self.DATA)]
        STEPB = [STEPB.strip('') for STEPB in STEPA]
        STEPC = [ i for i in STEPB if i.isdigit() ]
        STEPD = [STEPC[i:i + 25] for i in range(0, len(STEPC), 25)]
        STEPE = STEPD[0:1]
        STEPF = [str(d) for d in str(STEPE)]
        STEPG = [ i for i in STEPF if i.isdigit() ]
        CHUNKS = [STEPG[x:x + 5] for x in range(0, len(STEPG), 5)]
        BASE = CHUNKS[4:]
        for n in BASE:
            global x
            x = (n)
            self.cal = max(x)
        for position,char in enumerate(x):
            if char==self.cal:
                self.row = (position+1)
        STORED[self.row] += 1

    def __tanh(self, x):
        return (exp(x)-exp(-x))/(exp(x)+exp(-x))
    def __relu(self, x):
        return np.where(x>0,x,0)
    def __sigmoid(self, x):
        return 1/(1+exp(-x))
    def training(self, TRAINING_SET_INPUTS, TRAINING_SET_OUTPUTS, NUMBER_OF_TRAINING_ITERATIONS):
        for iteration in range(NUMBER_OF_TRAINING_ITERATIONS):
            OUTPUT = self.think(TRAINING_SET_INPUTS)
            ERROR = TRAINING_SET_OUTPUTS-OUTPUT
            ADJUSTMENT = dot(TRAINING_SET_INPUTS.T, ERROR * self.__tanh(OUTPUT))
            self.layer += ADJUSTMENT
    def think(self, INPUTS):
        return self.__sigmoid(dot(INPUTS, self.layer))
    def run(self):
        NUMBER_OF_TRAINING_ITERATIONS = 400
        TRAINING_SET_INPUTS = array([[0,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[0,0,1,1,1],[1,1,0,0,0]])
        TRAINING_SET_OUTPUTS = array([0+1+1+0+1])
        self.training(TRAINING_SET_INPUTS, TRAINING_SET_OUTPUTS, NUMBER_OF_TRAINING_ITERATIONS)
        self.DATA = []
        self.DATA.append(self.layer)
        self.operation()
    def stats(self):
        self.operation()
        for i in range(25):
            self.run()
        self.val = (json.dumps(STORED, indent=5))
        self.dump = self.row

    def show(self):
        self.stats()
        print(self.val)

def getdata():
    table1 = table()
    table1.stats()
    return table1.val

def selective():
    table1 = table()
    table1.stats()
    return table1.dump