def adade_fard(a,b):
    z=[]
    for x in range(a,b+1):
        if x%2!=0:
            z.append(x)
    z.reverse()
    return z

print(adade_fard(3,7))
