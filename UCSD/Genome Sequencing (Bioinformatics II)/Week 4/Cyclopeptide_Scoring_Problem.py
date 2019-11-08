#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 08:01:33 2019

@author: jungangzou
"""
from Read_Mass_Table import read_mass_table
from Generating_Theoretical_Spectrum_Problem import generating_theoretical_spectrum_cyclic_peptide, generating_theoretical_spectrum_linear_peptide

def cyclopeptide_scoring_linear(peptide, experimental_spectrum):
   
    theoretic_spectrum = sorted(generating_theoretical_spectrum_linear_peptide(peptide))
    experimental_spectrum = sorted(experimental_spectrum)
    scoring = 0
    #print(theoretic_spectrum)
    index_theoretic = 0
    index_experimental = 0
    
    while index_theoretic < len(theoretic_spectrum) and index_experimental < len(experimental_spectrum):
        if theoretic_spectrum[index_theoretic] == experimental_spectrum[index_experimental]:
            #print(theoretic_spectrum[index_theoretic])
            scoring += 1
            index_theoretic += 1
            index_experimental += 1
        elif theoretic_spectrum[index_theoretic] < experimental_spectrum[index_experimental]:
            index_theoretic += 1
        elif theoretic_spectrum[index_theoretic] > experimental_spectrum[index_experimental]:
            index_experimental += 1
    return scoring


def cyclopeptide_scoring_cycle(peptide, experimental_spectrum):
   
    theoretic_spectrum = sorted(generating_theoretical_spectrum_cyclic_peptide(peptide))
    experimental_spectrum = sorted(experimental_spectrum)
    scoring = 0
    #print(theoretic_spectrum)
    index_theoretic = 0
    index_experimental = 0
    
    while index_theoretic < len(theoretic_spectrum) and index_experimental < len(experimental_spectrum):
        if theoretic_spectrum[index_theoretic] == experimental_spectrum[index_experimental]:
            #print(theoretic_spectrum[index_theoretic])
            scoring += 1
            index_theoretic += 1
            index_experimental += 1
        elif theoretic_spectrum[index_theoretic] < experimental_spectrum[index_experimental]:
            index_theoretic += 1
        elif theoretic_spectrum[index_theoretic] > experimental_spectrum[index_experimental]:
            index_experimental += 1
        
    return scoring

if __name__ == "__main__":
    with open("dataset_4913_1.txt", "r") as f:
        string = f.readlines()
        peptide = string[0].replace("\n", "")
        es = string[1].replace("\n", "").split()
        for i in range(len(es)):
            es[i] = int(es[i])
    peptide = "PEEP"
    es = [0, 97, 97, 97, 100, 129, 194, 226, 226, 226, 258, 323, 323, 355, 393, 452]
    
    print(cyclopeptide_scoring_linear(peptide, es))