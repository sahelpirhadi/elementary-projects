def milk_bread(file_name):
    two=[]
    three=[]
    dict1={}
    f=open(file_name)
    data=f.readlines()
    for line in data:
        one=[]
        one=line.strip('\n').split(' ')
        if one[0]=='m':
            two.append(one[1:])
        elif one[0]=='b':
            three.append(one[1:])
        for i in range(0,len(two)):
            for j in range(0,len(two[0])):
                two[i][j]=float(two[i][j])
        for i in range(0,len(three)):
            for j in range(0,len(three[0])):
                three[i][j]=float(three[i][j])
    dict1['milk']=two
    dict1['bread']=three
    return dict1
file_name='my.txt'
print(milk_bread(file_name))
