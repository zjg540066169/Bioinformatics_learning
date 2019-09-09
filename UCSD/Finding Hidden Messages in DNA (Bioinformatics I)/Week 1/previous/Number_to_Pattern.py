# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:56:24 2018

@author: wang
"""

def NumberToPattern(index, k):
    string = ""
    while index != 0:        
        a = str(index % 4)
        if a == '0':
            string = 'A' + string
        elif a == '1':
            string = 'C' + string
        elif a == '2':
            string = 'G' + string
        elif a == '3':
            string = 'T' + string
        index = (index-int(a)) // 4
    while len(string) < k:
        string = 'A'+ string
    return string

if __name__ == '__main__':
    print(NumberToPattern(5437, 8))