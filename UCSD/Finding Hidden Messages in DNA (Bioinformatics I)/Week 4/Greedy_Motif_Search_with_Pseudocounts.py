#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:53:08 2019

@author: jungangzou
"""

import numpy as np
import math


def Hamming_Distance_Problem(string1,string2):
    hamming_distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamming_distance += 1
    return hamming_distance

def Profile_most_Probable_K_mer_Problem(string, k, matrix):
    max_probability = 0
    max_k_mer = string[:k]
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
        if probability > max_probability:
            max_probability = probability
            max_k_mer = pattern
    return max_k_mer


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


def Greedy_Motif_Search_with_Pseudocounts(Dna, k, t, pseudocount = 1):
    for i in range(len(Dna)):
        Dna[i] = list(Dna[i])
    best_k_mers = []
    for i in Dna:
        best_k_mers.append(i[:k])
    best_score = Scoring_Calculation(Profile_Matrix_with_Pseudocounts(best_k_mers, pseudocount), best_k_mers)
    for i in range(len(Dna[0]) - k + 1):
        pattern = Dna[0][i:i+k]
        k_mers = []
        k_mers.append(pattern)
        for j in range(1, t):
            pm = Profile_Matrix_with_Pseudocounts(k_mers, pseudocount)
            #print(pm)
            pattern = list(Profile_most_Probable_K_mer_Problem(Dna[j], k, pm))
            #print(pattern)
            k_mers.append(pattern)
        pm = Profile_Matrix_with_Pseudocounts(k_mers, pseudocount)
        sc = Scoring_Calculation(pm, k_mers)
        if sc < best_score:
            best_score = sc
            best_k_mers = k_mers
    for i in range(len(best_k_mers)):
        best_k_mers[i] = ''.join(best_k_mers[i])
    return best_k_mers



if __name__ == '__main__':
    with open("dataset_160_9.txt","r") as f:
        string = f.readlines()
        k, t = string[0][:-1].split(" ")
        
        print(string)
        k, t = int(k), int(t)
        dna = []
        for i in string[1:]:
            dna.append(i[:-1])
    


        a = Greedy_Motif_Search_with_Pseudocounts(dna, k, t)
        for i in a:
            print(i, end = " ")