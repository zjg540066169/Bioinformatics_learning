#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:18:28 2019

@author: jungangzou
"""

from K_Universal_String import k_universal_mers

class node(object):
    def __init__(self, ID):
        #self.attribute = attribute
        self.ID = ID
        self.edge = []
    
    def add_new_edge(self, ID):
        self.edge.append(ID)
    
    def get_ID(self):
        return self.ID
    
    def get_edge(self):
        return self.edge
    
class Number_of_KUC(object):
    def __init__(self):
        self.node_list = []
        self.node_num = 0
        self.ID_to_Index = {}
        self.Index_to_ID = {}

    def add_node(self, ID, k):
        if ID in self.ID_to_Index:
            raise Exception("there is the node with this ID")
        self.ID_to_Index[ID] = self.node_num
        self.Index_to_ID[self.node_num] = ID
        new_node = node(ID)
        self.node_list.append(new_node)
        self.node_num += 1
        self.fit_prefix(ID, k)
        self.fit_suffix(ID, k)
        
    
    def add_undirect_edge(self, start_ID, end_ID):
        start_index = self.ID_to_Index[start_ID]
        end_index = self.ID_to_Index[end_ID]
        self.node_list[start_index].add_new_edge(end_ID)
        self.node_list[end_index].add_new_edge(start_ID)
        
    def add_direct_edge(self, start_ID, end_ID):
        start_index = self.ID_to_Index[start_ID]
        self.node_list[start_index].add_new_edge(end_ID)

    
    def get_node_by_id(self, node_id):
        index = self.ID_to_Index[node_id]
        return self.node_list[index]

    def get_edge_by_node(self, node_id):
        index = self.ID_to_Index[node_id]
        return self.node_list[index].get_edge()
    
    
    def get_all_nodes_ID(self):
        ID = []
        for i in self.node_list:
            ID.append(i.get_ID())
        return ID
    
    def get_all_edges(self):
        edge_dict = {}
        ID_list = self.get_all_nodes_ID()
        for ID in ID_list:
            edge_dict[ID] = self.get_edge_by_node(ID)
        return edge_dict
    
    
    def fit_prefix(self, node_ID, k, direct = True):
        #use this node_id`s first k character to fit other node_id`s last k character
        prefix = node_ID[:k]
        for i in self.node_list:
            node_list_id = i.get_ID()
           # if node_ID == node_list_id:
           #     continue
            suffix = node_list_id[-k:]
            if suffix == prefix:
                if direct:
                    self.add_direct_edge(node_list_id, node_ID)
                else:
                    self.add_undirect_edge(node_list_id, node_ID)

    def fit_suffix(self, node_ID, k, direct = True):
        #use this node_id`s last k character to fit other node_id`s first k character
        suffix = node_ID[-k:]
        for i in self.node_list:
            node_list_id = i.get_ID()
            #if node_ID == node_list_id:
            #    continue
            prefix = node_list_id[:k]
            if suffix == prefix:
                if direct:
                    self.add_direct_edge(node_ID, node_list_id)
                else:
                    self.add_undirect_edge(node_ID, node_list_id) 

    
    def depth_first_search_start(self):
        searched = [False for i in range(len(self.node_list))]
        self.num_path = 0
        self.path = []
        for ID in [6, 9, 7]:
            #ID = self.Index_to_ID[i]
            node_order, num = self.__depth_first_search(ID, searched.copy(), 0, [])
            
            #print(num, node_order)
            #if num == len(self.node_list):
            #    print(i, node_order)
    
    def __depth_first_search(self, ID, searched, num, node_order):
        #searched denote an array of boolean that this index of node is searched
        #print(ID,"->", end = "")
        if ID == 1 and num != len(self.node_list) - 1 :
            return node_order, num
        node = self.get_node_by_id(ID)
        index = self.ID_to_Index[ID]
        if searched[index]:
            return node_order, num
        node_order.append(ID)
        num += 1
        searched[index] = True
        edge = node.get_edge()
        #print(ID, edge)
        if len(edge) == 0:
            return node_order, num
        else:
            #if the node has neighbors, then use recursive function to find next node.
            #We count the number of node in node_order and return the maximum of num and its node_order
            max_num = 0
            max_node_order = []
            
            for neighbor in edge:
                #print(ID, "->", neighbor, end = " | ")
                node_order_new, num_new = self.__depth_first_search(neighbor, searched.copy(), num, node_order.copy())
                #print(node_order_new, num_new)
                if num_new >= max_num:
                    max_num = num_new
                    max_node_order = node_order_new
                #print(num_new, len(self.node_list), end = " | ")
                if num_new == len(self.node_list):
                    
                    #print(self.num_path, node_order_new)
                    if str(node_order_new) not in self.path:
                        print(str(node_order_new))
                        self.num_path += 1
                        self.path.append(str(node_order_new))
                #print()
            return max_node_order, max_num
        
def number_of_k_universal_circular_string(k):
    g = Number_of_KUC()
    k_mers = k_universal_mers(k)
    for i in k_mers:
        g.add_node(i, k)

    k_universal_string_list = g.eulerian_cycle_search(i[:k-1])
    print(k_universal_string_list)
    return circle_string_spelled_by_a_genome_path_problem(k_universal_string_list)
        
        
if __name__ =="__main__":

