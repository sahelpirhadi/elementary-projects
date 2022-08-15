def monthly_payment(principal,annual_interest_rate,duration):
    if annual_interest_rate!=0:
        r=(annual_interest_rate/100)/12
        n=duration*12
        mp=(principal*(r*((1+r)**n)))/(((1+r)**n)-1)
        return mp
    else:
        n=duration*12
        mp=principal/n
        return mp



