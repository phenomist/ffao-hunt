import itertools
x = ["bikini","conics","insect","mildly","mystic","tecton","traces","waiter"]
diff = [(0,0),(1,0),(2,0),(2,1),(1,1),(0,1)]
diff2 = [(0,0),(0,2),(0,4),(0,6),(3,0),(3,2),(3,4),(3,6)]
badpairs = {chr(i)+chr(i) for i in range(ord('a'),ord('z')+1)}
badpairs.update({'ie','ei','dr','rd'})
countsol = 0

def pprint(x):
    for i in x:
        print(''.join(i))

for i in itertools.permutations(x):
    griddo = [['' for a in range(8)] for b in range(6)]
    for j in range(8):
        for m in range(6):
            griddo[diff[m][0]+diff2[j][0]][diff[m][1]+diff2[j][1]] = i[j][m]
    flag = True
    for x in range(7):
        for y in range(6):
            if griddo[y][x]+griddo[y][x+1] in badpairs:
                flag = False
    for x in range(8):
        for y in range(5):
            if griddo[y][x]+griddo[y+1][x] in badpairs:
                flag = False
    if flag:
        countsol += 1
    if countsol == 1:
        pprint(griddo)
print(countsol)
