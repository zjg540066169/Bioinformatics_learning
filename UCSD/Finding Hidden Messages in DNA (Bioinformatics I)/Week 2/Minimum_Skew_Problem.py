#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:49:09 2019

@author: jungangzou
"""

import matplotlib.pyplot as plt
import numpy as np

def Minimum_Skew_Problem(strand):
    minimum_index = []
    minimum_count = 0
    current_count = 0
    for i in range(len(strand)):
        if strand[i] == 'C':
            current_count -= 1
        elif strand[i] == 'G':
            current_count += 1
        if current_count < minimum_count:
            minimum_index = [i+1]
            minimum_count = current_count
        elif current_count == minimum_count:
            minimum_index.append(i+1)
    return minimum_index


if __name__ == '__main__':
    with open("dataset_7_6.txt",'r') as f:
        string = f.readlines()[0][:-1]
        #print(string)
        print(Minimum_Skew_Problem(string))
        
    