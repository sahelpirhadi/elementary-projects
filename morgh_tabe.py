def d_ch(x,y):
    b=1
    sag=0
    morgh=0
    while b<=x:
        if y%(2*b)==0:
            sag=0
            morgh=b
        elif y%(2*b)==4:
            morgh=morgh+1
            sag=sag+1
        b=b+1
    if morgh+sag!=x:
        return None
    if morgh+sag==x:
        return [morgh,sag]

print(d_ch(3,10))
