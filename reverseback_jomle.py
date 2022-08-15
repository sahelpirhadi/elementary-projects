def reverseback_jomle(s):
    sr=""
    srb=""
    for x in range(len(s)-1,-1,-1):
        sr=sr+s[x]
        r=sr.split()
    for y in range(len(r)-1,-1,-1):
        srb=srb+r[y]+" "
        srb2=srb.strip()
    return srb2

s="Hello i AM saHEl."

print(reverseback_jomle(s))
