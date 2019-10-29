#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:33:04 2019

@author: jungangzou
"""

from Hamiltonian_Graph import node


class node_with_degree(node):
    def __init__(self, ID):
        super().__init__(ID)
        #self.attribute = attribute
        self.ID = ID
        self.edge = []
        self.out_degree = 0
        self.in_degree = 0
    
    
    def get_out_degree(self):
        return self.out_degree
    
    def get_in_degree(self):
        return self.in_degree
    
    def set_out_degree(self, out_degree):
        self.out_degree = out_degree
        
    def set_in_degree(self, in_degree):
        self.in_degree = in_degree


class debruijn_graph_eulerian_path(object):
    def __init__(self):
        self.node_with_degree_list = []
        self.node_with_degree_num = 0
        self.ID_to_Index = {}
        self.Index_to_ID = {}
       
        
    def add_node_with_degree(self, ID):
        if ID in self.ID_to_Index:
            raise Exception("there is the node_with_degree with this ID")
        self.ID_to_Index[ID] = self.node_with_degree_num
        self.Index_to_ID[self.node_with_degree_num] = ID
        new_node_with_degree = node_with_degree(ID)
        self.node_with_degree_list.append(new_node_with_degree)
        self.node_with_degree_num += 1
        #self.fit_prefix(ID, k, self.direct)
        #self.fit_suffix(ID, k, self.direct)
        
        
    def add_direct_edge(self, start_ID, end_ID):
# =============================================================================
#         start_ID = edge_ID[:k]
#         end_ID = edge_ID[-k:]
# =============================================================================
        if start_ID not in self.ID_to_Index:
            self.add_node_with_degree(start_ID)
        if end_ID not in self.ID_to_Index:
            self.add_node_with_degree(end_ID)
        start_index = self.ID_to_Index[start_ID]
        end_index = self.ID_to_Index[end_ID]
        self.node_with_degree_list[start_index].add_new_edge(end_ID)
        
        self.node_with_degree_list[start_index].set_out_degree(self.node_with_degree_list[start_index].get_out_degree()+1)
        self.node_with_degree_list[end_index].set_in_degree(self.node_with_degree_list[end_index].get_in_degree()+1)

    
    def get_node_with_degree_by_id(self, node_with_degree_id):
        index = self.ID_to_Index[node_with_degree_id]
        return self.node_with_degree_list[index]

    def get_edge_by_node_with_degree(self, node_with_degree_id):
        index = self.ID_to_Index[node_with_degree_id]
        return self.node_with_degree_list[index].get_edge()
        
    def get_all_node_with_degrees_ID(self):
        ID = []
        for i in self.node_with_degree_list:
            ID.append(i.get_ID())
        return ID
    
    def get_all_edges(self):
        edge_dict = {}
        ID_list = self.get_all_node_with_degrees_ID()
        for ID in ID_list:
            edge_dict[ID] = self.get_edge_by_node_with_degree(ID).copy()
        return edge_dict

    def eulerian_path_search(self):
        for i in self.node_with_degree_list:
           # print(i.get_ID(),"in_degree",i.get_in_degree(), end = " | ")
           # print(i.get_ID(),"end_degree",i.get_out_degree())
            if i.get_in_degree() - i.get_out_degree() == -1:
                #print(i.get_ID(),"in_degree",i.get_in_degree)
                init_point = i.get_ID()
            if i.get_in_degree() - i.get_out_degree() == 1:
                #print(i.get_ID(),"end_degree",i.get_end_degree)
                end_point = i.get_ID()
        
        
        remain_edges = self.get_all_edges()
        remain_edges[end_point].append(init_point)
        path_node_with_degrees_list = []
        start_point = init_point
        while True:
            #use old path to generate the beginning of the new path 
            if len(path_node_with_degrees_list) != 0: 
                path_node_with_degrees_list = path_node_with_degrees_list[:-1]
                for i in range(len(path_node_with_degrees_list)):
                    if path_node_with_degrees_list[i] == start_point:
                        path_node_with_degrees_list = path_node_with_degrees_list[i:] + path_node_with_degrees_list[:i]
            
            path_node_with_degrees_list.append(start_point)
            while len(remain_edges[start_point]) != 0: 
                next_point_select_point_set = remain_edges[start_point]
                #max_neighbor_node_with_degree_id = next_point_select_point_set[0]
# =============================================================================
#                 next_point_select_index_set = []
#                 for ID in next_point_select_point_set:
#                     next_point_select_index_set.append(self.ID_to_Index[ID])
#                 
# =============================================================================
                max_neighbor = 0
                max_neighbor_node_with_degree_id = remain_edges[start_point][0]
                for neighbor_index in range(len(next_point_select_point_set)):
                    if len(remain_edges[next_point_select_point_set[neighbor_index]]) > max_neighbor:
                        max_neighbor_node_with_degree_id = next_point_select_point_set[neighbor_index]
                        max_neighbor = len(remain_edges[next_point_select_point_set[neighbor_index]])
                #print(start_point, max_neighbor_node_with_degree_id, remain_edges[start_point])
                #max_neighbor_node_with_degree_id = random.choice(next_point_select_point_set)
                remain_edges[start_point].remove(max_neighbor_node_with_degree_id)
                path_node_with_degrees_list.append(max_neighbor_node_with_degree_id)
                start_point = max_neighbor_node_with_degree_id
            
            for node_with_degree_id in path_node_with_degrees_list:
                if len(remain_edges[node_with_degree_id]) != 0:
                    start_point = node_with_degree_id
                    break
            else:
                #print(path_node_with_degrees_list, init_point, end_point)
                path_node_with_degrees_list = path_node_with_degrees_list[1:]
                #print(path_node_with_degrees_list, init_point, end_point)
                for i in range(len(path_node_with_degrees_list) - 1):
                    if path_node_with_degrees_list[i] == end_point and path_node_with_degrees_list[i+1] == init_point:
                        path_node_with_degrees_list = path_node_with_degrees_list[i+1:] + path_node_with_degrees_list[:i+1]
                        return path_node_with_degrees_list
            

if __name__ == "__main__":
# =============================================================================
#     with open("dataset_200_8.txt", "r") as f:
#         string = f.readlines()
#         for i in range(len(string)):
#             string[i] = string[i][:-1]
# =============================================================================
    path_num = 0
    with open('dataset_203_6 11.28.08.txt', 'r') as file:
        graph = dict((line.strip().split(' -> ') for line in file))
        for key in graph:
            graph[key] = graph[key].split(',')
    g = debruijn_graph_eulerian_path()
    for i in graph:
        for j in graph[i]:
            path_num += 1
            g.add_direct_edge(i,j)
            
    
    
    path = g.eulerian_path_search()
# =============================================================================
#     for i in range(len(path)):
#         if path[i] == "1140":
#             path = path[i:] + path[:i+1]
#             break
# =============================================================================
    a = "->".join(path)
    print(a)

