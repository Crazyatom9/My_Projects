"""
List
"""
# a=[34,5,7,3,7,4,9,2,5,7,89]
# su=0
# for i in range (len(a)):
#     su=su+a[i]
# print(su)


# a=[34,5,7,3,7,4,9,2,5,7,89,6]
# max=0
# for i in range(len(a)):
#     if a[i]>max:
#         max=a[i]
# print(max)
        
# a=[2,3,3,4,5,6,5,5,6,8]
# b=[]

# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
        
a=[2,3,3,4,5,6,5,5,6,8]
b=[]
for i in range(len(a)):
    c=0
    for j in range(len(b)):
        if a[i]==b[j]:
            c=c+1
    if c==0:
        b.append(a[i])
            
print(b)
            

    
