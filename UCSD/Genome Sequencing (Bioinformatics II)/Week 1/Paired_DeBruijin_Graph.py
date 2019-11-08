#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 07:50:17 2019

@author: jungangzou
"""
from DeBruijn_Graph import node_with_degree, debruijn_graph
from String_Spelled_by_a_Genome_Path_Problem import string_spelled_by_a_genome_path_problem
import numpy as np

class paired_debruijn_graph(debruijn_graph):
    def __init__(self):
        super().__init__()
        
        
    def add_direct_edge(self, edge_ID, k):
        paired_edge = edge_ID.split("|")
        start_ID = []
        end_ID = []
        for edge in paired_edge:
            #print(edge, end = ",")
            start_ID.append(edge[:k])
            end_ID.append(edge[-k:])
        print(paired_edge, k)
        print(start_ID, end_ID)
        
        start_ID = "|".join(start_ID)
        end_ID = "|".join(end_ID)
        #print(start_ID, end_ID)
        #print(edge_ID, start_ID, end_ID)
        if start_ID not in self.ID_to_Index:
            self.add_node(start_ID)
        if end_ID not in self.ID_to_Index:
            self.add_node(end_ID)
        start_index = self.ID_to_Index[start_ID]
        end_index = self.ID_to_Index[end_ID]
        self.node_list[start_index].add_new_edge(end_ID)
        self.node_list[start_index].set_out_degree(self.node_list[start_index].get_out_degree()+1)
        self.node_list[end_index].set_in_degree(self.node_list[end_index].get_in_degree()+1)
    
    def string_reconstruction_paired(self, path, k, d): 
        
        for i in range(len(path)):
            path[i] =  path[i].split("|")   
        
        string_list = np.array(path).T.tolist()
        #print(string_list)
        genome_list = []
        for string in string_list:
            genome_list.append(string_spelled_by_a_genome_path_problem(string))
        #print(genome_list)
        complete_genome = ""
        #print(genome_list)
        if genome_list[0][k+d+1:] == genome_list[1][:-(1+k+d)]:
            #print(genome_list[0][k+d:], genome_list[1][:k+d])
            complete_genome = genome_list[0][:k+d+1] + genome_list[1]
            return complete_genome
        else:
            return "there is no string spelled by the gapped patterns"
    
            
        
        
    
if __name__ == "__main__":
    
    with open("dataset_204_16.txt", "r") as f:
        string = f.readlines()
        for i in range(len(string)):
            string[i] = string[i].replace("\n", "").replace("(","").replace(")","")
        while "" in string:
            string.remove("")
        
            

    g = paired_debruijn_graph()
    for i in range(len(string)):
        
        k_mer = string[i]
        #print(k_mer)
        g.add_direct_edge(k_mer, 3 - 1)
    path = g.eulerian_path_search()
    print(g.string_reconstruction_paired(path, 2, 1))

    
    #print(g.string_reconstruction_paired(g.eulerian_path_search(), k-1, d))
    
    
    
    
    