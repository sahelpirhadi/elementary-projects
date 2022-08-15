def maghsoom_alayh(k):
    z=[]
    for x in range(1,k+1):
        if k%x==0:
            z.append(x)
    return z

print(maghsoom_alayh(2))
