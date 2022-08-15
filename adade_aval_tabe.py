def adade_aval(n):
    for x in (2,n):
        if n==2 or n==1 or n==0:
            return True
        if n%x==0:
            return False
            break
        else:
            return True


print(adade_aval(6))
        
