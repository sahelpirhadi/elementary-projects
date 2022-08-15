try:
    inputer=input("insert a number")
    inputer=int(inputer)
except ValueError:
    print('Error')
else:
    print("done")
