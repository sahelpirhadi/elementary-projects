def jaam_sotoonha(s):
    al=[]
    length=len(s[0])
    for y in range(0,length):
        total=0
        for z in range(0,len(s)):
            total=total+s[z][y]
        al.append(total)
    return al




s=[[1,2,3],
   [4,5,6]
   ]

jaam_sotoonha(s)
