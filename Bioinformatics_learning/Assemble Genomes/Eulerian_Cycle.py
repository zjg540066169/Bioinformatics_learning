# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:04:35 2018

@author: wang
"""

import numpy as np
import pandas as pd

def Eulerian_Cycle_adjan_matrix(adjan_matrix):
    path = []
    path.append( 0)
    rest = np.array(np.zeros((1,len(adjan_matrix.columns))))
    for i in adjan_matrix.index:
        rest[0,int(i)] = adjan_matrix.loc[i,:].sum()
    rest = rest[0]
    print(adjan_matrix)
    print(rest)
    pathCount = rest.sum()+1
    #print(rest.sum())
    while rest.sum()!=0:
        print(rest.sum())
        subpath = []
        for num in range(len(rest)):
            if rest[num]!= 0:
                start = num
                break
        #print(start,rest)
        step = 1
        for nextStep in range(len(adjan_matrix.loc[start,:])):
            if adjan_matrix.loc[start,nextStep]>0:
                adjan_matrix.loc[start,nextStep] -= 1
                step = nextStep
                break
        #print(step)
        while step!=start:
            
    
            rest[step] -= 1
            subpath.append(step)
            for nextStep in range(len(adjan_matrix.loc[step,:])):
                if adjan_matrix.loc[step,nextStep]>0:
                    adjan_matrix.loc[step,nextStep] -= 1
                    step = nextStep
                    break
        rest[step] -= 1
        subpath.append(step) 
        #print(subpath)
        for i in range(len(path)):
            if path[i] == start:
                path = path[:i+1]+subpath+path[i+1:]
                break
    print(path)
    print(rest)  
    print(adjan_matrix)
    for i in path[:-1]:
        print(str(i)+"->",end="")
    print(path[-1])


def Eulerian_Cycle_dic(dic):
    path = []
    path.append(0)
    rest = {}
    for i in dic:
        rest[i] = len(dic[i])
    #print(adjan_matrix)
    print(rest)
    #print(rest.sum())
    while np.array(list(rest.values())).sum()>0:
        print(np.array(list(rest.values())).sum())
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
            print(dic[step])
            step = dic[step].pop()
            print(step)
        rest[step] -= 1
        subpath.append(step) 
        #print(subpath)
        for i in range(len(path)):
            if path[i] == start:
                path = path[:i+1]+subpath+path[i+1:]
                break
    print(path)
    print(rest)  
    with open(r"E:\1.txt",'w') as f:
        for i in path[:-1]:
            f.write(str(i)+"->")
            print(str(i)+"->",end="")
        f.write(str(path[-1]))
        print(str(path[-1]))


def Eulerian_Path_dic_find_start_end(dic):
    key = set(list(dic.keys()))
    value = set()
    for i in dic:
        value = value.union(set(dic[i]))
    a = list(key.symmetric_difference(value))
    start = end = -1
    if a[0] not in key:
        end = a[0]
    if a[0] not in value:
        start = a[0]
    if len(a) > 1:
        if a[1] not in key:
            end = a[1]
    
        if a[1] not in value:
            start = a[1]
    if start!=-1 and end != -1:
        return (start,end)
    if start == -1 or end == -1:
        dic_new = {}
        for i in dic:
            if i not in dic_new:
                dic_new[i] = [0,0]
            dic_new[i][0] = len(dic[i])
            for j in dic[i]:
                if j not in dic_new:
                    dic_new[j] = [0,0]
                dic_new[j][1] += 1
        for i in dic_new:
            if dic_new[i][0] > dic_new[i][1]:
                start = i
            elif dic_new[i][0] < dic_new[i][1]:
                end = i
        return (start,end)

        




def Eulerian_Path_dic(dic,start,end):
    dic[end] = []
    path = []
    path.append(start)
    #print(path[0])
    rest = {}
    for i in dic:
        rest[i] = len(dic[i])
    #print(adjan_matrix)
    #print(rest.sum())
    count = 0
    while np.array(list(rest.values())).sum()>0:
        print(np.array(list(rest.values())).sum())
        subpath = []
        if count !=0 :
            for num in path:
                if rest[num] > 0:
                    print(num)
                    start = num
                    break
        else:
            start = path[0]
            
        rest[start] -= 1

            
        #print(dic[start])
        step = dic[start].pop()
                
        #print(step)
        if count != 0:
            while step!=start:
                rest[step] -= 1
                subpath.append(step)
                #print(dic[step])
                step = dic[step].pop()
                #print(step)
            
            
        else:
            while  step != end:
                rest[step] -= 1
                subpath.append(step)
                #print(dic[step])
                step = dic[step].pop()
                #print(step)
            count =1
         
        
        subpath.append(step) 
        print(subpath)
        for i in range(len(path)):
            if path[i] == start:
                path = path[:i+1]+subpath+path[i+1:]
                break

    #print(path)
    #print(rest)
    for i in path[:-1]:
        print(i[0],end="")
    print(path[-1])
# =============================================================================
#     with open(r"E:\1.txt",'w') as f:
#         for i in path[:-1]:
#             f.write(str(i)+"->")
#             print(str(i)+"->",end="")
#         f.write(str(path[-1]))
#         print(str(path[-1]))
# 
# =============================================================================
dic = {}


with open(r"E:\1.txt",'r') as f:
    for i in f:
        a = i.replace("\n","").split(" -> ")

        dic[a[0]] = a[1].split(",")


start,end = Eulerian_Path_dic_find_start_end(dic)
print(start,end)
# =============================================================================
# ad_matrix = pd.DataFrame(np.zeros((len(dic.keys()),len(dic.keys()))),index = dic.keys(),columns = dic.keys())      
# for i in dic:
#     if type(dic[i]) == int:
#         ad_matrix.loc[i,dic[i]] += 1
#     else:
#         for j in dic[i]:
#             ad_matrix.loc[i,j] += 1
# =============================================================================
Eulerian_Path_dic(dic,start,end)