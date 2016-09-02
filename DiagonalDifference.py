#!/bin/python

import sys


n = int(raw_input().strip())
a = []
b = 0
c = 0
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

for num in range(n):
    for num1 in range(n):
        if num == num1:
            b = a[num][num1] + b
            
for num in range(n):
    for num2 in range(n):
        if num + num2 == n-1:
            c = a[num][num2] + c
            
print abs(c - b)