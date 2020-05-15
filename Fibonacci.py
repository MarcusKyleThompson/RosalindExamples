# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:39:36 2020
@author: Marcus

Fibonacci Numbers
"""

inputNum = 9   #index of dataset, zero indexed

fibSequence = [0,1] #initialize the first two values

if inputNum == 0:
    f_n = fibSequence[0]
    
if inputNum == 1:
    f_n = fibSequence[1]
    
for x in range(inputNum-1):
    f_n = fibSequence[x]+fibSequence[x+1]
    fibSequence.append(f_n)         #append the value to the fibsequence list
    
print(f_n)
    

