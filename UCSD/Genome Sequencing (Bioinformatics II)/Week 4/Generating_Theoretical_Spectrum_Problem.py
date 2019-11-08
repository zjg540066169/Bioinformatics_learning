#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:44:56 2019

@author: jungangzou
"""
from Read_Mass_Table import read_mass_table

def generating_theoretical_spectrum_cyclic_peptide(peptide):
    mass_table = read_mass_table("integer_mass_table.txt")
    
# =============================================================================
#     a = range(57, 201, 1)
#     mass_table = {}
#     for i in a:
#         mass_table[chr(i)] = int(i)
# =============================================================================
 
    
    subpeptides = [peptide]
    
    #in order to easily process cylce, we double peptide
    peptide *= 2
    
    for i in range(0, int(len(peptide) / 2) ):
        for j in range(1, int(len(peptide) / 2)):
                subpeptides.append(peptide[i:i+j])
            
    spectrum = [0]
    #print(subpeptides)
    for subpeptide in subpeptides:
        mass = 0
        for acid in subpeptide:
            mass += mass_table[acid]
        spectrum.append(mass)
    return  spectrum

def generating_theoretical_spectrum_linear_peptide(peptide):
    mass_table = read_mass_table("integer_mass_table.txt")
    
# =============================================================================
#     a = range(57, 201, 1)
#     mass_table = {}
#     for i in a:
#         mass_table[chr(i)] = int(i)    
# =============================================================================
    subpeptides = []
    #in order to easily process cylce, we double peptide
    i = 0
    for i in range(0, int(len(peptide))):
        for j in range(1, int(len(peptide)) - i + 1):
            subpeptides.append(peptide[i:i+j])
    spectrum = [0]
    for subpeptide in subpeptides:
        mass = 0
        for acid in subpeptide:
            mass += mass_table[acid]
        spectrum.append(mass)
    return  spectrum

if __name__ == "__main__":
    a = "IAQMLFYCKVATN"
    b = generating_theoretical_spectrum_cyclic_peptide(a)
    print(len(sorted(b)))
    for i in sorted(generating_theoretical_spectrum_cyclic_peptide(a)):
        print(i, end = " ")
    #print(([0] + list(generating_theoretical_spectrum_linear_peptide(a).values())))
    #for i in ([0] + sorted(generating_theoretical_spectrum_linear_peptide(a))):
    #    print(i, end = " ")