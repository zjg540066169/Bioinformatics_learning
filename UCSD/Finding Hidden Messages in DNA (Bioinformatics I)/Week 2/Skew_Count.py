#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:36:10 2019

@author: jungangzou
"""
import matplotlib.pyplot as plt
import numpy as np

def Skew_Count(strand):
    count_array = [0]
    for i in range(len(strand)):
        if strand[i] == 'C':
            count_array.append(count_array[i] - 1)
        elif strand[i] == 'G':
            count_array.append(count_array[i] + 1)
        else:
            count_array.append(count_array[i])
    return count_array


if __name__ == '__main__':
    result = Skew_Count("CATTCCAGTACTTCGATGATGGCGTGAAGA")
    plt.plot(np.arange(len(result)),result)
    plt.show()
    for i in result:
        print(i,end = ' ')
    