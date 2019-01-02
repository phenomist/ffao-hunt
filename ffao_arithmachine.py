from num2words import num2words as word

def g(x):
    if x <= 7:
        return -1
    arr, n = [], 2
    while len(arr) < x-7:
        flag = True
        for i in arr:
            if n%i == 0:
                flag = False
        if flag:
            arr.append(n)
        n += 1
    return arr[-1]

def h(x):
    return 9**(x/9)

def i(x):
    w = word(x).replace('-','').replace(' ','')
    scorearray = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
    tot = 0
    for c in w:
        tot += scorearray[ord(c)-ord('a')]
    return tot

def j(x):
    return len(word(x).replace('-','').replace(' ',''))

def k(x):
    return 4*(3/4*x)**0.5

def l(x):
    a = 'A'+str(x**2).replace('0','A')
    return int(''.join(sorted(a[-2:])).replace('A','0'))

def resort(a):
    a = sorted(a)
    order = [3,1,4,2,0,5]
    ret = []
    for i in range(6):
        ret.append(a[order[i]])
    return ret

f = lambda x: [g(x),h(x),i(x),j(x),k(x),l(x)]
msg = "FINDEACHFUNCTIONSFIX"
cc = 27
for ch in msg:
    print(">>> f("+str(cc)+")")
    print(f(cc))
    cc += ord(ch)-ord('A')+1
print(f(237))

for cc in range(1,27):
    for dd in range(6):
        try:
            if f(cc)[dd] == cc:
                print(cc,dd)
        except:
            pass

