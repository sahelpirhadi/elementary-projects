def dastebandi_esm(file_name):
    my_dict={}
    d=[]
    di={}
    f=open(file_name)
    reader=f.readlines()
    for line in reader:
        if line[0]=='#':
            continue
        first,last,age=line.strip('\n').split(',')
        my_dict[last]=my_dict.get(last,d)+[(first,int(age))]
    for i in my_dict:
        my_dict[i]=dict(my_dict[i])
    return my_dict
file_name='mine.txt'
dastebandi_esm(file_name)
