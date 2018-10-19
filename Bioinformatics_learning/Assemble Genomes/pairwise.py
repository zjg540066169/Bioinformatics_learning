# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:25:10 2018

@author: wang
"""
import numpy as np
import pandas as pd
def merGenerate(string,k,r):
    l = []
    for i in range(len(string)-2*k-r+1):
        l.append((string[i:i+k],string[i+r+k:i+2*k+r]))
    return l    

def De_Bruijn_graph(pairList):
    dic = {}
    for i in pairList:
        dic[i[0]] = []
    for i in pairList:
        if i[0] == i[1]:
            pass
        dic[i[0]].append(i[1])

    return dic    

      
def reconstruct(pairList,k,d):
    pair1 = ""
    pair2 = ""
    for i in pairList[:-1]:
        pair1 += i[0][0]
        pair2 += i[1][0]
    pair1 += pairList[-1][0]
    pair2 += pairList[-1][1]
    pair1 += pair2[-k-d:]
    print(pair1)


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
        #print(subpath)
        for i in range(len(path)):
            if path[i] == start:
                path = path[:i+1]+subpath+path[i+1:]
                break

    #print(path)
    #print(rest)
    return path
    for i in path[:-1]:
        print(i[0],end="")
    print(path[-1])


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

def recover(path,k):
    readList = []
    for i in range(len(path)-1):
        readList.append((path[i][0][0:k//2]+path[i+1][0][-k//2:],path[i][1][0:k//2]+path[i+1][1][-k//2:]))
    #readList.append((path[-1][0][0:k//2]+path[0][0][-k//2:],path[-1][1][0:k//2]+path[0][1][-k//2:]))
    return readList


if __name__ == '__main__':
# =============================================================================
#     l = mer("TAATGCCATGGGATGTT",3,2)
#     for i in l:
#         print("("+i[0]+"|"+i[1]+")",end = "")
# =============================================================================
    pairList = []
    with open(r"E:\dataset_204_15.txt",'r') as f:
        string = f.readlines()
        k,d = string[0].split(" ")
        for i in string[1:]:
            s = i.replace("\n","").split("|")
            pairList.append((s[0],s[1]))
    k = int(k)
    d = int(d)
    
    #print(pairList,k,d)
    s = []
    for i in pairList:
        s.append(((i[0][:k-1],i[1][:k-1]),(i[0][1:],i[1][1:])))
    #print(s)
    dic = De_Bruijn_graph(s)  
    #print(dic)
    start,end = Eulerian_Path_dic_find_start_end(dic)
    path = Eulerian_Path_dic(dic,start,end)
    print(path)
    pairList_new = recover(path,k)
    print(pairList_new)
    
    reconstruct(pairList_new,k,d)