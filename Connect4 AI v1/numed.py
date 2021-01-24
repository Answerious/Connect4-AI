"""
SHORTENS QTABLE TO ONE NUMBER VALUE
"""
import random
no = random.randint(1,3)
def short(a):
    base = a[1:6]
    q = 0
    du = []
    for i in base:
        q += 1
        x = (i, (q))
        du.append(tuple(x))
    cal = max(du)
    row = cal[1:]
    clear = str(row)
    z = clear.replace("(","")
    c = z.replace(")","")
    z = c.replace(",","")
    row = int(z)

    return row