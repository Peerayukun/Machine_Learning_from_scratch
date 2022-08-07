import matplotlib.pyplot as plt
import math

ex2data = []
with open('machine-learning-ex2\ex2\ex2data1.txt') as f:
    content = f.read()
    ex2data_txt = content.split('\n')
for txt in ex2data_txt:
    co = txt.split(',')
    float_co = []
    for val in co:
        float_co.append(float(val))
    ex2data.append(float_co)

def MeanNormalize():
    feature1 = []
    feature2 = []
    for ex in ex2data:
        feature1.append(ex[0])
        feature2.append(ex[1])
    result = []
    for ex in ex2data:
        result.append([(ex[0]-(sum(feature1)/len(feature1)))/(max(feature1)-min(feature1)),\
                        (ex[1]-(sum(feature2)/len(feature2)))/(max(feature2)-min(feature2)),\
                        ex[2]])
    return result,feature1,feature2


def H(x):
    Hx = 0
    for i,th in enumerate(theta):
        if i == 0:
            Hx += th
        else:
            Hx += th*x[i-1]
    return 1/(1+math.e**(-1*Hx))

def cost():
    zigma = 0
    for ex in dataNorm:
        if ex[-1] == 1:
            zigma += math.log(H(ex))
        else:
            zigma += math.log(1-H(ex))
    return (-1*zigma)/len(ex2data)

def updateTheta():
    newTheta = []
    for i,th in enumerate(theta):
        zigma = 0
        for ex in dataNorm:
            if i == 0:
                zigma += (H(ex)-ex[-1])
            else:
                zigma += (H(ex)-ex[-1])*ex[i-1]
        newTheta.append(th-(alpha*zigma))
    return newTheta

dataNorm,f1,f2 = MeanNormalize()
alpha = 0.1
theta = [1 for i in range(len(ex2data[0]))]
prev = math.inf
while cost() < prev:
    prev = cost()
    theta = updateTheta().copy()

for co in ex2data: #plot datapoint
    if co[-1] == 0:
        plt.plot(co[0],co[1],'go') 
    else:
         plt.plot(co[0],co[1],'r+')
#plot linear
head = 100
tail = 0
for ex in dataNorm: #find head and tail x of linear
    if ex[0] > tail:
        tail = ex[0]
    if ex[0] < head:
        head = ex[0]
#find head and tail y of linear(find x2 from Theta0+x0theta1+x2theta2 = 0) and convert to value before normalize
yyh = (((-theta[0]-(theta[1]*head))/theta[2])*(max(f2)-min(f2)))+(sum(f2)/len(f2))
yyt = (((-theta[0]-(theta[1]*tail))/theta[2])*(max(f2)-min(f2)))+(sum(f2)/len(f2))
#convert head and tail to value before normalize
head = (head*(max(f1)-min(f1)))+(sum(f1)/len(f1))
tail = (tail*(max(f1)-min(f1)))+(sum(f1)/len(f1))
plt.plot([head,tail],[yyh,yyt])

plt.show()
