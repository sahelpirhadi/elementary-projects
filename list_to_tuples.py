def list_to_tuples(some_2d_list):
    c=[]
    for i in some_2d_list:
        b=()
        i.reverse()
        b=tuple(i)
        c.append(b)
    return(tuple(c))

a=[['mean', 'really', 'is', 'jean'],
 ['world', 'my', 'rocks', 'python']]
list_to_tuples(a)
