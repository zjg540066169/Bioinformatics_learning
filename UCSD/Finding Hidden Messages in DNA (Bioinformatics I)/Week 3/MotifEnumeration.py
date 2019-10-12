#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:39:58 2019


Input: Integers k and d, followed by a collection of strings Dna.
Output: All (k, d)-motifs in Dna.



MotifEnumeration(Dna, k, d)
    Patterns ← an empty set
    for each k-mer Pattern in the first string in Dna
        for each k-mer Pattern’ differing from Pattern by at most d mismatches
            if Pattern' appears in each string from Dna with at most d mismatches
                add Pattern' to Patterns
    remove duplicates from Patterns
    return Patterns

@author: jungangzou
"""

from Neighbors import Neighbors




def MotifEnumeration(Dna, k ,d):
    
    Frequent_Set = set()
    
    Text = Dna[0]
    neighbor_list = []

    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        neighbor = Neighbors(pattern, d)
        neighbor.append(pattern)
        neighbor_list.extend(neighbor)
    
     
    Neighbor_Set = set(neighbor_list)
    print(Neighbor_Set)
    
        
        
        
        
    for neighbor in Neighbor_Set:

        pattern_neighbor_new = set(Neighbors(neighbor, d))
        pattern_neighbor_new.add(neighbor)
            
       
        
        line_count = 0
        for line in Dna:
            for pattern_new in pattern_neighbor_new:
                if pattern_new in line:
                    #print(line)
                    line_count += 1
                    break

        if line_count == len(Dna):
            Frequent_Set.add(neighbor)

    return sorted(Frequent_Set)

if __name__ == '__main__':
    with open("dataset_156_8 09.04.25.txt","r") as f:
        string = f.readlines()
        k, d = string[0][:-1].split(" ")
        
        print(string)
        k, d = int(k), int(d)
        dna = []
        for i in string[1:]:
            dna.append(i[:-1])
    


        result = MotifEnumeration(dna, k ,d)
        for i in result:
            print(i, end = " ")
            
            
# =============================================================================
#     dna = ['ATTTGGC','TGCCTTA', "CGGTATC", "GAAAATT"]
# 
#     k = 3
#     d = 1
#     print(MotifEnumeration(dna, k ,d))
# 
# =============================================================================
