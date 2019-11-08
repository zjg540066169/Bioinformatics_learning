#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:44:56 2019

@author: jungangzou
"""
from Read_Mass_Table import read_mass_table

def generating_theoretical_spectrum_cyclic_peptide(peptide):
    mass_table = read_mass_table("integer_mass_table.txt")
    
    subpeptides = [peptide]
    #in order to easily process cylce, we double peptide
    peptide *= 2
    
    for i in range(0, int(len(peptide) / 2)):
        for j in range(1, int(len(peptide) / 2)):
                subpeptides.append(peptide[i:i+j])
            
    spectrum = []
    for subpeptide in subpeptides:
        mass = 0
        for acid in subpeptide:
            mass += mass_table[acid]
        spectrum.append(mass)
    return  spectrum

def generating_theoretical_spectrum_linear_peptide(peptide):
    mass_table = read_mass_table("integer_mass_table.txt")
    subpeptides = []
    #in order to easily process cylce, we double peptide
    i = 0
    for i in range(0, int(len(peptide))):
        for j in range(1, int(len(peptide)) - i + 1):
            subpeptides.append(peptide[i:i+j])
    spectrum = []
    for subpeptide in subpeptides:
        mass = 0
        for acid in subpeptide:
            mass += mass_table[acid]
        spectrum.append(mass)
    return  spectrum

if __name__ == "__main__":
    a = "0 71 99 101 103 128 129 199 200 204 227 230 231 298 303 328 330 332 333"
    a = a.split(" ")
    for i in range(len(a)):
        a[i] = int(a[i])
    b = "CTV"
    b = sorted([0] + list(generating_theoretical_spectrum_linear_peptide(b)))
    for i in b:
        if i not in a:
            print("a")
            break
    else:
        print(True)
    #for i in ([0] + sorted(generating_theoretical_spectrum_linear_peptide(a))):
    #    print(i, end = " ")