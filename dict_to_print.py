def formatted_print(a):
    values=list(a.values())
    values.sort()
    values.reverse()
    for i in values:
        str=''
        d=list(a.keys())[list(a.values()).index(i)]
        str='{0:<10s}{1:>6.2f}'.format(d,i)
        print(str)
a={'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900}

formatted_print(a)
