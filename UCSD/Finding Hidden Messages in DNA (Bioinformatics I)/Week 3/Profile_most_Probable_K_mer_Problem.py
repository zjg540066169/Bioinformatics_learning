#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:23:19 2019

@author: jungangzou
"""


def Profile_most_Probable_K_mer_Problem(string, k, matrix):
    max_probability = 0
    max_k_mer = ""
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

if __name__ == '__main__':
    with open("dataset_159_3 13.42.43.txt","r") as f:
        string = f.readlines()
        print(string)
        dna = string[0][:-1]
        k = int(string[1][:-1])
        matrix = []
        for i in range(2, len(string)):
            row = string[i][:-1].split()
            for j in range(len(row)):
                row[j] = float(row[j])
            matrix.append(row)
        print(Profile_most_Probable_K_mer_Problem(dna, k, matrix))
        