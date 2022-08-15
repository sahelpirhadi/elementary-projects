def tedad(a,b):
    count=0
    for x in range(0,len(a)):
        if b==a[x]:
            count=count+1
    return count


a=[1,2,3,5,5,5,7]
b=5

print(tedad(a,b))
