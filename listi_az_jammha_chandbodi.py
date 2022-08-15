def list_jammha(s):
    total=0
    al=[]
    for x in s:
        total=0
        for y in x:
            total=total+y
        al.append(total)
    return al


s=[[1,2,3],
   [4,5,6]
   ]

print(list_jammha(s))

def _sum_of_rows_sample_(sample_list):
    mylist = []
    for item in sample_list:
        mylist.append(sum(item))
    return mylist
