#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:40:37 2019

@author: jungangzou
"""
from Hamiltonian_Graph import hamiltonian_graph
from String_Spelled_by_a_Genome_Path_Problem import string_spelled_by_a_genome_path_problem

def k_universal_mers(k):
    if k == 1:
        return ["0" , "1"]
    else:
        k_minus_1_mers =  k_universal_mers(k - 1)
        k_mers = []
        for i in k_minus_1_mers:
            k_mers.append("0" + i)
            k_mers.append("1" + i)
        return k_mers
            
        

def k_universal_string(k):
    g = hamiltonian_graph("directed")
    k_mers = k_universal_mers(k)
    for i in k_mers:
        g.add_node(i, len(i) - 1)
    k_universal_string_list = g.depth_first_search_start()
    return string_spelled_by_a_genome_path_problem(k_universal_string_list)

if __name__ == '__main__':
    print(k_universal_string(10))