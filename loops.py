# -*- coding: utf-8 -*-
"""
for loop: you know how maany times a set of code should run
while loop: you just give the stopping condition

range(starting number , ending number, step)
"""
sum=0
for i in range(1,1000):
    if i%7==0 and i%11==0:
        sum=sum+1
print(sum)
