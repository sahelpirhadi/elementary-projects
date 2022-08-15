def changing(a,b,c):
    try:
        a[int(b)]=c
    except:
        return a
    else:
        return a

a=[2,3,"hi"]
b=2
c='hello'
print(changing(a,b,c))
