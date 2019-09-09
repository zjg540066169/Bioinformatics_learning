# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:37:38 2018

@author: wang
"""

def Read(path):
    with open(path,'r') as f:
        pattern = f.readline().replace("\n","")
        genome = f.readline().replace("\n","")
        return genome,pattern
    
def PatternMatchingProblem(pattern,genome):
    count = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i+len(pattern)] == pattern:
            count.append(i)
    return count

def writeList(path,lis):
    with open(path,'w') as f:
        for i in lis:
            f.write(str(i)+" ")

if __name__ == '__main__':
    path = "Vibrio_cholerae.txt"
    a = (PatternMatchingProblem("AA","AAACATAGGATCAAC"))
    print(a)
