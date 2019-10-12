#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:45:27 2019

@author: jungangzou
"""

from Greedy_Motif_Search_with_Pseudocounts import Scoring_Calculation, Profile_most_Probable_K_mer_Problem, Profile_Matrix_with_Pseudocounts
import random

random.seed(1)

def Randomized_Motif_Search(Dna, k, t):
    for i in range(len(Dna)):
        Dna[i] = list(Dna[i])
    best_k_mers = []
    for i in range(len(Dna)):
        position_select = random.choice(range(len(Dna[0]) - k + 1))
        best_k_mers.append(Dna[i][position_select : position_select + k])
    profile_matrix = Profile_Matrix_with_Pseudocounts(best_k_mers, 1)
    best_score = Scoring_Calculation(profile_matrix, best_k_mers)
    k_mers_last = best_k_mers
    while True:
        k_mers_current = []
        for i in range(len(Dna)):
            k_mers_current.append(Profile_most_Probable_K_mer_Problem(Dna[i], k, profile_matrix))
        profile_matrix = Profile_Matrix_with_Pseudocounts(k_mers_current, 1)
        
        
        k_mers_current_set = set()
        k_mers_last_set = set()
        for i in range(len(k_mers_current)):
            k_mers_current_set.add(''.join(k_mers_current[i]))
            k_mers_last_set.add(''.join(k_mers_last[i]))
        if k_mers_current_set.issubset(k_mers_last_set) and k_mers_last_set.issubset(k_mers_current_set):
            if Scoring_Calculation(profile_matrix, k_mers_current) < best_score:
                best_score = Scoring_Calculation(profile_matrix, k_mers_current)
                best_k_mers = k_mers_current
            for i in range(len(best_k_mers)):
                best_k_mers[i] = ''.join(best_k_mers[i])
            return best_k_mers, best_score
        k_mers_last = k_mers_current
        
def Randomized_Motif_Search_Multiple(Dna, k, t, times):
    best_k_mers, best_score = Randomized_Motif_Search(Dna, k, t)
    for i in range(times - 1):
        k_mers, score = Randomized_Motif_Search(Dna, k, t)
        if score < best_score:
            best_score = score
            best_k_mers = k_mers
    return best_k_mers
    
if __name__ == '__main__':
    with open("dataset_161_5-2.txt","r") as f:
        string = f.readlines()
        k, t = string[0][:-1].split(" ")
        
        print(string)
        k, t = int(k), int(t)
        dna = []
        for i in string[1:]:
            dna.append(i[:-1])
    


        a = Randomized_Motif_Search_Multiple(dna, k, t, 1000)
        for i in a:
            print(i, end = "\n")