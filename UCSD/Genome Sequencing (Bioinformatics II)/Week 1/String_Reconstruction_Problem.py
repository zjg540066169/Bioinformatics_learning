#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:37:07 2019

@author: jungangzou
"""

from DeBruijn_Graph import debruijn_graph
from String_Spelled_by_a_Genome_Path_Problem import string_spelled_by_a_genome_path_problem

def string_reconstruction_problem(patterns, k):

    g = debruijn_graph()
    for i in patterns:
        g.add_direct_edge(i, k-1)
    return string_spelled_by_a_genome_path_problem(g.eulerian_path_search())
    
    
if __name__ == "__main__":
    with open("dataset_203_7.txt",'r') as f:
        string = f.readlines()
        k = int(string[0][:-1])
        pattern = string[1:]
        for i in range(len(pattern)):
            pattern[i] = pattern[i][:-1]
        print(string_reconstruction_problem(pattern, k))
