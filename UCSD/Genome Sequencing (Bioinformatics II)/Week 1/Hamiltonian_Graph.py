#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:07:57 2019

@author: jungangzou
"""



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
    
    
class hamiltonian_graph(object):
    def __init__(self, direct):
        self.node_list = []
        self.node_num = 0
        self.ID_to_Index = {}
        self.Index_to_ID = {}
        if direct == "direct":
            self.direct = True
        elif direct == "undirect":
            self.direct = False
        else:
            self.direct = direct
        
        
    def add_node(self, ID, k):
        if ID in self.ID_to_Index:
            raise Exception("there is the node with this ID")
        self.ID_to_Index[ID] = self.node_num
        self.Index_to_ID[self.node_num] = ID
        new_node = node(ID)
        self.node_list.append(new_node)
        self.node_num += 1
        self.fit_prefix(ID, k, self.direct)
        self.fit_suffix(ID, k, self.direct)
        
    
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
    
    def fit_prefix(self, node_ID, k, direct = False):
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

    def fit_suffix(self, node_ID, k, direct = False):
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
    
    def depth_first_search_start(self):
        searched = [False for i in range(len(self.node_list))]
        for i in range(len(self.node_list)): 
            ID = self.Index_to_ID[i]
            node_order, num = self.__depth_first_search(ID, searched.copy(), 0, [])
            #print(num, node_order)
            if num == len(self.node_list):
                return node_order
            
    def __depth_first_search(self, ID, searched, num, node_order):
        #searched denote an array of boolean that this index of node is searched
        #print(ID,"->", end = "")
        node = self.get_node_by_id(ID)
        index = self.ID_to_Index[ID]
        if searched[index]:
            #print("[]")
            return node_order, num

        node_order.append(ID)
        num += 1
        searched[index] = True
        edge = node.get_edge()
        #print(','.join(edge))
        if len(edge) == 0:
            return node_order, num
        
        else:
            #if the node has neighbors, then use recursive function to find next node.
            #We count the number of node in node_order and return the maximum of num and its node_order
            max_num = 0
            max_node_order = []
            for neighbor in edge:
                node_order_new, num_new = self.__depth_first_search(neighbor, searched, num, node_order)
                if num_new >= max_num:
                    max_num = num_new
                    max_node_order = node_order_new
            return max_node_order, max_num
            
        
    
            
    
if __name__ == "__main__":
    with open("dataset_198_10 16.30.17.txt", "r") as f:
        string = f.readlines()
        ID = []
        for i in string:
            ID.append(i[:-1])
    g = hamiltonian_graph("direct")
    for i in ID:
        g.add_node(i, len(i) - 1)
    edges = g.get_all_edges()
    with open("dataset_198_10_result.txt", "w") as w:
        for pattern, adjacencies in g.get_all_edges().items():
            if len(adjacencies) > 0:
                w.write(pattern + '->' + str(','.join(adjacencies)) + "\n")
    