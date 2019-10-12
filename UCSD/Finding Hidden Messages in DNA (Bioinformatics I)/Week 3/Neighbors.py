#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:58:47 2019

@author: jungangzou
"""

def Neighbors(string,d):
    if d == 0:
        return [string]
    elif len(string) == 1:
        if string[0] == 'A':
            return ['C','G','T']
        elif string[0] == 'C':
            return ['A','G','T']
        elif string[0] == 'G':
            return ['A','C','T']
        elif string[0] == 'T':
            return ['A','C','G']
    else:
        Neighbors_Array = []
        dex = string[0]
        Suffix_Neighbors = Neighbors(string[1:],d)
        for i in Suffix_Neighbors:
            Neighbors_Array.append(dex+i)
            
        Suffix_Neighbors_D_1 = Neighbors(string[1:],d - 1)
        if dex == 'A':
            first = ['C','G','T']
        elif dex == 'C':
            first = ['A','G','T']
        elif dex == 'G':
            first = ['A','C','T']
        elif dex == 'T':
            first = ['A','C','G']
        for i in first:
            for j in Suffix_Neighbors_D_1:
                Neighbors_Array.append(i+j)
    return Neighbors_Array

if __name__ == '__main__':
    ls = Neighbors('AA',1)
    for i in ls:
        print(i, end = ' ')