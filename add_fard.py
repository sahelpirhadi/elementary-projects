def add_fard(a):
    b=a
    for x in range(0,len(b)):
        if b[x]%2!=0:
            b[x]=b[x]+1
    b.sort()
    return b

a=[2,3,7,9,5,6,3,5]
print(add_fard(a))
