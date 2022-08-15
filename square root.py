def show_jazr(number):
    guess=number/2
    error=0.01
    while(abs(number-guess**2)>error):
        taghsim=number/guess
        guess=(taghsim+guess)/2
    print("the square root of",number,"is",guess)



x=float(input("give me a number"))

show_jazr(x)

show_jazr(50)
show_jazr(70)
