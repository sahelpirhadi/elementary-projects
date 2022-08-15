def calculate_expenses(filename):
    handle=open(filename,'r')
    data=handle.readlines()
    handle.close()
    final=[]
    for i in data:
        mylist=i.strip().split(",")
        for j in range(0,len(mylist)):
            mylist[j]=mylist[j].strip()
        mylist[1]=float(mylist[1])
        z=[item for item in final if item[0] ==mylist[0]]
        if z==[]:
            final.append(mylist)
        else:
            a=final.index(z[0])
            final[a][1]=final[a][1]+mylist[1]
    sorted_list=sorted(final, key=lambda x:(x[0]))
    for q in range(0,len(sorted_list)):
            str=''
            str='${0:.2f}'.format(sorted_list[q][1])
            sorted_list[q][1]=str
            sorted_list[q]=tuple(sorted_list[q])
    print(sorted_list)
        
            
filename="my.txt"
calculate_expenses(filename)
