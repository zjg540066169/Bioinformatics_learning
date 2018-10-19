# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:09:12 2018

@author: wang
"""

import pandas as pd
import numpy as np

def De_Bruijn_graph(pairList):
    dic = {}
    for i in pairList:
        dic[i[0]] = []
    for i in pairList:
        if i[0] == i[1]:
            pass
        dic[i[0]].append(i[1])

    return dic    


def recover(path):
    readList = []
    k = len(path[0])
    for i in range(len(path)-1):
        readList.append(path[i][0:k-1]+path[i+1][1-k:])
    readList.append(path[-1][0:k-1]+path[0][1-k:])
    string = ""
    for i in readList[:-1]:
        string += i[0]
    string += readList[-1]
    print(string)
    count = -1
    for i in range(int(len(string)/2)):
        #print(i,1-i)
        if string[0:i] == string[::-1][0:i]:
            count = i
        else:
            break
    if count != -1:
        print(string[:-count])
        return string[:1-count]




def generateBinary(k,length):
    a = bin(k)[2:]
    b = ""
    if len(a) < length:
        b = "0"*(length-len(a))
    return b+a   

def Eulerian_Cycle_dic(dic):
    start = list(dic.keys())[0]
    path = []
    path.append(start)
    rest = {}
    for i in dic:
        rest[i] = len(dic[i])
    #print(adjan_matrix)
    #print(rest)
    #print(rest.sum())
    while np.array(list(rest.values())).sum()>0:
        #print(np.array(list(rest.values())).sum())
        subpath = []
        for num in path:
            if rest[num]!= 0:
                start = num
                break
        #print(start,rest)
        step = 1
        
            
        rest[start] -= 1
       
        step = dic[start].pop()
                
        #print(step)
        while step!=start:
            
    
            rest[step] -= 1
            subpath.append(step)
            #print(dic[step])
            step = dic[step].pop()
            #print(step)
        rest[step] -= 1
        subpath.append(step) 
        #print(subpath)
        for i in range(len(path)):
            if path[i] == start:
                path = path[:i+1]+subpath+path[i+1:]
                break
    print(path)
    return path
    
    count = -1
    for i in range(int(len(string)/2)):
        #print(i,1-i)
        if string[0:i] == string[::-1][0:i]:
            count = i
        else:
            break
    if count != -1:
        #print(string[:1-count])
        return string[:1-count]
    
def getRead(circle,k):
    s = []
    circle+=circle[:k-1]
    print(circle)
    for i in range(len(circle)-k+1):
        s.append(circle[i:i+k])
    print(s)


with open(r"E:\dataset_203_11.txt",'r') as f:
    string = f.readlines()
    num = int(string[0])
num = 4
string = []
string = ['AAAT','AATG','ACCC','ACGC','ATAC','ATCA','ATGC','CAAA','CACC','CATA','CATC','CCAG','CCCA','CGCT','CTCA','GCAT','GCTC','TACG','TCAC','TCAT','TGCA']
s = []
k = set()
for i in string:
    j = i
    s.append((j[0:len(j)-1],j[1-len(j):]))
#print(s)
dic = De_Bruijn_graph(s)  
#print(dic) 
circle = Eulerian_Cycle_dic(dic)
recover(circle)
#getRead("0000110010111101",num)

