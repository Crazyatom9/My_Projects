# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 21:05:43 2023

@author: ASUS
"""
# Stack:- First in Last Out
class node():
    def __init__(self,val):
        self.val=val
        self.next=None

class stack():
    def __init__(self):
        self.head=None
        
    def insert(self,new):
        if self.head==None:
            self.head= node(new)
        else:
            newnode=node(new)
            newnode.next= self.head
            self.head=newnode 
    def poper(self):
        if self.head==None:
            print('Nothing to print')
        else:
            print(self.head.val)
            self.head=self.head.next            
    
    def get_length(self):
        if self.head!=None:
            count=1
            checker = self.head
            while checker.next!=None:
                count = count+1
                checker = checker.next
            print('Length of Stack is '+str(count))
            return count
        else:
            print('No data')
            
        
    
            
    def indexing(self,index_val):
        if index_val<self.get_length() and index_val>0:
            count=0
            checker=self.head
            newindex=self.get_length()-index_val
            while newindex!=count:
               count=count+1
               checker=checker.next
            print(index_val,count,self.get_length(),newindex)
            print(checker.val)
        else:
            print('no Data') 
    
    
    def max_element(self):
        max=0
        checker=self.head
        while checker.next!=None:
            if max>=checker.val:
                max=checker.val
            checker=checker.next
        print('Max Element is '+str(max))
            



c=stack()

for i in range(1,100,5):
    c.insert(i)
    


# c.insert(4)
# c.insert(5)
# c.insert(6)      insertion of data in a Stack


            
            
            
            
            
            
            
            
            
            
            
            
