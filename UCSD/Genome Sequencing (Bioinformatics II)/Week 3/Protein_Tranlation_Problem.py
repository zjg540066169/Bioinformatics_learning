#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:04:32 2019

@author: jungangzou
"""

def protein_translation(codon_dictionary, string):
    protein_string = ""
    for i in range(0, len(string), 3):
        protein_string += codon_dictionary[string[i:i+3]]
    return protein_string

if __name__ == "__main__":
    with open("RNA_codon_table_1.txt", "r") as f:
        rna = f.readlines()
        for i in range(len(rna)):
            rna[i] = rna[i].replace("\n", "").split()
        codon_dic = {}
        for i in rna:
            if len(i) > 1:
                codon_dic[i[0]] = i[1]
            else:
                codon_dic[i[0]] = ""
    string = "CCAAGAACAGAUAUCAAU"
    print(protein_translation(codon_dic, string))