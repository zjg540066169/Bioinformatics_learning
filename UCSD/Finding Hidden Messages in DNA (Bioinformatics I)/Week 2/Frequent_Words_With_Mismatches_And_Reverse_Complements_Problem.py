#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:53:53 2019

@author: jungangzou
"""

from Neighbors import Neighbors

def Frequent_Words_With_Mismatches_And_Reverse_Complements_Problem(Text, k, d):
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
        
        reverse_pattern = Reverse_Complement_Problem(pattern)
        if reverse_pattern not in Neighbor_Dictionary:
            reverse_pattern_neighbor = set(Neighbors(reverse_pattern, d))
            Neighbor_Dictionary[reverse_pattern] = reverse_pattern_neighbor
        else:
            reverse_pattern_neighbor = Neighbor_Dictionary[reverse_pattern]
        reverse_pattern_neighbor.add(reverse_pattern)

        total_pattern_neighbor = pattern_neighbor.union(reverse_pattern_neighbor)
        for neighbor in total_pattern_neighbor:
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
# =============================================================================
#         if Reverse_Complement_Problem(i) not in Frequent_Dictionary:
#             re_count = 0
#         else:
#             re_count = Frequent_Dictionary[Reverse_Complement_Problem(i)]
#         if Reverse_Complement_Problem(i) == i:
#             re_count = 0
# =============================================================================
        if Frequent_Dictionary[i] > Frequent_Count:
            Frequent_Count = Frequent_Dictionary[i] 
            #print(Frequent_Set)
            Frequent_Set = set()
            Frequent_Set.add(i)
        elif Frequent_Dictionary[i] == Frequent_Count:
            Frequent_Set.add(i)
    return sorted(Frequent_Set)


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

if __name__ == "__main__":
    with open("dataset_9_7.txt",'r') as f:
        string = f.readlines()

        Text = "AAGAAAGATGATTAGATAGAGATAAAATATATATAGAGAAAGATTCAGATGAAAAAAATCATCATCAAATATAGAGATCAAAGATATCAGATATCAGATCATAAAAAAATCATAGATGATGAAAGATAATCAGATGAAATAAATAGAGAAATAAATAAATAGATAAGAGATAAAGATTAGAAATAGATGATTCAAAGATTATCATCATAGA"
        number = string[1][:-1].split()
        k,d = 7,2
        result = Frequent_Words_With_Mismatches_And_Reverse_Complements_Problem(Text, k, d)
        print(result)
