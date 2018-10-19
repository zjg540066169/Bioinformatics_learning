# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:58:31 2018

@author: wang
"""
def Read(path):
    with open(path,'r') as f:
        string = f.readline().replace("\n","")
        num = f.readline().replace("\n","").split(" ")
        k = int(num[0])
        L = int(num[1])
        t = int(num[2])
        return string, k, L , t

def ClumpFindingProblem(genome,k,L,t):
    maxPattern = set()
    for i in range(len(genome) - L + 1):
        string = genome[i:i+L]
        patternDic = {}
        for j in range(len(string) - k + 1):
            patternDic[string[j:j+k]] = patternDic.get(string[j:j+k],0)+1
        sortedDict= sorted(patternDic.items(), key=lambda x:x[1] , reverse = True)
        maxCount = sortedDict[0][1]
        if maxCount >= t:
            for j in sortedDict:
                if j[1] == maxCount:
                    maxPattern.add(j[0])
                else:
                    break
    return list(maxPattern)

def writeList(path,lis):
    with open(path,'w') as f:
        for i in lis:
            f.write(str(i)+" ")

if __name__ == '__main__':
    path = "dataset_4_5.txt"
    a = ClumpFindingProblem(Read(path)[0],Read(path)[1],Read(path)[2],Read(path)[3])
    print(len(a))