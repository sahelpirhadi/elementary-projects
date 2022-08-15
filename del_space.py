def del_space(a):
    z=""
    for x in a:
        if x==" ":
            continue
        else:
            z=z+x
    return z
            

a="hello i am there"

print(del_space(a))
