def bordarr(x):
    z=0
    for y in x:
        z=z+(y**2)
    guess=z/2
    error=0.000001
    while (abs(z-guess**2)>error):
        taghsim=z/guess
        guess=(taghsim+guess)/2

    return guess


w=[2,3,-4]

print(bordarr(w))
        
    
