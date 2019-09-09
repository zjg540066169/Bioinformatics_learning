#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Sep  8 22:46:13 2019

FrequentWords(Text, k)
    FrequentPatterns ← an empty set
    for i ← 0 to |Text| − k
        Pattern ← the k-mer Text(i, k)
        Count(i) ← PatternCount(Text, Pattern)
    maxCount ← maximum value in array Count
    for i ← 0 to |Text| − k
        if Count(i) = maxCount
            add Text(i, k) to FrequentPatterns
    remove duplicates from FrequentPatterns
    return FrequentPatterns
    
O(|Text| **2 * |k|)

@author: jungangzou
"""


from Pattern_Count import Pattern_Count

def Frequent_Words(Text, k):
    
    Frequent_Patterns = set()
    Frequent_Patterns_Num = 0
    for index in range(len(Text) - k + 1):
        Current_Pattern_Count = Pattern_Count(Text,Text[index:index+k])
        if Current_Pattern_Count > Frequent_Patterns_Num:
            Frequent_Patterns_Num = Current_Pattern_Count
            Frequent_Patterns = set()
            Frequent_Patterns.add(Text[index:index+k])
        elif Current_Pattern_Count == Frequent_Patterns_Num:
            Frequent_Patterns.add(Text[index:index+k])
    return  Frequent_Patterns







if __name__ =='__main__':
    with open("dataset_2_10.txt",'r') as f:
        string = f.readlines()
        
        Text = string[0][:-1]
        k = int(string[1][:-1])
        a = Frequent_Words(Text,k)
        for i in a:
            print(i,end = ' ')
        
# =============================================================================
#     print(Frequent_Words('CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT',3))
# =============================================================================
