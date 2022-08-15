def max_meghdar_zoj(s):
    maximom=0
    thereis=False
    for x in s:
        for y in x:
            if y%2==0 and y>maximom:
                thereis=True
                maximom=y
    if thereis==True:
        return maximom


s=[[1,3,5],
   [7,9,5]
   ]

print(max_meghdar_zoj(s))
