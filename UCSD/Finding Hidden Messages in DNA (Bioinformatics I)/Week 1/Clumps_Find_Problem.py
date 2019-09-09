#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:03:42 2019

@author: jungangzou
"""

def Clumps_Find_Problem(Genome, k_mer, clump_length, occur_frequent):
    Frequent_Patterns = set()
    Frequent_Dict = {}
    Clumps = set()
    #Frequent_Patterns_Num = 0
    init = 0
    for index in range(0,len(Genome) - clump_length + 1):
        text = Genome[index : index + clump_length]
        #print(len(Frequent_Patterns))
        
        Frequent_Dict,Frequent_Patterns,init = Frequent_Words_fast(text, k_mer,  occur_frequent,Frequent_Dict,Frequent_Patterns, init)
        Clumps = Clumps.union(Frequent_Patterns)
        #Frequent_Patterns_Num += len(Frequent_Patterns)
    return Clumps
        


def Frequent_Words_fast(Text, k_mer, occur_frequent,Frequent_Dict,Frequent_Patterns, init):
    
    
    Frequent_Patterns_Num = occur_frequent

    
    if Frequent_Dict == {}:
        for index in range(len(Text) - k_mer + 1):
            Current_Pattern_Count = Frequent_Dict.get(Text[index:index+k_mer],0) + 1
            Frequent_Dict[Text[index:index+k_mer]] = Current_Pattern_Count
            if Current_Pattern_Count >= Frequent_Patterns_Num:
                Frequent_Patterns.add(Text[index:index+k_mer])
    elif Frequent_Dict != {}:
        Frequent_Dict[init + Text[0:k_mer-1]] -= 1
        if Frequent_Dict[init + Text[0:k_mer-1]] < Frequent_Patterns_Num :
           if Frequent_Dict[init + Text[0:k_mer-1]] in Frequent_Patterns:
               #pass
               Frequent_Patterns.remove(init + Text[0:k_mer-1])
        Frequent_Dict[Text[-k_mer:]] = Frequent_Dict.get(Text[-k_mer:],0) + 1
        if Frequent_Dict[Text[-k_mer:]] >= Frequent_Patterns_Num:
            Frequent_Patterns.add(Text[-k_mer:])
    init = Text[0]
    return  Frequent_Dict,Frequent_Patterns,init

if __name__ == '__main__':
    with open("dataset_4_5.txt",'r') as f:
        string = f.readlines()
        Genome = string[0][:-1]
        number = string[1][:-1].split(' ')
        
        k_mer = int(number[0])
        clump_length = int(number[1])
        occur_frequent = int(number[2])
        #print(k_mer, clump_length, occur_frequent)
        print(Clumps_Find_Problem(Genome, k_mer, clump_length, occur_frequent))


# =============================================================================
#     with open("E_coli.txt",'r') as f:
#         string = f.readlines()
#         Genome = string[0][:-1]
# =============================================================================
        
        
        k_mer = 9
        clump_length = 500
        occur_frequent = 3
        #print(k_mer, clump_length, occur_frequent)
        print(Clumps_Find_Problem(Genome, k_mer, clump_length, occur_frequent))
