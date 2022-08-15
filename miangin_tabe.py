def miangin(x):
    y=0
    for z in x:
        y=y+z
    my_size=len(x)
    f=y/my_size
    return f

my_list=[1,2,3,4,5,6]

print(miangin(my_list))
