import matplotlib.pyplot as plt
import math
import numpy as np

ex1data = []
with open('machine-learning-ex1\ex1\ex1data2.txt') as f:
    content = f.read()
    ex1data_txt = content.split('\n')
for txt in ex1data_txt:
    co = txt.split(',')
    float_co = []
    for val in co:
        float_co.append(float(val))
    ex1data.append(float_co)

x = []
y = []
z = []
for co in ex1data:#plot datapoint
    x.append(co[0])
    y.append(co[1])
    z.append(co[2])
ax = plt.axes(projection='3d')
ax.scatter3D(x,y,z)

def MeanNormalize():
    feature1 = []
    feature2 = []
    for ex in ex1data:
        feature1.append(ex[0])
        feature2.append(ex[1])
    result = []
    for ex in ex1data:
        result.append([(ex[0]-(sum(feature1)/len(feature1)))/(max(feature1)-min(feature1)),\
                        (ex[1]-(sum(feature2)/len(feature2)))/(max(feature2)-min(feature2)),\
                        ex[2]])
    return result,feature1,feature2

def updatTheta(theta):
    newTheta = []
    for j,th in enumerate(theta):
        zigma = 0
        for ex in dataNorm:
            X = ex.copy()
            X.pop(-1)
            X.insert(0,1)
            H = 0
            for i,val in enumerate(X):     
                H += val*theta[i]
            zigma += (H-ex[-1])*X[j]
        newTheta.append(th-(alpha*(1/len(ex1data))*zigma))
    return newTheta

def cost(theta):
    zigma = 0
    for ex in dataNorm:
        X = ex.copy()
        X.pop(-1)
        X.insert(0,1)
        H = 0
        for i,val in enumerate(X):
            H += val*theta[i]
        zigma += (H-ex[-1])**2
    return zigma/(2*len(ex1data))

alpha = 0.1
theta = [1 for i in range(len(ex1data[0]))]
prev = math.inf
dataNorm,feature1,feature2 = MeanNormalize()
while cost(theta) < prev: #update theta until can n0t reduce the cost
    prev = cost(theta)
    theta = updatTheta(theta).copy()
print(theta)

xx,yy = np.meshgrid(x,y)
avg1 = sum(feature1)/len(feature1)
range1 = max(feature1)-min(feature1)
avg2 = sum(feature2)/len(feature2)
range2 = max(feature2)-min(feature2)
z_plane = []
for i in range(47):
    for j in range(47):
        z_plane.append(theta[0]+(theta[1]*((xx[i][j])-avg1)/range1)+(theta[2]*((yy[i][j]-avg2)/range2))) #result of normalize input
ax.plot_wireframe(xx,yy,np.array(z_plane).reshape(47,47),color='g') #result in green sur face (rotate graph with mouse to see)

#normal equation
X = []
Y = []
for ex in ex1data:
    x4 = ex.copy()
    x4.pop(-1)
    x4.insert(0,1)
    X.append(x4)
    Y.append([ex[-1]])
arrX = np.array(X)
arrY = np.array(Y)
arrXT = arrX.transpose()
H = np.linalg.inv(arrXT.dot(arrX)).dot(arrXT).dot(arrY)

xx,yy = np.meshgrid(x,y)
z_plane = []
for i in range(47):
    for j in range(47):
        z_plane.append(H[0][0]+(H[1][0]*xx[i][j])+(H[2][0]*yy[i][j]))
ax.plot_wireframe(xx,yy,np.array(z_plane).reshape(47,47),color='r') #result in red surface

ax.view_init(0,90)
plt.show()