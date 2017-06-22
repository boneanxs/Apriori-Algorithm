import itertools
def getSubSet(S):
    subLens = len(S) - 1
    return [list(i) for i in itertools.combinations(S,subLens)]

def isSubSetExist(tar, L):
    tar = [set(i[0]) for i in tar]
    isIn = 1
    for i in L:
        for j in tar:
            if j < set(i):
                isIn = 0
                return isIn
    return isIn
                
def Apriori(tar, thr, le):
    curFrequ = {}
    for key in tar.keys():
        items = tar[key]
        for item in items:
            if item not in curFrequ.keys():
                curFrequ[item] = 1
            else:
                curFrequ[item] += 1
    tarLen = len(list(tar.keys()))
    keys = list(curFrequ.keys())
    for key in keys:
        curFrequ[key] = curFrequ[key] / tarLen
        if curFrequ[key] < thr:
            del curFrequ[key]
    curFrequ = [[key,curFrequ[key]] for key in curFrequ.keys()]
    if le == 1:
        return curFrequ
    tempLe = 2
    while tempLe <= le:
        tempList = []
        for i in range(len(curFrequ)):
            for j in range(i+1,len(curFrequ)):
                temp = []
                if tempLe == 2:
                    temp = [curFrequ[i][0],curFrequ[j][0]]
                else:
                    temp = list(set(curFrequ[i][0]) | set(curFrequ[j][0]))
                if len(temp) != tempLe:
                    continue
                temp.sort()
                if isSubSetExist(curFrequ,getSubSet(temp)) == 1:
                    if temp not in tempList:
                        tempList.append(temp)
        curFrequ = []
        for item in tempList:
            tempLen = 0
            for key in tar.keys():
                if set(item) <= set(tar[key]):
                    tempLen += 1
            tempLen = tempLen /tarLen
            if tempLen >= thr:
                curFrequ.append([item,tempLen])
        tempLe += 1
    return curFrequ
