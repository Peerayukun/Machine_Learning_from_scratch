import matplotlib.pyplot as plt
import math
ex1data = []
with open('machine-learning-ex1\ex1\ex1data1.txt') as f:
    content = f.read()
    ex1data_txt = content.split('\n')
for txt in ex1data_txt:
    co = txt.split(',')
    float_co = []
    for val in co:
        float_co.append(float(val))
    ex1data.append(float_co)

for co in ex1data:
    plt.plot(co[0],co[1],'rx') #plot datapoint

def updatTheta0(theta0,theta1):
    zigma = 0
    for ex in ex1data:
        zigma += (theta0+(theta1*ex[0]))-ex[1]
    return theta0-(alpha*(1/len(ex1data))*zigma)

def updatTheta1(theta0,theta1):
    zigma = 0
    for ex in ex1data:
        zigma += ((theta0+(theta1*ex[0]))-ex[1])*ex[0]
    return theta1-(alpha*(1/len(ex1data))*zigma)

def cost(theta0,theta1):
    zigma = 0
    for ex in ex1data:
        zigma += ((theta0+(theta1*ex[0]))-ex[1])**2
    return zigma/(2*len(ex1data))

alpha = 0.01
theta0 = 1
theta1 = 1
prev = math.inf
while cost(theta0,theta1) < prev: #update theta until can n0t reduce the cost
    prev = cost(theta0,theta1)
    print(prev)
    new0 = updatTheta0(theta0,theta1)
    new1 = updatTheta1(theta0,theta1)
    theta0 = new0
    theta1 = new1

head = 100
tail = 0
for ex in ex1data: #find head and tail of linear
    if ex[0] > tail:
        tail = ex[0]
    if ex[0] < head:
        head = ex[0]

plt.plot([head,tail],[theta0+theta1*head,theta0+theta1*tail])
plt.show()