def spacee(a):
    q=""
    for x in range(len(a)-1,-1,-1):
        if a[x]!=" ":
            b=x
            break
    for z in range(0,b+1):
        q=q+a[z]
    return q


a="hello   "

print(spacee(a))
