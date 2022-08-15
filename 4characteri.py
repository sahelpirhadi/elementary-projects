def tedad_kalamat_4character(s):
    A=s.lower().split()
    count=0
    for x in A:
        if len(x)>4:
            count=count+1
    return count


s="hello man sahelam va inja irane!"

print(tedad_kalamat_4character(s))
