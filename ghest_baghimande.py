def remain_payment(principal,annual_interest_rate,duration,number_of_payments):
    if annual_interest_rate!=0:
        r=(annual_interest_rate/100)/12
        n=duration*12
        p=number_of_payments
        rl=(principal*(((1+r)**n)-((1+r)**p)))/(((1+r)**n)-1)
        return rl
    else:
        n=duration*12
        p=number_of_payments
        rl=principal-principal*(p/n)
        return rl

