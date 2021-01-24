import qtable
import basegame
import sys

qtable.setval(1,-1)
qtable.size(2)

class first_act():
    def __init__(self):
        self.create = qtable.create()
        self.org = qtable.sepr(self.create)
        self.du = []
    def choice(self):
        self.base = self.org[1:6]
        q = 0
        for i in self.base:
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
    def redo(self):
        self.create = qtable.create()
        self.org = qtable.sepr(self.create)
        fn = first_act()
        fn.choice()
def val():
    fn = first_act()
    fn.choice()
    return fn.row

def info():
    fn = first_act()
    return fn.create