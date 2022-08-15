def miangin_miane(t):
    import numpy
    miane=numpy.median(t)
    miangin=numpy.mean(t)
    return(miangin,miane)

t=(3, 3, 0, 1, 12, 13, 15, 16)

print(miangin_miane(t))
