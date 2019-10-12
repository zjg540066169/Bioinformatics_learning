#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:44:46 2019

@author: jungangzou
"""


def Hamming_Distance_Problem(string1,string2):
    hamming_distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamming_distance += 1
    return hamming_distance


def Hamming_distance_string(pattern, string):
    min_distance = 99999999
    for i in range(len(string) - len(pattern) + 1):
        string_pattern = string[i:i+len(pattern)]
        hd = Hamming_Distance_Problem(pattern, string_pattern)
        if hd < min_distance:
            min_distance = hd
    return min_distance

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    distance = 0
    for i in Dna:
        distance += Hamming_distance_string(Pattern, i)
    return distance

if __name__ == '__main__':
    with open("dataset_5164_1-2.txt","r") as f:
        string = f.readlines()
        pattern = string[0][:-1]
        
        dna = string[1][:-1].split()
        
        print(DistanceBetweenPatternAndStrings(pattern, dna))
