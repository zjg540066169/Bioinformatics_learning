#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 22:05:58 2019

@author: jungangzou
"""
from Read_Mass_Table import read_mass_table

def counting_peptides_with_given_mass(m):
    # we know the smallest mass is 57 for G, so the length of linear peptides 
    # will be less than int(m/57)
    # On the other hand, the largest mass is 186 for W, so the length will be
    # greater than int(m/186)
    # so the interval of length is [int(m/186), int(m/57)]
    mass_table = read_mass_table("integer_mass_table.txt")
    mass_table.pop("I")
    mass_table.pop("K")
    peptides = [""]
    count = 0
    mass_list = [0]
    for i in range(int(m / 57)):
        print(i)
        peptides_new = []
        mass_list_new = []
        for j in range(len(peptides)):
            for amino in mass_table:
                new_peptide = peptides[j] + amino
                new_peptide_mass = mass_list[j] + mass_table[amino]
                #if i >= int(m / 186) - 1:
                if new_peptide_mass == m:
                    count += 1
                    continue
                elif new_peptide_mass + 57 > m:
                    continue
                peptides_new.append(new_peptide)
                mass_list_new.append(new_peptide_mass)
        mass_list = mass_list_new
        peptides = peptides_new
    return count
                
                
        
def mass_count(mass_table, peptide):
    mass = 0
    for acid in peptide:
        mass += mass_table[acid]
    return mass

    
if __name__ == "__main__":
    
    print(counting_peptides_with_given_mass(1024))