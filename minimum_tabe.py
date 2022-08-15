def minimum(x):
    z=x[0]
    for y in x:
        if z>y:
            z=y
    return z

w=[45,2,5,8,96,78,456,3]

print(minimum(w))
