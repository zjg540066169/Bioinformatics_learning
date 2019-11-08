#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:45:45 2019

@author: jungangzou
"""
from Read_Mass_Table import read_mass_table
from Generating_Theoretical_Spectrum_Problem import generating_theoretical_spectrum_linear_peptide, generating_theoretical_spectrum_cyclic_peptide

def cyclopeptide_sequencing(spectrum):
    mass_table = read_mass_table("integer_mass_table.txt")
    one_k_mer = spectrum_consistent(spectrum, mass_table.copy())
    peptides = one_k_mer.copy()
    for i in range(int(max(spectrum) / 57)):
        new_peptides = []
        for peptide in peptides:
            for j in one_k_mer:
                new_peptides.append(peptide + j)
        peptides_temp = []
        for new_peptide in new_peptides:
            new_peptide_spectrum = generating_theoretical_spectrum_linear_peptide(new_peptide)
            #if max(new_peptide_spectrum.values()) == max(spectrum):
            if spectrum_consistent_bool(spectrum, new_peptide_spectrum):
                peptides_temp.append(new_peptide)
        if len(peptides_temp) != 0:
            peptides = peptides_temp
    peptides = set(peptides)
    print(sorted(peptides))
    cyclopeptide_spectrum = []
    for i in peptides:
        s = []
        for j in i:
            s.append(str(mass_table[j]))
        cyclopeptide_spectrum.append("-".join(s))
    return set(cyclopeptide_spectrum)

def spectrum_consistent(original_spectrum, spectrum):
    consistent_factor = []
    for i in spectrum:
        if spectrum[i] in original_spectrum:
            consistent_factor.append(i)
    return consistent_factor

def spectrum_consistent_bool(original_spectrum, spectrum):
    for i in spectrum:
        if spectrum[i] not in original_spectrum:
            return False
    return True

if __name__ == "__main__":
    with open("dataset_100_6.txt", "r") as f:
        mass = f.readlines()[0].split()
        for i in range(len(mass)):
            mass[i] = int(mass[i])

    print(" ".join(cyclopeptide_sequencing(mass)))