def jaam_fard(a,b):
    z=0
    w=0
    for x in a:
        if x%2!=0:
            z=z+x
    for y in b:
        if y%2!=0:
            w=w+y
    q=w+z

    return q

a=[2,3,5]
b=[3,6,5]

print(jaam_fard(a,b))
            
