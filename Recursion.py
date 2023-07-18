# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 20:24:58 2023

@author: ASUS
"""
# #Recursion or recurive thinking where you only 


# Factorial of a number using Recursion
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)  #calling same function inside of same function
    
# print(fact(10))

# Fibonaaci Sreies

def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
        
print(fibo(10))
