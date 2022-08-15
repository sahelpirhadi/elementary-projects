n=int(input("please insert a number:"))
print(n*"*")
for z in range(n-1,1,-1):
    print("*"+(z-2)*" "+"*")
print("*")
