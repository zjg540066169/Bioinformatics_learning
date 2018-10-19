# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:19:13 2018

@author: wang
"""

import pandas as pd
import numpy as np


def De_Bruijn_graph(pairList):
    dic = {}
    for i in pairList:
        dic[i[0]] = []
    for i in pairList:
        dic[i[0]].append(i[1])
        if len(dic[i[0]])>2:
            pass
    return dic    
    with open(r"E:\1.txt",'w') as f:
        for i in dic:
            if len(dic[i]) >= 1:
                f.write(i+" -> "+dic[i][0])
                print(i+" -> "+dic[i][0],end = "")
                if len(dic[i])>1:
                    for j in dic[i][1:]:
                        f.write(","+j)
                        print(","+j,end="")
                f.write("\n")
                print()


def generateBinary(k,length):
    a = bin(k)[2:]
    b = ""
    if len(a) < length:
        b = "0"*(length-len(a))
    return b+a   



l = list()
with open(r"E:\dataset_203_7.txt",'r') as f:
    
    string = f.readlines()
    num = string[0]
    string = string[1:]

   

l = []
s = []
k = set()
for i in string:
    j = i[:-1]
    s.append((j[0:len(j)-1],j[1-len(j):]))
De_Bruijn_graph(s)    
    

    
