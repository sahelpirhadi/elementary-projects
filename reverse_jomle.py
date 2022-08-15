def reverse_jomle(s):
    A=s.swapcase()
    sr=""
    for x in range(len(A)-1,-1,-1):
        sr=sr+A[x]

    return sr


s="Hello i AM saHEl"

print(reverse_jomle(s))
