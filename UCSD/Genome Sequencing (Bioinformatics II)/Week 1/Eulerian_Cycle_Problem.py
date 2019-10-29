#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 07:47:11 2019

Input: The adjacency list of an Eulerian directed graph.
Output: An Eulerian cycle in this graph.


Randomly select a starting point S, randomly search for a path from S to S,
which forms a cycle.

while True:
    If there is no node has unused edges, then print the cycle.
    Else 
      randomly select a searched point T that has unused edges, use searched path
      to form a cycle first, from T to T. Then search from T by using another unused
      edge. To form a new cycle.

Optimization: When searched in a new point D, read all neghbors of D, choose the
point that has the most neighbors that has not searched as the next point.


O(n), n is the number of edge, since we can simply change the position of path array

@author: jungangzou
"""

from Hamiltonian_Graph import node

    
    
class debruijn_graph_eulerian_cycle(object):
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
        #self.fit_prefix(ID, k, self.direct)
        #self.fit_suffix(ID, k, self.direct)
        
        
    def add_direct_edge(self, start_ID, end_ID):
# =============================================================================
#         start_ID = edge_ID[:k]
#         end_ID = edge_ID[-k:]
# =============================================================================
        if start_ID not in self.ID_to_Index:
            self.add_node(start_ID)
        if end_ID not in self.ID_to_Index:
            self.add_node(end_ID)
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
            edge_dict[ID] = self.get_edge_by_node(ID).copy()
        return edge_dict

    def eulerian_cycle_search(self, start_id):
        remain_edges = self.get_all_edges()
        path_nodes_list = []
        start_point = start_id
        while True:
            #use old path to generate the beginning of the new path 
            if len(path_nodes_list) != 0: 
                path_nodes_list = path_nodes_list[:-1]
                for i in range(len(path_nodes_list)):
                    if path_nodes_list[i] == start_point:
                        path_nodes_list = path_nodes_list[i:] + path_nodes_list[:i]
            
            path_nodes_list.append(start_point)
            
            while len(remain_edges[start_point]) != 0: 
                next_point_select_point_set = remain_edges[start_point]
                
                #max_neighbor_node_id = next_point_select_point_set[0]
# =============================================================================
#                 next_point_select_index_set = []
#                 for ID in next_point_select_point_set:
#                     next_point_select_index_set.append(self.ID_to_Index[ID])
#                 
# =============================================================================
                max_neighbor = 0
                max_neighbor_node_id = remain_edges[start_point][0]
                for neighbor_index in range(len(next_point_select_point_set)):
                    if len(remain_edges[next_point_select_point_set[neighbor_index]]) > max_neighbor:
                        max_neighbor_node_id = next_point_select_point_set[neighbor_index]
                        max_neighbor = len(remain_edges[next_point_select_point_set[neighbor_index]])
                #print(start_point, max_neighbor_node_id, remain_edges[start_point])
                #max_neighbor_node_id = random.choice(next_point_select_point_set)
                remain_edges[start_point].remove(max_neighbor_node_id)
                path_nodes_list.append(max_neighbor_node_id)
                start_point = max_neighbor_node_id
            
            for node_id in path_nodes_list:
                if len(remain_edges[node_id]) != 0:
                    start_point = node_id
                    break
            else:
                return path_nodes_list
            
                

if __name__ == "__main__":
# =============================================================================
#     with open("dataset_200_8.txt", "r") as f:
#         string = f.readlines()
#         for i in range(len(string)):
#             string[i] = string[i][:-1]
# =============================================================================
    path_num = 0
    with open('dataset_203_2 09.26.00.txt', 'r') as file:
        graph = dict((line.strip().split(' -> ') for line in file))
        for key in graph:
            graph[key] = graph[key].split(',')
    g = debruijn_graph_eulerian_cycle()
    for i in graph:
        for j in graph[i]:
            path_num += 1
            g.add_direct_edge(i,j)
            
    
    
    path = g.eulerian_cycle_search(list(graph.keys())[3])
# =============================================================================
#     for i in range(len(path)):
#         if path[i] == "1140":
#             path = path[i:] + path[:i+1]
#             break
# =============================================================================
    a = "->".join(path)
    print(a)
# =============================================================================
#     with open("dataset_200_8_result.txt", "w") as w:
#         for pattern, adjacencies in g.get_all_edges().items():
#             if len(adjacencies) > 0:
#                 w.write(pattern + ' -> ' + str(', '.join(adjacencies)) + "\n")
# 
# =============================================================================
