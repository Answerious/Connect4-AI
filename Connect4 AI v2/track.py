#Made by Jake Leroux 2021-2020(c);
#Algorithm made by Jake Leroux { JADAL };
import json
import sys
import aialgo
import time
wins = {
    'CPU1':0,
    'CPU2':0
}

class object():
    def __init__(self):
        self.a = 0
    def apply(self):
        print("Object has ran")
        self.data = aialgo.getdata()
        print(self.data)
    def limit(self):
        self.winner = 'CPU1'
        self.data = {
            1:5,
            2:5,
            3:5,
            4:5,
            5:5
        }
        self.turns = 0
        self.start = time.perf_counter()
        self.board = [['X' for i in range(5)] for row in range(5)]
        for i in range(20):
            self.turns += 1
            self.row = aialgo.selective()
            self.data[self.row] -= 1
            if self.turns%2 != 0:
                self.board[self.data[self.row]][self.row-1] = "H"
                a=0
                for row in self.board:
                    rowString = ''.join(row)
                    if rowString.count("HHH") >= 1:
                        self.winner = 'CPU1'
                        break
            if self.turns%2==0:
                self.board[self.data[self.row]][self.row-1] = "Y"
                b = 0
                for row in self.board:
                    rowStringb = ''.join(row)
                    if rowStringb.count("YYY") >= 1:
                        self.winner = 'CPU2'
                        break
        self.end = time.perf_counter()
        wins[self.winner] += 1
    def check(self):
        pass
        """
        for col in range(len(self.board[0])):
            colString = []
            for row in self.board:
                colString = colString.append(row[col])
                if colString.count('HHH') > 2:
                    print("CPU1 WIN") 
                if colString.count('YYY') > 2:
                    print ("CPU2 WIN")
            """
    def active(self):
        print ('   ' + '   '.join(map(str, range(1, 6))))
        print ('\n'.join('{0}: '.format(i+1) + ' | '.join(row) for i, row in enumerate(self.board)))
        print(json.dumps(wins, indent=2))
        print(f"TIME SPENT SIMULATING: {self.end-self.start:0.4f}s")

if __name__=="__main__":
    object = object()
    #AVG running time for my i7 16gb MacBook pro is 4.2s per game so if you want more or less 
    for n in range(50): # CHANGE THIS ONE TO THE NUMBER OF GAMES YOU WANT I WOULDN'T CHANGE IT THO
        for i in range(1):
            object.limit()
            object.active()