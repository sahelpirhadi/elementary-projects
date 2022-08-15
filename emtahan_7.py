def row_maximums(my_multidimensional_list):
    my_dict={}
    x=0
    for i in my_multidimensional_list:
        maximum=0
        for j in i:
            if maximum<j:
                maximum=j
        key='row '+str(x)+' max'
        my_dict[key]=maximum
        x=x+1
    return my_dict
my_multidimensional_list=[[5, 0, 0, 0, 13],
                          [0, 12, 0, 0],
                          [20, 0, 11, 0],
                          [6, 0, 0, 8]]
print(row_maximums(my_multidimensional_list))
