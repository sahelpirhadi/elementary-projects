def calculate_grades(file_name):
    import statistics
    d=0
    final=[]
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    file_pointer.close()
    for i in data:
        dotai=tuple()
        mylist=[]
        mylist=i.strip().split(",")
        for j in range(1,len(mylist)):
            mylist[j]=int(mylist[j])
        d=statistics.mean(mylist[1:])
        dotai=(mylist[0],d)
        final.append(dotai)
    sorted_list=sorted(final, key=lambda x:(x[0]))
    sorted_list=tuple(sorted_list)
    return sorted_list
file_name="my.txt"

calculate_grades(file_name)
#
