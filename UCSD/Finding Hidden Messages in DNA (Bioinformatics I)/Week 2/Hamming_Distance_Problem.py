#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:24:47 2019

Calculate how many mismatches do two length-equal strings have?

@author: jungangzou
"""

def Hamming_Distance_Problem(string1,string2):
    hamming_distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamming_distance += 1
    return hamming_distance

if __name__ == '__main__':
    with open("dataset_9_3.txt",'r') as f:
        string = f.readlines()
        print(string)
        string1 = string[0][:-1]
        string2 = string[1][:-1]
        print(Hamming_Distance_Problem(string1,string2))
