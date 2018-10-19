# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:54:49 2018

@author: wang
"""
import numpy as np
import pandas as pd

def Read(path):
    with open(path,'r') as f:
        string = f.readline().replace("\n","")
        pattern = f.readline().replace("\n","")
        return string,pattern
    
def PatternCount(string,pattern):
    count = 0
    for i in range(len(string) - len(pattern) + 1):
        if string[i:i+len(pattern)] == pattern:
            count += 1
    return count


if __name__ == '__main__':
    path = "dataset_2_7.txt"
    print(PatternCount("CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC","CGCG"))
        