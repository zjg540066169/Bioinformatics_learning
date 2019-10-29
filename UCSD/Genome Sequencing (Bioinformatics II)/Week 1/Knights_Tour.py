#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:02:10 2019

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
    
    
class knights_tour(object):
    def __init__(self):
        self.node_list = []
        self.node_num = 0
        self.ID_to_Index = {}
        self.Index_to_ID = {}

    def add_node(self, ID):
        if ID in self.ID_to_Index:
            raise Exception("there is the node with this ID")
        self.ID_to_Index[ID] = self.node_num
        self.Index_to_ID[self.node_num] = ID
        new_node = node(ID)
        self.node_list.append(new_node)
        self.node_num += 1
        
    
    def add_undirect_edge(self, start_ID, end_ID):
        start_index = self.ID_to_Index[start_ID]
        end_index = self.ID_to_Index[end_ID]
        self.node_list[start_index].add_new_edge(end_ID)
        self.node_list[end_index].add_new_edge(start_ID)

    
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

if __name__ == '__main__':
    g = knights_tour()
    for i in range(1, 13):
        g.add_node(i)
    g.add_undirect_edge(1, 6)
    g.add_undirect_edge(1, 7)
    g.add_undirect_edge(1, 9)
    g.add_undirect_edge(2, 10)
    g.add_undirect_edge(2, 8)
    g.add_undirect_edge(2, 3)
    g.add_undirect_edge(3, 9)
    g.add_undirect_edge(3, 11)
    g.add_undirect_edge(4, 10)
    g.add_undirect_edge(4, 12)
    g.add_undirect_edge(5, 7)
    g.add_undirect_edge(5, 11)
    g.add_undirect_edge(6, 8)
    g.add_undirect_edge(6, 12)
    g.add_undirect_edge(7, 12)
    g.add_undirect_edge(10, 11)
    #print(g.get_all_nodes_ID())
    g.depth_first_search_start()
    
    
