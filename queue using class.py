# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:06:21 2023

@author: ASUS
"""
class node():
    def __init__(self,val):
        self.val=val
        self.next=None
        
class queue():
    def __init__(self):
        self.head=None
        
    def insert(self,new):
        if self.head==None:
           self.head= node(new)
        else:
            newnode=node(new)
            point=self.head
            while point.next!=None:
                point=point.next
            point.next=newnode
            
    def poper(self):
        if self.head==None:
            print('Nothing to print')
        else:
            print(self.head.val)
            self.head=self.head.next           
    
    def get_length(self):
        if self.head!=None:
            count=1
            check = self.head
            while check.next!=None:
                count = count+1
                check = check.next
            print('Length of Stack is '+str(count))
            return count
        else:
            print('No data')
            
            
    def indexing(self,index_val):
        if index_val<self.get_length() and index_val>0:
            count=0
            checker=self.head
            while index_val!=count:
               count=count+1
               checker=checker.next
            print(index_val,count,self.get_length())
            print(checker.val)
        else:
            print('no Data')
                    
                
            
            
            
            
            
c=queue()
# c.insert(4)
# c.insert(5)
# c.insert(6)
        
for i in range(1,100,5):
    c.insert(i)
    

    
    
