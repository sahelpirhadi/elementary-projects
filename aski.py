def swapp(s):
    new_s=''
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            new_s=new_s+chr(ord(i)+32)
        elif ord(i)>=97 and ord(i)<=122:
            new_s=new_s+chr(ord(i)-32)
        else:
            new_s=new_s+i
    return new_s
s='Hello therE'
print(swapp(s))
