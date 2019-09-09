#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:22:11 2019





@author: jungangzou
"""


def Reverse_Complement_Problem(string):
    Reverse_Complement_String = ""
    for gene in range(len(string) - 1 , -1, -1):
        if string[gene] == 'A':
            Reverse_Complement_String += "T"
        elif string[gene] == 'C':
            Reverse_Complement_String += "G"
        elif string[gene] == 'G':
            Reverse_Complement_String += "C"
        elif string[gene] == 'T':
            Reverse_Complement_String += "A"
    return Reverse_Complement_String

if __name__ == '__main__':
    with open("dataset_3_2.txt",'r') as f:
        string = f.readlines()[0]
        
        
        print(Reverse_Complement_Problem(string))

    #print(Reverse_Complement_Problem('CCAGATC'))