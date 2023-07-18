n=6
def corner(n):
    if n==1:
        return 2
    else:
        return 2**n
def edge(n):
    if n==1:
        return 1
    else:
        return corner(n-1)+edge(n-1)*2
    
def face(n):
    if n==2:
        return 1
    else:
        return edge(n-1)+face(n-1)*2


print(corner(n),edge(n),face(n))