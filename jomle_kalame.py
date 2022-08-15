def jomle_kalame(s,n):
    B=s.lower()
    A=B.split()
    count=0
    for x in A:
        if x[0]==n:
            count=count+1
    return count











s="Hello I am sahel and I am here for you"
n="i"

print(jomle_kalame(s,n))
