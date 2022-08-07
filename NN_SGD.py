import math
import time
import random
Xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

# h0 = [random.normalvariate(0,1)*10 for i in range(3)]
# h1 = [random.normalvariate(0,1)*10 for i in range(3)]
# o = [random.normalvariate(0,1)*10 for i in range(3)]
h0 = [-2.8715866349921777, 0.48222026190470424, -7.842843152171863] 
h1 = [-7.080200949384262, 11.891369736646936, 4.456743433140631] 
o = [17.389839325924406, -6.2628462341499045, -1.4649681873225577]

def H(X):
    p0 = h0[0]
    for i,x in enumerate(X):
        if i < len(X)-1:
            p0 += h0[i+1]*x
    return 1/(1+math.e**(-p0))

def G(X):
    p1 = h1[0]
    for i,x in enumerate(X):
        if i < len(X)-1:
            p1 += h1[i+1]*x
    return 1/(1+math.e**(-p1))

def F(X):
    p2 = o[0]+(o[1]*H(X))+(o[2]*G(X))
    return 1/(1+math.e**(-p2))

def cost():
    zigma = 0
    for ex in Xor_data:
        if ex[-1] == 0:
            zigma += math.log(1-F(ex))
        else:
            zigma += math.log(F(ex))
    return (-zigma/len(Xor_data))

alpha = 0.1
do = True
while do:
    do =False
    for ex in Xor_data:
        output = F(ex)
        # if round(output) != ex[-1]:
        if (ex[-1]==1 and output<=0.9) or (ex[-1]==0 and output>=0.05) :
            do = True
            hH = H(ex)
            gG = G(ex)
            g = output-ex[-1]
            h = (output-ex[-1])*hH
            i = (output-ex[-1])*gG
            d = o[2]*gG*(1-gG)*(output-ex[-1])
            e = o[2]*gG*(1-gG)*(output-ex[-1])*ex[0]
            f = o[2]*gG*(1-gG)*(output-ex[-1])*ex[1]
            a = o[1]*hH*(1-hH)*(output-ex[-1])
            b = o[1]*hH*(1-hH)*(output-ex[-1])*ex[0]
            c = o[1]*hH*(1-hH)*(output-ex[-1])*ex[1]
            o[0] = o[0]-(alpha*g)
            o[1] = o[1]-(alpha*h)
            o[2] = o[2]-(alpha*i)
            h1[0] = h1[0]-(alpha*d)
            h1[1] = h1[1]-(alpha*e)
            h1[2] = h1[2]-(alpha*f)
            h0[0] = h0[0]-(alpha*a)
            h0[1] = h0[1]-(alpha*b)
            h0[2] = h0[2]-(alpha*c)
            # print(cost()) 
            break       

print(h0,h1,o)
for ex in Xor_data:
    print('taget:',ex[-1],'neural network o/p:',round(F(ex)),'approx('+str(F(ex)),")")
