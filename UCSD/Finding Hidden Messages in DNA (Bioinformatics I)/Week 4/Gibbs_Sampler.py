#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:54:48 2019

@author: jungangzou
"""

import numpy as np
import math
import random

def Hamming_Distance_Problem(string1,string2):
    hamming_distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamming_distance += 1
    return hamming_distance

def Profile_Probability_Problem_Gibbs_Sampler(string, k, matrix):
    probability_list = []
    A = matrix[0]
    T = matrix[3]
    C = matrix[1]
    G = matrix[2]
    for i in range(len(string) - k + 1):
        pattern = string[i:i+k]
        probability = 1
        for character in range(len(pattern)):
            if pattern[character] == 'A':
                probability *= A[character]
            elif pattern[character] == 'T':
                probability *= T[character]
            elif pattern[character] == 'C':
                probability *= C[character]
            elif pattern[character] == 'G':
                probability *= G[character]   
        probability_list.append(probability)
    probability_list = np.array(probability_list)/np.array(probability_list).sum()
    #print(np.array(probability_list).sum())
    start_point = random.choices(range(len(probability_list)), weights = probability_list.tolist())[0]
    return string[start_point : start_point+k]


def Profile_Matrix_with_Pseudocounts(k_mers, pseudocount = 1):
    k_mers_matrix = np.array(k_mers)
    profile_matrix = np.zeros((4, k_mers_matrix.shape[1]))
    for i in range(k_mers_matrix.shape[1]):
        for j in range(k_mers_matrix.shape[0]):
            if k_mers_matrix[j][i] == 'A':
                profile_matrix[0][i] += 1
            elif k_mers_matrix[j][i] == 'C':
                profile_matrix[1][i] += 1
            elif k_mers_matrix[j][i] == 'G':
                profile_matrix[2][i] += 1
            elif k_mers_matrix[j][i] == 'T':
                profile_matrix[3][i] += 1
    profile_matrix += 1
    profile_matrix /= profile_matrix[:,:].sum(0)
    return profile_matrix
                


def Scoring_Calculation(profile_matrix, k_mers = None, entropy = False):
    similarity = 0
    if entropy:
        information_entropy = 0
        for i in range(4):
            information_entropy_column = 0
            for j in range(profile_matrix.shape[1]):
                if profile_matrix[i][j] == 0:
                    continue
                if entropy:
                    information_entropy_column += - profile_matrix[i][j] * math.log2(profile_matrix[i][j])
                
            information_entropy += information_entropy_column
        similarity = information_entropy
        
    else:#use hamming distance
        if k_mers == None:
            raise Exception("k_mers_matrix need to calculate the hamming distance")
        motif = ""
        for i in range(profile_matrix.shape[1]):
            nucleartide = np.argmax(profile_matrix[:,i])
            if nucleartide == 0:
                motif += "A"
            elif nucleartide == 1:
                motif += "C"
            elif nucleartide == 2:
                motif += "G"
            elif nucleartide == 3:
                motif += "T"
        hamming_distance = 0
        for i in k_mers:
            hamming_distance += Hamming_Distance_Problem(''.join(i), motif)
        similarity = hamming_distance
    return similarity





def Gibbs_Sampler(Dna, k, t, N, pseudocount = 1):
    for i in range(len(Dna)):
        Dna[i] = list(Dna[i])
    best_k_mers = []
    for i in range(len(Dna)):
        position_select = random.choice(range(len(Dna[0]) - k + 1))
        best_k_mers.append(Dna[i][position_select : position_select + k])
    profile_matrix = Profile_Matrix_with_Pseudocounts(best_k_mers, 1)
    best_score = Scoring_Calculation(profile_matrix, best_k_mers)
    k_mers_last = best_k_mers
    for n in range(N):
        delete_string_index = random.choice(range(len(k_mers_last)))
        profile_matrix = Profile_Matrix_with_Pseudocounts(k_mers_last[:delete_string_index] + k_mers_last[delete_string_index + 1:], 1)
        k_mers_last[delete_string_index] = Profile_Probability_Problem_Gibbs_Sampler(Dna[delete_string_index], k, profile_matrix)
        
        if Scoring_Calculation(profile_matrix, k_mers_last) < best_score:
            best_score = Scoring_Calculation(profile_matrix, k_mers_last)
            best_k_mers = k_mers_last
    for i in range(len(best_k_mers)):
        best_k_mers[i] = ''.join(best_k_mers[i])
    return best_k_mers, best_score

def Gibbs_Sampler_Multiple(Dna, k, t, N, times):
    best_k_mers, best_score = Gibbs_Sampler(Dna, k, t, N)
    for i in range(times - 1):
        k_mers, score = Gibbs_Sampler(Dna, k, t, N)
        if score < best_score:
            best_score = score
            best_k_mers = k_mers
    return best_k_mers

if __name__ == '__main__':
    with open("dataset_163_4.txt","r") as f:
        string = f.readlines()
        k, t, N = string[0][:-1].split(" ")
        
        print(string)
        k, t, N = int(k), int(t), int(N)
        dna = []
        for i in string[1:]:
            dna.append(i[:-1])
    


        a = Gibbs_Sampler_Multiple(dna, k, t, N, 20)
        for i in a:
            print(i, end = "\n")