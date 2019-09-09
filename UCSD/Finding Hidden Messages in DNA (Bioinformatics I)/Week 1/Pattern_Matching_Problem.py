#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:43:09 2019

@author: jungangzou
"""

def Pattern_Matching_Problem(Genome,Pattern):
    Position_Array = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i : i + len(Pattern)] == Pattern:
            Position_Array.append(i)
    return Position_Array

if __name__ == '__main__':
# =============================================================================
#     with open("dataset_Pattern_Matching_Problem.txt",'r') as f:
#         string = f.readlines()
#         Pattern = string[0][:-1]
#         Genome = string[1][:-1]
#         for i in Pattern_Matching_Problem(Genome,Pattern):
#             print(i,end = ' ')
# =============================================================================
            
            
    with open("Vibrio_cholerae.txt",'r') as f:
        string = f.readlines()
        Pattern = "CTTGATCAT"
        Genome = string[0][:-1]
        PM_result = Pattern_Matching_Problem(Genome,Pattern)
        with open("Vibrio_cholerae_result.txt",'w') as g:
            
            for i in PM_result:
                g.write(str(i)+" ")
                