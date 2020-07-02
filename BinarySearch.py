# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:44:27 2020

@author: Marcus
"""
# https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array

# Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.

# Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

n = 5
m = 6

A = [10, 20, 30, 40, 50]
listInts = [40, 10, 35, 15, 40, 20]

#get target key from listInts
thisKey = listInts[0]
#set min and max value of window in the A array
minVal = A[0]
maxVal = A[n-1]

#find middle of A array
mid = int(n/2)
midVal = A[mid]
#compare target key to a[n/2], if lower-iterate on first half, if lower-iterate on 2nd half
if thisKey < midVal:
    print('lower') 
if thisKey > midVal:
    print('higher')

