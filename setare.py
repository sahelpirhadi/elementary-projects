adad=int(input('your number'))
if adad>1:
    print("*"*adad)
    for i in range(adad-1,1,-1):
        print('*'+(i-2)*' '+'*')
    print('*')
elif adad==1:
    print('*')
