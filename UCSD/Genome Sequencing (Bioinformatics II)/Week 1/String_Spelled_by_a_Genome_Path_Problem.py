#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:51:51 2019

@author: jungangzou
"""

def string_spelled_by_a_genome_path_problem(k_mers_list):
    genome = ""
    for i in range(0, len(k_mers_list) - 1):
        genome += k_mers_list[i][0]
        if i == len(k_mers_list) - 2:#add last k_mers
            genome += k_mers_list[i + 1]
    return genome

if __name__ =='__main__':
    with open("dataset_198_3.txt",'r') as f:
        string = f.readlines()
        for i in range(len(string)):
            string[i] = string[i][:-1]
    with open("dataset_198_3_result.txt",'w') as g:
        g.write(string_spelled_by_a_genome_path_problem(string))
        
        
