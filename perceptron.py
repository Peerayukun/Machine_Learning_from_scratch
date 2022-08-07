And_data = [
    [0,0,0],
    [0,1,0],
    [1,0,0],
    [1,1,1]
]


def updateW(o,x,W):
    newW = []
    for i,w in enumerate(W):
        if i == 0:
            newW.append(w+(alpha*(x[-1]-o)))
        else:
            newW.append(w+(alpha*(x[-1]-o)*x[i-1]))
    return newW

def badW(x,M):
    zigma = 0
    for i,w in enumerate(M):
        if i == 0:
            zigma += w
        else:
            zigma += w*x[i-1]
    if zigma <= 0:
        o = 0
    else:
        o = 1
    if o != x[-1]:
        return True, updateW(o,x,M)
    else:
        return False, M

W = [1,1,1]
alpha = 0.5
do = True
while do: 
    do = False
    for ex in And_data:
        bad,newW = badW(ex,W)
        if bad:
            W = newW.copy()
            do = True
            break
print(W)
#test result
for ex in And_data:
    zigma = 0
    for i,w in enumerate(W):
        if i == 0:
            zigma += w
        else:
            zigma += w*ex[i-1]
    if zigma <= 0:
        o = 0
    else:
        o = 1
    print('o:',o,'t:',ex[-1])

import matplotlib.pyplot as plt
for co in And_data: #plot datapoint
    if co[-1] == 0:
        plt.plot(co[0],co[1],'go') 
    else:
         plt.plot(co[0],co[1],'r+')
#plot perceptron
head = 0
tail = 1.25
yyh = (-W[0]-(W[1]*head))/W[2]
yyt = (-W[0]-(W[1]*tail))/W[2]
plt.plot([head,tail],[yyh,yyt])
plt.show()