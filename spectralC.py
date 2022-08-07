import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_circles
from sklearn.datasets._samples_generator import make_blobs
from sklearn.datasets._samples_generator import make_moons
import random
import math

x_range = 100
y_range = 100
n_node = 500
fig, ax = plt.subplots()

def gennode():
    xloc_list = []
    yloc_list = []
    # X, l = make_circles(n_samples=n_node, noise=0.1, factor=.2)
    # X, l = make_blobs(n_samples=n_node, centers=4, cluster_std=1, n_features=2)
    X, l = make_moons(n_samples=n_node, noise=0.1)
    xloc_list = X[:,0].tolist()
    yloc_list = X[:,1].tolist()
    # for a in range(n_node):
    #     xloc = random.randint(0,x_range)
    #     xloc_list.append(xloc)
    #     yloc = random.randint(0,y_range)
    #     yloc_list.append(yloc)
    return(xloc_list,yloc_list)

def finddis(xloc_list,yloc_list):
    dis_list = []
    for b in range(n_node):
        present_node = []
        present_node.extend((xloc_list[b],yloc_list[b]))
        dis_node_list = []
        for c in range(n_node):
            other_node = []
            other_node.extend((xloc_list[c],yloc_list[c]))
            distance = math.sqrt(((present_node[0]-other_node[0])**2)+((present_node[1]-other_node[1])**2))
            if distance>0.2: #depend on density and avg distance of data (10,5,0.2,3)
                dis_node_list.append(0)
            else:
                dis_node_list.append(1)
        dis_list.append(dis_node_list)
    return dis_list

def laplacian(dis_list):
    diag = []
    for i in dis_list:
        diag.append(sum(i))
    L = []
    sub_L = []
    for i in dis_list:
        for j in i:
            sub_L.append(j*(-1))
        L.append(sub_L.copy())
        sub_L = []
    for i,j in enumerate(L):
        j[i] = diag[i]
    return L

def eigan(L):
    l = np.array(L)
    vals, vecs = np.linalg.eig(l)
    vals = np.real(vals)
    vecs = np.real(vecs)
    return(vals,vecs)
    
def plotcluster(xloc_list,yloc_list,vals,vecs):
    cluster = int(input('how many cluster do you want : '))
    vecs = vecs[:,np.argsort(vals)] #sort eigan vectors by their eigan values, results still give the scoefficient of vector in vertical
    vals = vals[np.argsort(vals)]
    kmeans = KMeans(n_clusters=cluster)
    kmeans.fit(vecs[:,0:cluster]) #select the first n vectors for clustering by kmeans; n is number of cluster
    data_with_tag = kmeans.labels_
    group = [[] for i in range(cluster)]
    for i,j in enumerate(data_with_tag):
        group[j].append(i)
    color = ['blue','red','green','purple','orange']
    for k,j in enumerate(group):
        print('cluster'+str(k+1)+':',j)
        for i in j:
            plt.plot(xloc_list[i],yloc_list[i],marker='o',markerfacecolor=color[k],markersize='10',color='None',linestyle='None')
    plt.show()
    return group


xloc_list, yloc_list = gennode()
print(1)
A = finddis(xloc_list,yloc_list)
print(2)
L = laplacian(A)
print(3)
vals, vecs = eigan(L)
print(4)
plotcluster(xloc_list,yloc_list,vals,vecs)
print(5)
