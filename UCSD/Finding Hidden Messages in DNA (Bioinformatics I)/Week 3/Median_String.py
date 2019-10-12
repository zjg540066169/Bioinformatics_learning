#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:37:13 2019

@author: jungangzou
"""





def Hamming_Distance_Problem(string1,string2):
    hamming_distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamming_distance += 1
    return hamming_distance


def Hamming_distance_string(pattern, string):
    min_distance = 99999999
    for i in range(len(string) - len(pattern) + 1):
        string_pattern = string[i:i+len(pattern)]
        hd = Hamming_Distance_Problem(pattern, string_pattern)
        if hd < min_distance:
            min_distance = hd
    return min_distance


def K_mers_generate(k):
    K_mers = ["A","T","C","G"]
    for i in range(k - 1):
        new_K_mers = []
        for j in K_mers:
            new_K_mers.append(j+"A")
            new_K_mers.append(j+"T")
            new_K_mers.append(j+"C")
            new_K_mers.append(j+"G")
        K_mers = new_K_mers
    return K_mers


        
def Median_String(k, Dna_List):
    k_mers_list = K_mers_generate(k)
    k_mer_min = []
    k_mer_hd_min = 999999999
    for k_mer in k_mers_list:
        hamming_distance_total = 0
        for dna in Dna_List:
            hamming_distance_total += Hamming_distance_string(k_mer, dna)
        if hamming_distance_total < k_mer_hd_min:
            k_mer_hd_min = hamming_distance_total
            k_mer_min = [k_mer]
        elif hamming_distance_total == k_mer_hd_min:
            k_mer_hd_min = hamming_distance_total
            k_mer_min.append(k_mer)
    return k_mer_min
        





if __name__ == '__main__':
    #with open("dataset_158_9.txt", 'r') as f:
        #string = f.readlines()
        #k = int(string[0][:-1])
        dna = [
               'CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',

'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',

'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG'

 
                ]
        #for i in string[1:]:
        #    dna.append(i[:-1])
        print(Median_String(7, dna))