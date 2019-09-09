#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:01:57 2019



PatternCount(Text, Pattern)
    count ← 0
    for i ← 0 to |Text| − |Pattern|
        if Text(i, |Pattern|) = Pattern
            count ← count + 1
    return count

O(|Text|*|Pattern|)
比较需要字符串需要花费O(|Pattern|)


@author: jungangzou
"""

def Pattern_Count(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

if __name__ == "__main__":
    with open("dataset_Pattern_Count.txt",'r') as f:
        string = f.readlines()
        Text = string[0][:-1]
        Pattern = string[1][:-1]
        print(Pattern_Count(Text,Pattern))
        