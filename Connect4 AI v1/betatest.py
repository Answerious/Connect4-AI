import computer1
import computer2
import math
import time
import qtable
import mapoints
import numed
import json

"""
BETA TEST OF THE QTABLE ALG
"""

class user():
    def __init__(self):
        self.start1 = computer1.val()
        self.start2 = computer2.val()

    def train_init(self):
        self.a = qtable.train(self.start1)
        self.b = qtable.train(self.start2)
        self.check1 = qtable.sepr(self.a)
        self.check2 = qtable.sepr(self.b)
        self.new1 = numed.short(self.check1)
        self.new2 = numed.short(self.check2)

    def run(self):
        self.train_init()
        total = {
                1:0,
                2:0,
                3:0,
                4:0,
                5:0
            }
        for i in range(25):
            self.start1 = self.new1
            self.start2 = self.new2
            self.train_init()
            total[self.new1] += 1
            total[self.new2] += 1
        print(json.dumps(total, indent=5))
            #print(f"RUN: {self.start1} {self.start2}")
            #print(f"UPDATED: {self.new1} {self.new2}")


if __name__=="__main__":
    user = user()
    user.run()