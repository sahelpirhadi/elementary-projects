def spacee(a):
    q=""
    for x in range(0,len(a)):
        if a[x]!=" ":
            b=x
            break
    for z in range(b,len(a)):
        q=q+a[z]
    return q



a="hello   "

print(spacee(a))
                   
