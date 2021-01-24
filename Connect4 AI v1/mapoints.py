import sys
class dataset():
    def __init__(self):
        self.col_1 = 0
        self.col_2 = 0
        self.col_3 = 0
        self.col_4 = 0
        self.col_5 = 0
        self.col_check = 0
    def action(self, x):
        if x == 1:
            self.col_1 += 1
        if x == 2:
            self.col_2 += 1
        if x == 3:
            self.col_3 += 1
        if x == 4:
            self.col_4 += 1
        if x == 5:
            self.col_5 += 1
        if x > 5:
            print("DATABASE TABLE 'action' COLUMN ERROR {0} | check number 1-5?".format(x))
            sys.exit()
        if x <= 0:
            print("DATABASE TABLE 'action' COLUMN ERROR {0} | check number 1-5?".format(x))
            sys.exit()
    def data1(self):
        self.du = (self.col_1, self.col_2, self.col_3, self.col_4, self.col_5)
        self.data = list(self.du)
        return self.data

dataset = dataset()
def info(x):
    dataset.first = x
    dataset.action(x)
    dataset.data1()
    return list(dataset.du)
def col(x, i):
    if i <= 0:
        print("ACTION ERROR {0} | check number 1-5?".format(i))
        sys.exit()
    if i > 5:
        print("ACTION ERROR {0} | check number 1-5?".format(i))
        sys.exit()
    b = x[i-1:]
    if i == 5:
        c = str(b)
        d = c.replace("[","")
        f = d.replace("]","")
        e = int(f)
        return e
    if i != 5:
        c = b[:i-5]
        d = str(c)
        f = d.replace("[","")
        e = f.replace("]","")
        g = int(e)
        return g