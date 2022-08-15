def _unique_list_sample_(a,b):
    c=a
    d=[]
    c.extend(b)
    for x in c:
        if x not in d:
            d.append(x)

    return d

a=[1,2,3,4,5]

b=[2,2,3,6,5]

print(_unique_list_sample_(a,b))
