import computer1
import computer2
import math
import time
import qtable
import mapoints

class draw():
    def __init__(self):
        self.board_1 = """
        (21) (22) (23) (24) (25)
        (16) (17) (18) (19) (20)
        (11) (12) (13) (14) (15)
        (6) (7) (8) (9) (10)
        (1) (2) (3) (4) (5)
        """
        self.val = computer1.val()
        self.check = str(self.val)
        mapoints.info(self.val)
        self.val2 = computer2.val()
        self.check2 = str(self.val2)
        mapoints.info(self.val2)
    def run(self):
        self.update = str(self.board_1)
        self.a = self.update.replace("("+self.check+")", "(Q)")
        self.b = ""
        if self.check == self.check2:
            computer2.first_act().redo()
        else:
            self.b = self.a.replace("("+self.check2+")", "(Z)")
        
    
    def con(self):
        print("FIRST MOVE Q, Z = PLACED")
        print(self.b)
        self.cpm1 = (self.val)
        self.cpm2 = (self.val2)
        #print(self.upt)
        self.redo()
        #self.onemore()
        self.final()

    def redo(self):
        self.upt = qtable.train(self.cpm1)
        self.upt2 = qtable.train(self.cpm2)
        self.base = self.upt
        self.org = qtable.sepr(self.base)
        self.mar = self.org[1:6]
        self.du = []
        self.cpm1_lv = 0
        self.cpm2_lv = 0
        self.check_2 = 0
        self.check_21 = 0
        self.check_22 = 0
        q = 0
        for i in self.mar:
            q += 1
            x = (i, (q))
            self.du.append(tuple(x))
        self.cal = max(self.du)
        self.row = self.cal[1:]
        self.clear = str(self.row)
        a = self.clear.replace("(","")
        b = a.replace(")","")
        self.clear = b.replace(",","")
        self.row = int(self.clear)
        self.check_1 = int(self.row)
        print(self.check_1)
        mapoints.info(self.check_1)
        if self.check_1 == self.cpm1:
            self.cpm1_lv += 1
            self.check_21 = (self.check_1 + (self.cpm1_lv*5))
            self.check_1 = str(self.check_21)
            self.a = self.b.replace("("+(self.check_1)+")", "(Q)")
            self.cpm1 = self.check_1
        if self.check_1 == self.check_2:
            self.cpm1_lv += 1
            self.check_21 = (self.check_1 + (self.cpm2_lv*5))
            self.check_1 = str(self.check_21)
            self.a = self.b.replace("("+(self.check_1)+")", "(Q)")
            self.cpm1 = self.check_1
        if self.check_1 == self.cpm2:
            self.cpm1_lv += 1
            self.check_21 = (self.check_1 + (self.cpm2_lv*5))
            self.check_1 = str(self.check_21)
            self.a = self.b.replace("("+(self.check_1)+")", "(Q)")
            self.cpm1 = self.check_1
        else:
            self.check_21 = str(self.check_1)
            self.a = self.b.replace("("+(self.check_21)+")", "(Q)")
            self.cpm1 = self.check_21

        self.base = self.upt2
        self.org = qtable.sepr(self.base)
        self.mar = self.org[1:6]
        self.du = []
        q = 0
        for i in self.mar:
            q += 1
            x = (i, (q))
            self.du.append(tuple(x))
        self.cal = max(self.du)
        self.row = self.cal[1:]
        self.clear = str(self.row)
        a = self.clear.replace("(","")
        b = a.replace(")","")
        self.clear = b.replace(",","")
        self.row = int(self.clear)
        self.check_2 = int(self.row)
        print(self.check_2)
        if self.check_2 == self.cpm2:
            self.cpm2_lv += 1
            self.check_22 = (self.check_2 + (self.cpm2_lv*5))
            self.check_2 = str(self.check_22)
            self.b = self.a.replace("("+(self.check_2)+")", "(Z)")
            self.cpm2 = self.check_2
        if self.check_2 == self.check_1:
            self.cpm2_lv += 1
            self.check_22 = (self.check_2 + (self.cpm1_lv*5))
            self.check_2 = str(self.check_22)
            self.b = self.a.replace("("+(self.check_2)+")", "(Z)")
            self.cpm2 = self.check_2
        if self.check_2 == self.cpm1:
            self.cpm2_lv += 1
            self.check_22 = (self.check_2 + (self.cpm1_lv*5))
            self.check_2 = str(self.check_22)
            self.b = self.a.replace("("+(self.check_2)+")", "(Z)")
            self.cpm2 = self.check_2
        else:
            self.check_22 = str(self.check_2)
            self.b = self.a.replace("("+(self.check_22)+")", "(Z)")
            self.cpm2 = self.check_22

    def final(self):
        print(self.b)
    def onemore(self):
        self.redo()
        self.final()


if __name__=="__main__":
    draw = draw()
    draw.run()
    draw.con()
