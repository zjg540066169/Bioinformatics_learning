# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:30:21 2018

@author: wang
"""

def Read(path):
    with open(path,'r') as f:
        string = f.readline().replace("\n","")
        return string

def ReverseComplementProblem(string):
    complementary = ""
    for i in string:
        if i == 'A':
            complementary = 'T'+complementary
        elif i == 'T':
            complementary = 'A'+complementary
        elif i == 'C':
            complementary = 'G'+complementary
        elif i == 'G':
            complementary = 'C'+complementary
    return complementary

if __name__ == '__main__':
    path = "dataset_3_2.txt"
    print(ReverseComplementProblem(Read(path)))