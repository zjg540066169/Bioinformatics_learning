#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:30:12 2019

Find all approximate occurrences of a pattern in a string.

Input: Strings Pattern and Text along with an integer d.
Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

@author: jungangzou
"""

from Hamming_Distance_Problem import Hamming_Distance_Problem

def Approximate_Pattern_Matching_Problem(Pattern, Text, d):
    start_position_array = []
    for i in range(len(Text) - len(Pattern) + 1):
        if Hamming_Distance_Problem(Text[i:i+len(Pattern)] , Pattern) <= d :
            start_position_array.append(i)
    return start_position_array



      
if __name__ == '__main__':
# =============================================================================
#     with open("dataset_9_4.txt",'r') as f:
#         string = f.readlines()
#         Pattern = string[0][:-1]
#         Text = string[1][:-1]
#         d = int(string[2][:-1])
#         
#         result = Approximate_Pattern_Matching_Problem(Pattern, Text, d)
#     with open("dataset_9_4_result.txt",'w') as g:
#         for i in result:
#             g.write(str(i)+" ")
# =============================================================================
        
        
        
    with open("dataset_9_6.txt",'r') as f:
        string = f.readlines()
        Pattern = string[0][:-1]
        Text = string[1][:-1]
        d = int(string[2][:-1])
        result = Approximate_Pattern_Matching_Problem(Pattern, Text, d)
        print(len(result))

