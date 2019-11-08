#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:42:26 2019

@author: jungangzou
"""
from Read_Mass_Table import read_mass_table
from Cyclopeptide_Scoring_Problem import cyclopeptide_scoring_cycle, cyclopeptide_scoring_linear
from Generating_Theoretical_Spectrum_Problem import generating_theoretical_spectrum_linear_peptide, generating_theoretical_spectrum_cyclic_peptide

def trim(leaderboard, N, experimental_spectrum):
    leaderboard_score = {}
    for i in leaderboard:
        leaderboard_score[i] = cyclopeptide_scoring_linear(i, experimental_spectrum)
    all_score = sorted(leaderboard_score.items(), key = lambda item:item[1], reverse = True)
    #print(all_score)
    for i in range(len(all_score)):
        #print(i)
        if i >= N and all_score[i][1] != all_score[i - 1][1]:
            leader_score = all_score[:i]
            break
    else:
        leader_score = all_score
    trim_leader = []
    if len(leader_score) < N:
        for i in leader_score:
            trim_leader.append(i[0])
        return trim_leader
    for i in leader_score:
        if i[1] >= leader_score[N][1]:
            trim_leader.append(i[0])
        else:
            break
    return trim_leader


def leaderboard_cyclopeptide_sequencing(N, mass_table, experimental_spectrum):
    #mass_table = read_mass_table("integer_mass_table.txt")
    
    peptides = list(set(mass_table.keys()))
    best_peptides = ["A"]
    parent_mass = max(experimental_spectrum)
    best_cyclopeptide_score = 0
    while len(peptides) != 0:
    #for i in range(int(max(experimental_spectrum) / 57)):
        new_peptides = []
        for peptide in peptides:
            for j in mass_table:
                new_peptides.append(peptide + j)
        temp_new_peptides = []
        for j in new_peptides:
            mass_peptide = max(generating_theoretical_spectrum_cyclic_peptide(j))
            if mass_peptide < parent_mass:
                temp_new_peptides.append(j)
                continue
            elif mass_peptide == parent_mass:
                temp_new_peptides.append(j)
                cyclopeptide_score = cyclopeptide_scoring_cycle(j, experimental_spectrum)
                if cyclopeptide_score > best_cyclopeptide_score:
                    best_peptides = [j]
                    best_cyclopeptide_score = cyclopeptide_score
                    print(best_cyclopeptide_score)
                    #print(cyclopeptide_scoring_cycle(j, experimental_spectrum))
                elif cyclopeptide_score == best_cyclopeptide_score:
                    best_peptides.append(j)
            elif  mass_peptide >  parent_mass:
                #equals that remove the unequal mass of peptide in new_peptides
                continue
        
        peptides = trim(temp_new_peptides, N, experimental_spectrum)
    best_result = []
    best_peptides = set(best_peptides)
    for i in best_peptides:
        s = []
        for j in i:
            s.append(str(mass_table[j]))
        best_result.append("-".join(s))
    return best_result

if __name__ == "__main__":
    
    with open("dataset_103_2 16.11.02.txt", "r") as f:
        string = f.readlines()
        N = int(string[0].replace("\n", ""))
        es = string[1].replace("\n", "").split()
        for i in range(len(es)):
            es[i] = int(es[i].replace("\n", ""))
        a = range(57, 201, 1)
        mass_table = {}
        for i in a:
            mass_table[chr(i)] = int(i)
        result  = leaderboard_cyclopeptide_sequencing(N, mass_table, es)
        for i in result:
            print(i, end = " ")
        
            
        