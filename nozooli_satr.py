def nozooli_satr(s):
    al=[]
    for x in s:
        final=[]
        final=sorted(x)
        final.reverse()
        al.append(final)
    return al


s=[[3,2,5],
   [8,5,6]
   ]

print(nozooli_satr(s))


def _2d_rows_sorted_sample_(_2d_list):
    for rows in _2d_list:
        rows.sort(reverse=True)
    return _2d_list
