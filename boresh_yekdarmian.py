def boresh_yekdarmian(a):
    z=[]
    for x in range(0,len(a)):
        if x%2==0:
            k=a[x]
            z.append(k)
    return z


input_list=[2,4,6,8,10,12,14]
print(boresh_yekdarmian(input_list))
        
