def normal(bordar):
    x=bordar[0]
    y=bordar[1]
    z=bordar[2]
    w=((x**2)+(y**2)+(z**2))**(1/2)
    q=[bordar[0]/w,bordar[1]/w,bordar[2]/w]

    return q

bordar=[2,3,-4]

print(normal(bordar))
    
