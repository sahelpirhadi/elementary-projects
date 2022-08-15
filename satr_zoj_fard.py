def satr_zoj_fard(s):
    zoj=0
    final=[]
    fard=0
    for x in s:
        total=0
        for y in x:
            total=total+y
        if total%2==0:
            zoj=zoj+1
        if total%2!=0:
            fard=fard+1
    
    final.insert(0,zoj)
    final.insert(1,fard)
    return final


s=[[1,2],
   [3,4]
   ]

print(satr_zoj_fard(s))
            

def _count_even_sum_sample_(sample_2d_list):
    even_count = 0
    odd_count = 0
    # For each row
    for rows in sample_2d_list:
        row_sum = sum(rows)
        if row_sum % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return [even_count, odd_count]
