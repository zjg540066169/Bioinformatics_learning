#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:45:41 2019

@author: jungangzou
"""

def read_mass_table(path):
    with open(path, "r") as f:
        peptide = f.readlines()
        for i in range(len(peptide)):
            peptide[i] = peptide[i].replace("\n", "").split()
        mass_dic = {}
        for i in peptide:
            mass_dic[i[0]] = int(i[1])
        return mass_dic
    
if __name__ == "__main__":
    print(read_mass_table("integer_mass_table.txt"))