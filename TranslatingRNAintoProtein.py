# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:50:30 2020

@author: Marcus
"""
#http://rosalind.info/problems/prot/

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

# Return: The protein string encoded by s.

rna_codon = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
           "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
           "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
           "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
           "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
           "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
           "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
           "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }

#Open the text file containing the data and read the strings
f = open('rosalind_prot.txt','r')
rnaString = f.read()

#Initialize counters for the grouping trios
index1 = 0
index2 = 1
index3 = 2

#Number of rna string trios
groupNum = int(len(rnaString)/3)

#Initialize a string to hold the protein codons
proteinString = ''


#Loop through the rnaString based on the number found by groupNum, update each index at the end of loop, break loop if stop codon found
for x in range(groupNum):
    
    thisGroup = rnaString[index1] + rnaString[index2] + rnaString[index3]
    #print(thisGroup)
    thisCodon = rna_codon[thisGroup]
    #print(thisCodon)
    if thisCodon =='STOP':
        break
    proteinString += thisCodon
    index1 += 3
    index2 += 3
    index3 += 3
print(proteinString)