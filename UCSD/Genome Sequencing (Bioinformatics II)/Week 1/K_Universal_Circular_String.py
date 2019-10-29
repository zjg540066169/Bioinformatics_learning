#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:46:28 2019

@author: jungangzou
"""

from DeBruijn_Graph import debruijn_graph
from K_Universal_String import k_universal_mers


def circle_string_spelled_by_a_genome_path_problem(k_mers_list):
    genome = ""
    for i in range(len(k_mers_list)):
        genome += k_mers_list[i][0]
    return genome

def k_universal_circular_string(k):
    g = debruijn_graph()
    k_mers = k_universal_mers(k)
    for i in k_mers:
        g.add_direct_edge(i, k - 1)

    k_universal_string_list = g.eulerian_cycle_search(i[:k-1])[1:]
    #print(k_universal_string_list)
    return circle_string_spelled_by_a_genome_path_problem(k_universal_string_list)




if __name__ == "__main__":
    a = k_universal_circular_string(9)