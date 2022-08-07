import math
train_set = [
    {'fever':0,'cough':0,'breath-iss':0,'target':0},
    {'fever':1,'cough':1,'breath-iss':1,'target':1},
    {'fever':1,'cough':1,'breath-iss':0,'target':0},
    {'fever':1,'cough':0,'breath-iss':1,'target':1},
    {'fever':1,'cough':1,'breath-iss':1,'target':1},
    {'fever':0,'cough':1,'breath-iss':0,'target':0},
    {'fever':1,'cough':0,'breath-iss':1,'target':1},
    {'fever':1,'cough':0,'breath-iss':1,'target':1},
    {'fever':0,'cough':1,'breath-iss':1,'target':1},
    {'fever':1,'cough':1,'breath-iss':0,'target':1},
    {'fever':0,'cough':1,'breath-iss':0,'target':0},
    {'fever':0,'cough':1,'breath-iss':1,'target':1},
    {'fever':0,'cough':1,'breath-iss':1,'target':0},
    {'fever':1,'cough':1,'breath-iss':0,'target':0}
]
att = ['fever','cough','breath-iss']
def entropy(x):
    zig = 0
    for v in x:
        zig += (v/sum(x))*math.log2(v/sum(x))
    return -1*zig
def IG(a,b):
    result = a
    for i in b:
        result += -1*((i[1]/len(upper))*i[0])
    return result
def createNode():
    counter = 0
    for i in upper:
        if i['target'] == 0:
            counter+=1
    top = entropy([counter,len(upper)-counter])
    bestIG = 0
    node = ''
    for a in att:
        att_type = []
        Filter = {}
        for ex in upper:
            if ex[a] not in att_type:
                att_type.append(ex[a])
            if (ex[a],ex['target']) not in Filter:
                Filter[(ex[a],ex['target'])] = 1
            else:
                Filter[(ex[a],ex['target'])] += 1
        etp_set = []
        for i in att_type:
            c = []
            for group in Filter:
                if group[0] == i:
                    c.append(Filter[group])
            etp_set.append([entropy(c),sum(c)])
        ig = IG(top,etp_set)
        if ig > bestIG:
            bestIG = ig
            node = a
    return node

upper = train_set
node = createNode()
tree = {node:'root'}
att.remove(node)
while len(att) != 0:
    parent = node
    newUp = {}
    for ex in upper:
        if ex[node] not in newUp:
            newUp[ex[node]] = [ex]
        else:
            newUp[ex[node]].append(ex)
    for val in newUp:
        upper = newUp[val]
        node = createNode()
        att.remove(node) 
        tree[node] = [parent,val]

print(tree)