def adade_zoj(a,b):
    z=[]
    for x in range(a,b):
        if x%2==0:
            z.append(x)
    return z


print(adade_zoj(2,5))
