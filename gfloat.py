"""
Avoid problems with floats
created by mondlos: https://github.com/mondlos/MondlosPython
"""

def gFloat(num, p=2):
    return int(float(format(num, "."+str(p)+"f"))*10**p)

def addDecimal(num):
    d = str(num)
    return d[0]+"."+d[1:len(d)]
