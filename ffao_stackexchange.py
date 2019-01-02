a = "31223"
b = "33311"
c = ord("1")+ord("2")+ord("3")
def tohdist(x, y):
    if x == y:
        return 0
    if x[-1] == y[-1]:
        return tohdist(x[:-1],y[:-1])
    else:
        return 1+tohdist(x[:-1],chr(c-ord(x[-1])-ord(y[-1]))*(len(x)-1))+tohdist(y[:-1],chr(c-ord(x[-1])-ord(y[-1]))*(len(x)-1))

print(tohdist(a,b))

#OINKED
