def miangin(s):
    total=0
    length=0
    for i in s:
        length=length+len(i)
        for y in i:
            total=total+y
    miangin=total/length

    return miangin

s=[[1,2,3],
       [4,5,6]
       ]
print(miangin(s))
