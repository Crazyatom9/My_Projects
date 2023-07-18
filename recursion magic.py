# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:15:46 2023

@author: ASUS
"""

def check(a):
    print(a)
    if a==0:
        return 
    for i in range(a):
        check(a-1)
        
        
a=check(4)