def maximum(x):
    z=x[0]
    for y in x:
        if z<y:
            z=y
    return z
    


w=[1]

print(maximum(w))
            
        
