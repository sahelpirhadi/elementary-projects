def sorting(a):
    b=a
    for x in range(0,len(b)):
        for y in range(0,len(b)):
            if b[x]<b[y]:
                u=b[y]
                b[y]=b[x]
                b[x]=u
    return b

a=[1,2,8,3,6,7,5]

print(sorting(a))
        
            
            
