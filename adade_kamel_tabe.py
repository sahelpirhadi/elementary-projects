def adade_kamel(x):
    m=0
    for y in range(1,x):
        if x%y==0:
            m=m+y
    if m==x:
        return True
    else :
        return False


print(adade_kamel(6))
            
