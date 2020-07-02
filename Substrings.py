# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:08:16 2020

@author: Marcus
"""
#http://rosalind.info/problems/subs/

#CONFIRMED CORRECT

# Given: Two DNA strings s and t (each of length at most 1 kbp).

# Return: All locations of t as a substring of s.

s = 'TACAAGACCAAAGACCACAGCAAGACCATAAGACCAAAGACCAAAGACCAGACTCAAAGACCAAAGACCATGATAGCAACTTCAAGACCATGAAGACCACAAGACCATAAAGACCAAAGACCAAAGACCAAAGACCAGGTGGCAAGACCACAGGTTCAAGACCACCAAAGACCACTAAAGACCAGCAAGACCATCCTCTACAAGACCATTACAAGACCAAAGACCATAAGACCAAAGACCATTTAATAAGACCATAGCAAGACCACTAAACAAGACCAAAGACCACAAAGACCAAAGACCAAAAGACCACCAAGACCAAAGACCAATAAGACCACTAAGACCAGAAGACCACCGAAAGACCAAAGACCAAAGACCACCATGAAGACCAGTCTTCTTAAGACCAAAGACCATAAGACCACTAGATTCATCAAGACCAGAGAAGACCAAAGACCAAGAAGACCAGTTAAGACCAAAAGACCAAAGACCAGACTATAAGACCACCGAAAGACCATGGTTCAAGACCAGAAGACCAAAGACCAGTAAAAAGACCAAAGACCAAGCGAAGACCAAAGACCACAAGACCAACACGCAAGACCAAAGACCAGTAAAAGACCATCAAGACCATCAAGACCATCCGTAAGACCACAACGGTTCCGGTAAAGACCAGGCGCAAGACCACCTCCAAGACCAGATGTAAAGACCACGAAGACCAAAGACCATGTTAAGACCAGAAGACCAAAGACCAAAGACCAAAGACCACTAAGACCAAAGACCAACAGAAGACCAAAGACCAAAGACCACAAAGACCATAAGACCAAAGACCACTATAAGACCAGCAAAGACCATCCGTGAAGACCAAAGACCAACGAAGACCAAAGACCAGGTAAGACCAGAAAGTCC'
t = 'AAGACCAAA'

indexes = []

stringLength = len(s)
substrLength = len(t)

# for x in range(stringLength):
#     if s[x] == t[0] and s[x+1] == t[1] and s[x+2] == t[2] and s[x+3] == t[3]:
#         indexes.append(x+1)

for x in range(stringLength):
    thisSub = s[x:(x+substrLength)]
    print(thisSub)
    if thisSub == t:
        indexes.append(x+1)
        
for x in range(len(indexes)):
    print (indexes[x])
    