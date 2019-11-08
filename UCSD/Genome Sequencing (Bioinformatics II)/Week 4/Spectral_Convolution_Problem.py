#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:51:24 2019

@author: jungangzou
"""

def spectral_convolution(spectrum):
    convolution = []
    for i in range(len(spectrum)):
        for j in range(i, len(spectrum)):
            if spectrum[i] != spectrum[j]:
                convolution.append(spectrum[j] - spectrum[i])
    return convolution

if __name__ == "__main__":
    with open("dataset_104_4.txt", "r") as f:
        spectrum = f.readlines()[0].split()
        for i in range(len(spectrum)):
            spectrum[i] = int(spectrum[i])

    spectrum = [0, 57, 118, 179, 236, 240, 301]
    print(sorted(spectral_convolution(spectrum)))
    for i in spectral_convolution(spectrum):
        print(i, end = " .")