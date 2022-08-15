def dict_tuple(mydict):
    t=tuple(mydict.keys())
    t2=tuple(mydict.values())
    return (t,t2)

mydict={1:"a", 2:"b", 3:"c", 4:"d"}

print(dict_tuple(mydict))
