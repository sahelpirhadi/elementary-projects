def one_to_2D(some_list, r, c):
    mylist=[]
    x=0
    temp_row=c*[None]
    for j in range(r):
        mylist.append(temp_row[:])
    if len(some_list)>=r*c:
        for i in range(len(mylist)):
            for j in range(len(mylist[0])):
                mylist[i][j]=some_list[x]
                x=x+1
    else:
        x=0
        row=len(some_list)//c
        column=len(some_list)%c
        for i in range(0,row+1):
            for j in range(0,len(mylist[0])):
                if i==row and j==column:
                    break
                mylist[i][j]=some_list[x]
                x=x+1        
    return mylist
some_list=[8,2,9,4,5,7,8]
r=2
c=3
print(one_to_2D(some_list, r, c))
