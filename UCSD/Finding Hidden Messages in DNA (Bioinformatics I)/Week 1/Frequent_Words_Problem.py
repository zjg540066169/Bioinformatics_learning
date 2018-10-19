# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:02:51 2018

@author: wang
"""

def Read(path):
    with open(path,'r') as f:
        string = f.readline().replace("\n","")
        k = int(f.readline().replace("\n",""))
        return string, k
    
def FrequentWordsProblem(string,k):
    patternDic = {}
    for i in range(len(string) - k + 1):
        patternDic[string[i:i+k]] = patternDic.get(string[i:i+k],0)+1
    sortedDict= sorted(patternDic.items(), key=lambda x:x[1] , reverse = True)
    #print(sortedDict)
    maxPattern = []
    maxCount = sortedDict[0][1]
    #print(maxCount)
    for i in sortedDict:
        if i[1] == maxCount:
            maxPattern.append(i[0])
        else:
            break
    return maxPattern
    
if __name__ == '__main__':
    path = "dataset_2_10.txt"
    print(FrequentWordsProblem("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT",3))