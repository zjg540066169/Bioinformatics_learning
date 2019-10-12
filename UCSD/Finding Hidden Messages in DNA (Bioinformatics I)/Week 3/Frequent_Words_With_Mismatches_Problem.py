#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:32:16 2019

@author: jungangzou
"""

from Neighbors import Neighbors

def Frequent_Words_With_Mismatches_Problem(Text, k, d):
    #k means the length of frequent words with k-mers
    #d means the maximun number of mismatches
    Neighbor_Dictionary = {}
    Frequent_Set = set()
    Frequent_Dictionary = {}
    Frequent_Count = 0
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        if pattern not in Neighbor_Dictionary:
            pattern_neighbor = set(Neighbors(pattern, d))
            Neighbor_Dictionary[pattern] = pattern_neighbor
        else:
            pattern_neighbor = Neighbor_Dictionary[pattern]
        pattern_neighbor.add(pattern)
        #print(i,pattern_neighbor)
        for neighbor in pattern_neighbor:
            Frequent_Dictionary[neighbor] = Frequent_Dictionary.get(neighbor,0) + 1
            #pattern_count += Frequent_Dictionary[neighbor]
        #print(i,Frequent_Dictionary)   
            
# =============================================================================
#             if pattern_count > Frequent_Count:
#                 Frequent_Count = pattern_count
#                 Frequent_Set = set()
#                 Frequent_Set.add(pattern)
#             elif pattern_count == Frequent_Count:
#                 Frequent_Set.add(pattern)
# =============================================================================
        
    for i in Frequent_Dictionary:
        #print(Frequent_Dictionary[i], Frequent_Count)
        if Frequent_Dictionary[i] > Frequent_Count:
            Frequent_Count = Frequent_Dictionary[i]
            #print(Frequent_Set)
            Frequent_Set = set()
            Frequent_Set.add(i)
        elif Frequent_Dictionary[i] == Frequent_Count:
            Frequent_Set.add(i)
    return sorted(Frequent_Set)

if __name__ == "__main__":
    with open("dataset_9_7.txt",'r') as f:
        string = f.readlines()

        Text = string[0][:-1]
        number = string[1][:-1].split()
        k,d = int(number[0]),int(number[1])
        result = Frequent_Words_With_Mismatches_Problem(Text, k, d)
        print(result)

    
    
    