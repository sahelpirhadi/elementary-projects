def list_sorted(s):
    final=[]
    for x in s:
        for y in x:
            final.append(y)

    al=sorted(final)
    return al


s=[[1,5,2],
   [7,6,2]
   ]

print(list_sorted(s))
            
