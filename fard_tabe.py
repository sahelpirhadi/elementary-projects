def fard(x):
    m=0
    for y in x:
        if y%2!=0:
            m=m+y
    return m
        
x=[2,4,6,8]
print(fard(x))
