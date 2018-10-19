# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:45:50 2018

@author: wang
"""

def PatternToNumber(pattern):
    length = len(pattern)
    count = 0
    for i in range(len(pattern)):
        if pattern[i] == 'A':
            count += 0 * 4 ** (length - i - 1 )
        elif pattern[i] == 'C':
            count += 1 * 4 ** (length - i - 1 )
        elif pattern[i] == 'G':
            count += 2 * 4 ** (length - i - 1 )
        elif pattern[i] == 'T':
            count += 3 * 4 ** (length - i - 1 )
    return count

if __name__ == '__main__': 
    print(PatternToNumber("CCATATCGTGGCCGCCCA"))