#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:51:12 2019

@author: jungangzou
"""

from Hamming_Distance_Problem import Hamming_Distance_Problem

def Hamming_distance_string(pattern, string):
    min_distance = 99999999
    for i in range(len(string) - len(pattern) + 1):
        string_pattern = string[i:i+len(pattern)]
        hd = Hamming_Distance_Problem(pattern, string_pattern)
        if hd < min_distance:
            min_distance = hd
    return min_distance


