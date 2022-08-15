def create_grades_dict(file_name):
    import numpy
    mydict={}
    f=open(file_name)
    reader=f.readlines()
    for line in reader:
        mlist=line.strip('\n').split(',')
        mlist=mlist[:6]
        for k in range(0,len(mlist)):
            mlist[k]=mlist[k].strip(' ')
        mydict[mlist[0]]=mlist[1:]
    s=list(mydict.values())
    for i in range(0,len(s)):
        slist=[]
        for j in range(1,len(s[i])):
            if s[i][j].isdecimal():
                s[i][j]=int(s[i][j])
            else:
                s[i][j]=0
        slist=s[i][1:]
        s[i].append(numpy.mean(slist))
    return mydict 
file_name='mine.txt'
print(create_grades_dict(file_name))

    
