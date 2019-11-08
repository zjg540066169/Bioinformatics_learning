#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:21:37 2019

@author: jungangzou
"""
from Read_RNA_Table import read_rna_table

def Reverse_Complement_RNA(string):
    Reverse_Complement_String = ""
    for gene in range(len(string) - 1 , -1, -1):
        if string[gene] == 'A':
            Reverse_Complement_String += "T"
        elif string[gene] == 'C':
            Reverse_Complement_String += "G"
        elif string[gene] == 'G':
            Reverse_Complement_String += "C"
        elif string[gene] == 'T':
            Reverse_Complement_String += "A"
    return Reverse_Complement_String

def peptide_encoding(dna, peptide):
    condon_dic = read_rna_table("RNA_codon_table_1.txt")
    peptide_dna = []
    reverse_dna = Reverse_Complement_RNA((dna))
    for i in range(0, len(dna) - len(peptide) * 3 + 1):
        #print(dna[i:i+len(peptide) * 3])
        for j in range(len(peptide)):
            dna_sequence = dna[i+j*3:i+j*3+3]            
            #print(dna_sequence, condon_dic[dna_sequence.replace("T", "U")], condon_dic[Reverse_Complement_RNA(dna_sequence.replace("T", "U"))], peptide[j])
        #print(condon_dic[dna_sequence.replace("T", "U")])
            if condon_dic[dna_sequence.replace("T", "U")] != peptide[j]:
                break
        else:
            peptide_dna.append(dna[i:i+len(peptide) * 3])


    for i in range(0, len(dna) - len(peptide) * 3 + 1):
        #print(dna[i:i+len(peptide) * 3])
        for j in range(len(peptide)):
            dna_sequence = reverse_dna[i+j*3:i+j*3+3]            
            if condon_dic[dna_sequence.replace("T", "U")] != peptide[j]:
                break
        else:
            peptide_dna.append(Reverse_Complement_RNA(reverse_dna[i:i+len(peptide) * 3]))
    
    return peptide_dna

if __name__ == '__main__':
    dna = ""
    with open("Bacillus_brevis.txt", "r") as f:
        rna = f.readlines()
        for i in range(len(rna)):
            dna += rna[i].replace("\n", "")
    #print(len(dna))
    dna = "CCGAGGACCGAAAUCAAC"
    num = 0
    peptide = "PRETEIN"
    for i in peptide_encoding(dna, peptide):
        num += 1
    #print(peptide_encoding(dna, peptide))
    
        