sky_att = input("sky:")
temp_att = input("temp:")
humid_att = input("humidity:")
wind_att = input("wind:")
water_att = input("water:")
fore_att = input("forecst:")

queryDict = {'sky':sky_att,'temp':temp_att,'humid':humid_att,'wind':wind_att,'water':water_att,'forecst':fore_att}

train_set = [[{'sky':'sunny','temp':'warm','humid':'normal','wind':'strong','water':'warm','forecst':'same'},1],
            [{'sky':'sunny','temp':'warm','humid':'high','wind':'strong','water':'warm','forecst':'same'},1],
            [{'sky':'rainy','temp':'cold','humid':'high','wind':'strong','water':'warm','forecst':'change'},0],
            [{'sky':'sunny','temp':'warm','humid':'high','wind':'strong','water':'cool','forecst':'change'},1]]

S = {'sky':None,'temp':None,'humid':None,'wind':None,'water':None,'forecst':None}
G = [{'sky':'','temp':'','humid':'','wind':'','water':'','forecst':''}] 

def comprehensive(g,x): #does g cover x?
    change = [] #list of attribute that have to change by S
    for att in g:
        if g[att] != x[att] and g[att] != '':
            return False,[] #if there is only one attribute value diff then G doesn't cover x
        else:
            change.append(att) #keep attribute that x and g has the same value
    return True,change

def VSsearch():
    global S 
    global G
    for ex in train_set:
        newG = []
        if ex[1] == 1: #if example is positive
            for att in S: #chane every attribute value to be more general
                if S[att] != ex[0][att]: 
                    if S[att] == None:
                        S[att] = ex[0][att]
                    else:
                        S[att] = ''
            for hyp in G: #delete some hypothesis of G that is not cover positive example
                newG.append(hyp)
                for att in hyp:
                    if hyp[att] != ex[0][att] and hyp[att] != '':
                        newG.pop(-1)
                        break
            G = newG.copy()
        if ex[1] == 0: #if example is negative
            newG = []
            for hyp in G: #check every hypothesis in G
                cond1,position = comprehensive(hyp,ex[0])
                if cond1: #if the hyp cover negative example
                    for att in position: # try to specialize hyp by S to get multiple hyp that don't cover negative 
                        moreSpe = hyp.copy()
                        moreSpe[att] = S[att]
                        cond2,_ = comprehensive(moreSpe,ex[0])
                        if not cond2:
                            x = moreSpe.copy()
                            newG.append(x)
                else: #if the hyp doesn't cover then keep it
                    newG.append(hyp)
            G = newG.copy()

def findHyp(): #find the hypo in the space between S and G
    hyp = [S]
    for mem in G:
        hyp.append(mem)
        x = mem.copy()
        for att in S:
            if S[att] != '':
                x[att] = S[att]
                newX = x.copy()
                if newX not in hyp:
                    hyp.append(newX)
                x = mem.copy()
    return hyp

def query(x): #find answers of all hyp if query new ex
    neg = 0
    for i in hyp:
        for att in x:
            if x[att] != i[att] and i[att] != '':
                neg += 1
                break
    return (len(hyp)-neg,neg)
VSsearch()
hyp = findHyp()
ratio = query(queryDict)
print(ratio)
