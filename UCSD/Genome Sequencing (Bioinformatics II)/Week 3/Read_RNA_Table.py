#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:04:32 2019

@author: jungangzou
"""



def read_rna_table(path):
    with open(path, "r") as f:
        rna = f.readlines()
        for i in range(len(rna)):
            rna[i] = rna[i].replace("\n", "").split()
        codon_dic = {}
        for i in rna:
            if len(i) > 1:
                codon_dic[i[0]] = i[1]
            else:
                codon_dic[i[0]] = ""
        return codon_dic
