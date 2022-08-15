n=int(input("please insert a number:"))
s="*"
for x in range(1,n+1):
    print(x*s)
x=x-1
while x>0:
    print(x*s)
    x=x-1


n = int(input("Please enter an integer: "))
for x in range(1, n+1):
    print("*" * x)
for y in range(n-1, 0, -1):
    print("*" * y)
