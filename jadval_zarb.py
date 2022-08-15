def multiplication_table(n):
    final=[]
    for i in range(1,n+1):
        a=[]
        for j in range(1,n+1):
            a.append(i*j)
        final.append(a)
    return final

n=5

print(multiplication_table(n))
