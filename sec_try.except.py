def attach(a,b):
    try:
        c=a+b
    except TypeError:
        return None
    else:
        return c

a="she"
b="is"
print(attach(a,b))
