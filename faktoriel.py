number=int(input("please enter a number:"))
x=number
while number>=1:
    if number-1!=0:
        x=x*(number-1)
    number=number-1

print(x)   
