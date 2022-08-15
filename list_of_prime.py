def list_of_primes(n):
    z=[]
    m=0
    z.append(2)
    for x in range(2,n):
        for y in range(2,x):
            if x%y==0:
                break
            else:
                z.append(x)
                break
    z.sort()
    return z



a=5

print(list_of_primes(a))
            
            
