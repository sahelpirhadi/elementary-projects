def nomarat(a):
    final=[]
    for x in a:
        count=0
        for y in a[x]:
            if y>=78:
                count=count+1
        if count==3:
            final.append(x)

    return final






s={'sahel':[78,100,100],'maryam':[45,95,87],'zahra':[100,100,100]}

print(nomarat(s))
