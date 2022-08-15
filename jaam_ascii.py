def jaam_ascii(a):
    z=0
    for x in a:
        z=z+ord(x)

    return z

a="hello"
print(jaam_ascii(a))
