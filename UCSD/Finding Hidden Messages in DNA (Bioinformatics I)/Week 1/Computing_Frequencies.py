# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:05:07 2018

@author: wang
"""
import numpy as np
from Pattern_to_Number import PatternToNumber
def ComputingFrequencies(Text, k):
    array = np.zeros((1,4**k),dtype=np.int)
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        number = PatternToNumber(pattern)
        array[0,number] += 1
    return array[0]
    
def Read(path):
    with open(path,'r') as f:
        string = f.readline().replace("\n","")
        k = int(f.readline().replace("\n",""))
        return string, k
    
def writeList(path,lis):
    with open(path,'w') as f:
        for i in lis:
            f.write(str(i)+" ")

if __name__ == '__main__':
    path = Read("dataset_2994_5.txt")
    a = (ComputingFrequencies(path[0],path[1]))
    writeList("dataset_2994_5_result.txt",a)