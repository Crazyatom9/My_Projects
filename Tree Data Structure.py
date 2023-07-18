# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 19:21:23 2023

@author: ASUS
"""
class node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    def insert(self,new_val):
        checker = self
        if checker.val<new_val:
            if checker.left == None:
                checker.left = node(new_val)
            else:
                checker.left.insert(new_val)
        else:
            if checker.right == None:
                checker.right = node(new_val)
            else:
                checker.right.insert(new_val)
    def inorder(self):
        if self.left.left!=None:
            self.left.inorder()
        else:
            print(self.left.val)
        print(self.val)
        if self.left.right!=None:
            self.right.inorder()
        else:
            print(self.right.val)
        
    def postorder(self):
        if self.left.left!=None:
            self.left.postorder()
        else:
            print(self.left.val)
        
        if self.left.right!=None:
            self.right.postorder()
        else:
            print(self.right.val)
        print(self.val)
        
    def preorder(self):
        print(self.val)
        if self.left.left!=None:
            self.left.preorder()
        else:
            print(self.left.val)
        
        if self.left.right!=None:
            self.right.preorder()
        else:
            print(self.right.val)
    
    
    
    def max_val(self):
        if self.left.left!=None:
            self.left.max_val()
        else:
            self.max_value(self.left.val)
        self.max_value(self.val)
        if self.left.right!=None:
            self.right.max_val()
        else:
            self.max_value(self.right.val)
            
            
    def max_value(self):
        m=self
        n=0
        if m<n:
            n=m
        
        print(n)
            
            
            
        
       
a = node(10)
a.insert(5)
a.insert(11)
a.insert(6)
a.insert(12)
a.insert(8)
a.insert(4)
a.insert(10.5)
a.insert(5.5)
a.insert(13)
a.insert(11.5)
a.insert(10.6)
a.insert(10.4)
a.insert(4.5)
a.insert(3)

# a.preorder()
a.max_val()




