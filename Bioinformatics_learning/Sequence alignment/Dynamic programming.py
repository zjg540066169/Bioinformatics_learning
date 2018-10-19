# -*- coding: utf-8 -*-
"""
Created on Sun May 20 16:11:50 2018

@author: wang
"""

import numpy as np
import pandas as pd



score_matrix = pd.DataFrame(
        np.array([
                [2,-7,-5,-7],
                [-7,2,-7,-5],
                [-5,-7,2,-7],
                [-7.-5,-7,2]
                ]),
        index = ['A','C','G','T'],
        columns = ['A','C','G','T']
        )

open_gap = extending_gap = -5



def SeqAlign(matrix,i,j,str1,str2):
    if i ==0 and j == 0:
        return max(matrix[0][0],0)
    else:
        s = score_matrix.loc[str1[i],str2[j]]
        a1 = max()



if __name__ == '__main__':
    