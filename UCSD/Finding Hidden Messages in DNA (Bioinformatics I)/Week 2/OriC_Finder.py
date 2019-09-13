#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:58:32 2019

@author: jungangzou
"""

from Skew_Count import Skew_Count
from Frequent_Words_With_Mismatches_And_Reverse_Complements_Problem import Frequent_Words_With_Mismatches_And_Reverse_Complements_Problem
import numpy as np
import matplotlib.pyplot as plt

def OriC_Finder(DNA_string, interval, k, d):
    skew_result = Skew_Count(DNA_string)
    mini_place =  skew_result.index(min(skew_result))
# =============================================================================
#     plt.plot(np.arange(len(skew_result)),skew_result)
#     plt.show()
# =============================================================================
    oriC_interval = DNA_string[mini_place - interval: mini_place + interval]
    #print(oriC_interval)
    return Frequent_Words_With_Mismatches_And_Reverse_Complements_Problem(oriC_interval,k,d)



if __name__ == '__main__':
    with open('Salmonella_enterica.txt','r') as f:
        string = f.readlines()
        DNA_string = ""
        for i in string:
            DNA_string += i[:-1]
        print(OriC_Finder(DNA_string,500,9,1))
        
        