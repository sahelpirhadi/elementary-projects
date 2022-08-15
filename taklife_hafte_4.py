a=float(input("Enter loan amount:"))
b=float(input("Enter annual interest rate (percent):"))
c=int(input("Enter loan duration in years:"))
import pardakht_mahane
import ghest_baghimande
print("LOAN AMOUNT:",int(a),"INTEREST RATE (PERCENT):",int(b))
print("DURATION (YEARS):",c,"MONTHLY PAYMENT:",int(pardakht_mahane.monthly_payment(a,b,c)))
x=1
while x<=c:
    
    z=pardakht_mahane.monthly_payment(a,b,c)
    y=z*x*12
    w=x*12
    print("YEAR:",x,"BALANCE:",int(ghest_baghimande.remain_payment(a,b,c,w)),"TOTAL PAYMENT",int(y))
    x=x+1
