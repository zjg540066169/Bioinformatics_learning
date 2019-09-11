#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:42:58 2019

ApproximatePatternCount(Text, Pattern, d)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            Pattern′ ← Text(i , |Pattern|)
            if HammingDistance(Pattern, Pattern′) ≤ d
                count ← count + 1
        return count

Input: Strings Pattern and Text as well as an integer d.
Output: Countd(Text, Pattern).
@author: jungangzou
"""

def pproximate_Pattern_Count(Text, Pattern, d):
    start_position_array = []
    for i in range(len(Text) - len(Pattern) + 1):
        if Hamming_Distance_Problem(Text[i:i+len(Pattern)] , Pattern) <= d :
            start_position_array.append(i)
    return len(start_position_array)

if __name__ == '__main__':
    
