#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:13:15 2019

@author: jungangzou
"""

from Cyclopeptide_Scoring_Problem import cyclopeptide_scoring

def trim(leaderboard, N, experimental_spectrum):
    leaderboard_score = {}
    for i in leaderboard:
        leaderboard_score[i] = cyclopeptide_scoring(i, experimental_spectrum)
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
    for i in leader_score:
        if i[1] >= leader_score[N][1]:
            trim_leader.append(i[0])
        else:
            break
    return trim_leader
        

if __name__ == "__main__":
    with open("dataset_4913_3 09.39.07.txt", "r") as f:
        string = f.readlines()
        leaderboard = string[0].replace("\n", "").split()
        es = string[1].replace("\n", "").split()
        for i in range(len(es)):
            es[i] = int(es[i])
        N = int(string[2].replace("\n", ""))
        print()
        for i in trim(leaderboard, N, es):
            print(i, end = " ")
    