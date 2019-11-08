#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:01:07 2019

@author: jungangzou
"""
from Hamiltonian_Graph import node
from String_Spelled_by_a_Genome_Path_Problem import string_spelled_by_a_genome_path_problem

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
        
        
    
class debruijn_graph(object):
    def __init__(self):
        self.node_list = []
        self.node_num = 0
        self.ID_to_Index = {}
        self.Index_to_ID = {}
       
    def get_all_in_degree(self):
        in_degree_dict = {}
        ID_list = self.get_all_nodes_ID()
        for ID in ID_list:
            #print(self.get_edge_by_node(ID))
            in_degree_dict[ID] = self.get_node_by_id(ID).get_in_degree()
        return in_degree_dict.copy()
     
    def get_all_out_degree(self):
        out_degree_dict = {}
        ID_list = self.get_all_nodes_ID()
        for ID in ID_list:
            #print(self.get_edge_by_node(ID))
            out_degree_dict[ID] = self.get_node_by_id(ID).get_out_degree()
        return out_degree_dict.copy()

        
    def add_node(self, ID):
        if ID in self.ID_to_Index:
            raise Exception("there is the node with this ID")
        self.ID_to_Index[ID] = self.node_num
        self.Index_to_ID[self.node_num] = ID
        new_node = node_with_degree(ID)
        self.node_list.append(new_node)
        self.node_num += 1
        #self.fit_prefix(ID, k, self.direct)
        #self.fit_suffix(ID, k, self.direct)
        
        
    def add_direct_edge(self, edge_ID, k):
        start_ID = edge_ID[:k]
        end_ID = edge_ID[-k:]
        if start_ID not in self.ID_to_Index:
            self.add_node(start_ID)
        if end_ID not in self.ID_to_Index:
            self.add_node(end_ID)
        start_index = self.ID_to_Index[start_ID]
        end_index = self.ID_to_Index[end_ID]
        self.node_list[start_index].add_new_edge(end_ID)
        self.node_list[start_index].set_out_degree(self.node_list[start_index].get_out_degree()+1)
        self.node_list[end_index].set_in_degree(self.node_list[end_index].get_in_degree()+1)
    
    def add_direct_edge_by_nodes(self, start_ID, end_ID):
        if start_ID not in self.ID_to_Index:
            self.add_node(start_ID)
        if end_ID not in self.ID_to_Index:
            self.add_node(end_ID)
        start_index = self.ID_to_Index[start_ID]
        end_index = self.ID_to_Index[end_ID]
        self.node_list[start_index].add_new_edge(end_ID)
        
        self.node_list[start_index].set_out_degree(self.node_list[start_index].get_out_degree()+1)
        self.node_list[end_index].set_in_degree(self.node_list[end_index].get_in_degree()+1)
    
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
            #print(self.get_edge_by_node(ID))
            edge_dict[ID] = self.get_edge_by_node(ID).copy()
        return edge_dict.copy()
    
    def depth_first_search_edge_start(self):
        searched = [False for i in range(len(self.node_list))]
        for i in range(len(self.node_list)): 
            ID = self.Index_to_ID[i]
            node_order, num = self.__depth_first_search(ID, searched.copy(), 0, [])
            #print(num, node_order)
            if num == len(self.node_list):
                return node_order
            
    def __depth_first_search_edge(self, ID, searched, num, node_order):
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
        
        
        
    def eulerian_path_search(self):
        for i in self.node_list:
           # print(i.get_ID(),"in_degree",i.get_in_degree(), end = " | ")
           # print(i.get_ID(),"end_degree",i.get_out_degree())
            if i.get_in_degree() == 0 and i.get_in_degree() - i.get_out_degree() == -1:
                #print(i.get_ID(),"in_degree",i.get_in_degree)
                init_point = i.get_ID()
            if i.get_out_degree() == 0 and i.get_in_degree() - i.get_out_degree() == 1:
                #print(i.get_ID(),"end_degree",i.get_end_degree)
                end_point = i.get_ID()
        print(init_point, end_point)
        remain_edges = self.get_all_edges().copy()
        remain_edges[end_point].append(init_point)
        path_node_list = []
        start_point = init_point
        while True:
            #use old path to generate the beginning of the new path 
            if len(path_node_list) != 0: 
                path_node_list = path_node_list[:-1]
                for i in range(len(path_node_list)):
                    if path_node_list[i] == start_point:
                        path_node_list = path_node_list[i:] + path_node_list[:i]
            
           
            path_node_list.append(start_point)
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
                max_neighbor_node_id = remain_edges[start_point][0]
                for neighbor_index in range(len(next_point_select_point_set)):
                    if len(remain_edges[next_point_select_point_set[neighbor_index]]) > max_neighbor:
                        max_neighbor_node_id = next_point_select_point_set[neighbor_index]
                        max_neighbor = len(remain_edges[next_point_select_point_set[neighbor_index]])
                #print(start_point, max_neighbor_node_with_degree_id, remain_edges[start_point])
                #max_neighbor_node_with_degree_id = random.choice(next_point_select_point_set)
                remain_edges[start_point].remove(max_neighbor_node_id)
                path_node_list.append(max_neighbor_node_id)
                start_point = max_neighbor_node_id
            
            for node_id in path_node_list:
                if len(remain_edges[node_id]) != 0:
                    start_point = node_id
                    break
            else:
                #print(path_node_with_degrees_list, init_point, end_point)
                path_node_list = path_node_list[1:]
                #print(path_node_with_degrees_list, init_point, end_point)
                for i in range(len(path_node_list) - 1):
                    if path_node_list[i] == end_point and path_node_list[i+1] == init_point:
                        path_node_list = path_node_list[i+1:] + path_node_list[:i+1]
                        #print(self.get_all_edges())
                        return path_node_list
                    
                    
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
                #print(remain_edges)
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
            
    def maximal_non_branching_paths_search_start(self):
        mnb_paths = []

        remain_edges = self.get_all_edges().copy()
        #mnb_paths += self.__maximal_non_branching_paths_search(init_point, remain_edges)
        in_degree = self.get_all_in_degree().copy()
        for i in self.get_all_nodes_ID():
            while i in remain_edges[i]: 
                
                mnb_paths.append([i, i])
                in_degree[i] -= 1
                remain_edges[i].remove(i)
            #print(in_degree[i], len(remain_edges[i]))
            if len(remain_edges[i]) != 1 or in_degree[i] != 1:
                
                if len(remain_edges[i]) > 0:
                    mnb_paths += self.__maximal_non_branching_paths_search(i, remain_edges, in_degree)
        for i in self.get_all_nodes_ID():
            if len(remain_edges[i]) > 0:
                    mnb_paths += self.__maximal_non_branching_paths_search(i, remain_edges, in_degree)
        while [] in mnb_paths:
            mnb_paths.remove([])
        return mnb_paths
        #in_degree = self.get_all_in_degree()
        #out_degree = self.get_all_out_degree()
        
    def __maximal_non_branching_paths_search(self, start_point, remain_edges, in_degree):#, in_degree, out_degree):
        path_list = []
        if len(remain_edges[start_point]) == 0: 
            return []
        while len(remain_edges[start_point]) > 0:
            path = [start_point]
            current_path_point = start_point
            next_path_point = remain_edges[start_point][0]
            #print(next_path_point, remain_edges[next_path_point])
            while len(remain_edges[next_path_point]) == 1 and in_degree[next_path_point] == 1:
                if start_point == "13" and next_path_point == "27":
                    print(remain_edges[next_path_point])
                in_degree[next_path_point] -= 1
                #print(current_path_point, end = " ")
                #print(next_path_point)
                path.append(next_path_point)
                remain_edges[current_path_point].remove(next_path_point)
                temp_point = next_path_point
                next_path_point = remain_edges[next_path_point][0]
                current_path_point = temp_point
                
            in_degree[next_path_point] -= 1
            path.append(next_path_point)
            remain_edges[current_path_point].remove(next_path_point)
            path_list.append(path)
            path_list += self.__maximal_non_branching_paths_search(next_path_point, remain_edges, in_degree)
        return path_list

    def contig_generation(self):
        return [string_spelled_by_a_genome_path_problem(path) for path in self.maximal_non_branching_paths_search_start()]


        
if __name__ == "__main__":

    
    g = debruijn_graph()
    
    with open("dataset_6207_2 01.34.51.txt", "r") as f:
        string = f.readlines()
        for i in range(len(string)):
        
            string[i] = string[i].replace("\n", "")
        while "" in string:
            string.remove("")
    for i in string:
        g.add_direct_edge(i, len(i) - 1)
    print(string_spelled_by_a_genome_path_problem(g.eulerian_path_search()))
    #with open("dataset_200_8_result.txt", "w") as w:
    #    for pattern, adjacencies in g.get_all_edges().items():
    #        if len(adjacencies) > 0:
    #            w.write(pattern + ' -> ' + str(', '.join(adjacencies)) + "\n")
    #a = g.eulerian_path_search()