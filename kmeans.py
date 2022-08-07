import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.datasets._samples_generator import make_blobs
from sklearn.datasets._samples_generator import make_moons
import random
import math
n_node = int(input('number of node: '))
k = int(input('number of cluster: '))
fig, ax = plt.subplots()

def gennode():
    xloc_list = []
    yloc_list = []
    # X, l = make_circles(n_samples=n_node, noise=0.1, factor=.2)
    X, l = make_blobs(n_samples=n_node, centers=k, cluster_std=1, n_features=2)
    # X, l = make_moons(n_samples=n_node, noise=0.1)
    xloc_list = X[:,0].tolist()
    yloc_list = X[:,1].tolist()
    # for a in range(n_node):
    #     xloc = random.randint(0,x_range)
    #     xloc_list.append(xloc)
    #     yloc = random.randint(0,y_range)
    #     yloc_list.append(yloc)
    return(xloc_list,yloc_list)

def finddis(a,b):
    return (((a[0]-xloc_list[b])**2)+((a[1]-yloc_list[b])**2))**(1/2)

def redo():
    if prev == 0:
        return True
    else:
        # print([len(prev[i]) for i in range(k)])
        # print([len(Cluster[i]) for i in range(k)])
        for i in range(k):
            if len(Cluster[i]) != len(prev[i]):
                return True
            else:
                for j in prev[i]:
                    if j not in Cluster[i]:
                        return True
        return False

def updateCentroid():
    for i in range(k):
        xx = []
        yy =[]
        for n in Cluster[i]:
            xx.append(xloc_list[n])
            yy.append(yloc_list[n])
        # the problem is the situation that the cluser is empty because no point close to it, then len(xx) = 0
        centroid[i] = (round(sum(xx)/len(xx),2),round(sum(yy)/len(yy),2))

def mostfar(c):
    for i in range(n_node):
        far[i].append(finddis(c,i))
    AVG = [sum(i)/len(i) for i in far]
    idx =  AVG.index(max(AVG))
    return (xloc_list[idx],yloc_list[idx])

xloc_list, yloc_list = gennode()
r = random.randint(0,n_node-1)
centroid = [(xloc_list[r],yloc_list[r])]
far = [[] for i in range(n_node)]
for i in range(k-1):
    x = mostfar(centroid[i])
    centroid.append(x)
print(centroid)
n_dis = [math.inf for i in range(n_node)]
prev = [0 for i in range(k)]
count = 0
while sum([prev[i]==centroid[i] for i in range(k)]) != k or count == 0:
    Cluster = [[] for i in range(k)]
    prev = centroid.copy()
    for n in range(n_node):
        for i,c in enumerate(centroid):
            n_to_c = finddis(c,n)
            if n_to_c < n_dis[n]:
                close_to = i
                n_dis[n] = n_to_c
        Cluster[close_to].append(n)
        n_dis[n] = math.inf
    updateCentroid()
    count += 1

print(count)
color = ['red','green','blue','orange','pink','purple','black']
for i,C in enumerate(Cluster):
    xplot = [xloc_list[j] for j in C]
    yplot = [yloc_list[j] for j in C]
    ax.scatter(xplot,yplot,c = color[i])
plt.show()