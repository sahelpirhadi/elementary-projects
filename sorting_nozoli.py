def sorting(a,b):
    c=a+b
    for x in range(0,len(c)):
        for y in range(0,len(c)):
            if c[y]<c[x]:
                u=c[y]
                c[y]=c[x]
                c[x]=u
    return c


a=[2,3,8,5,9,2]
b=[3,6,7,5,1]

print(sorting(a,b))
