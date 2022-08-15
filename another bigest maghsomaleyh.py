def tedad_maghsoom(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    return count
mylist=[]
mylist2=[0,0]
for i in range(0,20):
    adad=int(input())
    mylist2[0]=adad
    mylist2[1]=tedad_maghsoom(adad)
    mylist.append(tuple(mylist2)) 
sort=sorted(mylist, key=lambda x:(x[1],x[0]))
print(sort[-1])
