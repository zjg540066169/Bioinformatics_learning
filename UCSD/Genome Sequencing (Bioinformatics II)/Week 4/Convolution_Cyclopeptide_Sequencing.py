#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:01:33 2019

@author: jungangzou
"""
from Leaderboard_Cyclopeptide_Sequencing import leaderboard_cyclopeptide_sequencing

def spectral_convolution(spectrum):
    convolution = []
    for i in range(len(spectrum)):
        for j in range(i, len(spectrum)):
            if spectrum[i] != spectrum[j]:
                convolution.append(spectrum[j] - spectrum[i])
    return convolution

def convolution_cyclopeptide_sequencing(M, N, experimental_spectrum):
    experimental_spectrum = sorted(experimental_spectrum)
    convolution = spectral_convolution(experimental_spectrum)
    
    convolution_dict = {}
    for i in convolution:
        convolution_dict[i] = convolution_dict.get(i, 0) + 1
        
    all_score = sorted(convolution_dict.items(), key = lambda item:item[1], reverse = True)
    all_score_temp = []
    for i in all_score:
            if i[0] >= 57 and i[0] <= 200:
                all_score_temp.append(i)
    all_score = all_score_temp
    for i in range(len(all_score)):
        #print(i)
        if i >= M and all_score[i][1] != all_score[i - 1][1]:
            leader_score = all_score[:i]
            break
    else:
        leader_score = all_score
    
    acid = []
    
   
    if len(leader_score) <= M:
        for i in leader_score:
            #if i[0] >= 57 and i[0] <= 200:
            acid.append(i[0])
    
    else:
        for i in leader_score:
            if i[1] >= leader_score[M][1]:
                acid.append(i[0])
            else:
                break
    print(acid)
    mass_table = {}
    for i in acid:
        mass_table[chr(i)] = int(i)
    
    return leaderboard_cyclopeptide_sequencing(N, mass_table, experimental_spectrum)

if __name__ == "__main__":
    
    
    with open("dataset_104_8.txt", "r") as f:
        string = f.readlines()
        M = int(string[0].replace("\n", ""))
        N = int(string[1].replace("\n", ""))
        es = string[2].replace("\n", "").split()
        for i in range(len(es)):
            es[i] = int(es[i])
    result = convolution_cyclopeptide_sequencing(M, N, es)
    for i in result:
        print(i, end = " ")