# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:56:29 2020

@author: Marcus
"""


#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

#Plan:  find all possible pairs, determine dominance of pairs, create loop to produce probability tree

#Input data
k=27
m=25
n=29

#determine possible pair list

letters = ['k','m','n']
pairList = []
pairDict = {}
for x in letters:
    for y in letters:
        #print(x+y)
        pairList.append(x+y)
        pairDict[x+y]=''
        
#function to determine dominance of pairs
def dominance(x):       #input should be a string with 2 letter, ex. 'mn'
    dominantRatio = 0   #value to hold amount of dominant allele combinations, out of 4
    values = {'k':'aa','m':'ab','n':'bb'}
    firstAllele = values[x[0]]
    secondAllele = values[x[1]]
    #print('Testing dominance on pair: ' + firstLetter + secondLetter)
    for s in firstAllele:
        for t in secondAllele:
            thisAllele = s+t
            if 'a' in thisAllele:
                dominantRatio += 1
    return dominantRatio/4    
#Find ratios for pairs for probability tree

combinedRatio = 0

for pair in pairList:
    population = k+m+n #reset population total in each loop iteration
    populationDict = {'k':k,'m':m,'n':n}    #reset population dictionary in each loop iteration

    firstRatio = populationDict[pair[0]]/population         #first selection in probability tree
    populationDict[pair[0]]-=1                              #remove value from corresponding key in populationDict
    secondRatio = populationDict[pair[1]]/(population-1)    #second selection in probability tree
    pairRatio = firstRatio*secondRatio                      #value probability of first two choices
    totalRatio = pairRatio*(dominance(pair))                #value of choices with respect to dominance
    combinedRatio+=totalRatio                               #value to sum up all ratios 

    
print(combinedRatio)