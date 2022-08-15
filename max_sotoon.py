def max_sotoon(s):
    al=[]
    length=len(s[0])
    for y in range(0,length):
        maximom=0
        for z in range(0,len(s)):
            if s[z][y]>maximom:
                maximom=s[z][y]
        al.append(maximom)
    return al

s=[[1,3],
   [7,8]
   ]

print(max_sotoon(s))
