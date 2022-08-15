def kmm(x,y):
    z=0
    for n in range(1,x+1):
        if x%n==0:
            for m in range(1,y+1):
                if y%m==0:
                    if m==n and m>z:
                        z=m
                    
    w=x*y
    q=w/z
    return q


print(kmm(6,4))


def _least_common_multiple_sample_(a, b):
    # first make a backup/copy of a
    copy_of_a = a
    # While the remainder when a is divided by b is not 0
    # continue to add a to its backup (copy_of_a)
    while (copy_of_a % b) != 0:
        copy_of_a = copy_of_a + a
    return copy_of_a
