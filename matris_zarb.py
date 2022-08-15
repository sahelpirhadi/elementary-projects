def matris_zarb(s1,s2):
    sotoon1=len(s1[0])
    satr2=len(s2)
    if sotoon1==satr2:
        return True
    else:
        return False


s1=[[1,2,3],
    [2,3,4]
    ]

s2=[[1,2],
    [2,3],
    [2,3]
    ]

print(matris_zarb(s1,s2))
