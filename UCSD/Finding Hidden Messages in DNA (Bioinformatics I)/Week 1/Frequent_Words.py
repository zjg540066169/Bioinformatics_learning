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





def Frequent_Words_fast(Text, k_mer,Frequent_Dict = {},Frequent_Patterns = set()):#, init):
    
    
    Frequent_Patterns_Num = 0

    
    if Frequent_Dict == {}:
        for index in range(len(Text) - k_mer + 1):
            Current_Pattern_Count = Frequent_Dict.get(Text[index:index+k_mer],0) + 1
            Frequent_Dict[Text[index:index+k_mer]] = Current_Pattern_Count
            if Current_Pattern_Count >= Frequent_Patterns_Num:
                Frequent_Patterns_Num = Current_Pattern_Count
                Frequent_Patterns.add(Text[index:index+k_mer])
    elif Frequent_Dict != {}:
       # Frequent_Dict[init + Text[0:k_mer-1]] -= 1
        Frequent_Dict[Text[1-k_mer:]] = Frequent_Dict.get(Text[1-k_mer:],0) + 1
        if Frequent_Dict[Text[1-k_mer:]] >= Frequent_Patterns_Num:
            Frequent_Patterns.add(Frequent_Dict[Text[1-k_mer:]])
            Frequent_Patterns_Num = Frequent_Dict[Text[1-k_mer:]]
    
    return  Frequent_Patterns


if __name__ =='__main__':
    with open("dataset_Frequent_Words.txt",'r') as f:
        string = f.readlines()
        
        Text = string[0][:-1]
        k = int(string[1][:-1])
        print(Frequent_Words_fast(Text,k))
