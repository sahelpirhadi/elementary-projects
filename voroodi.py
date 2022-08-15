def tarikh(vorodi):
    from math import floor
    listv=vorodi.split()
    months={"March":1,"April":2,"May":3,"June":4,"July":5,"Augest":6,"September":7,"October":8,"November":9,"December":10,"January":11,"February":12}
    days={'0':'Sunday','1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday'}
    m=months[listv[0]]
    d=int(listv[1])
    c=int(listv[2][:2])
    if m==11 or m==12:
        y=int(listv[2][2:])-1
    else:
        y=int(listv[2][2:])
    w=(d + floor(2.6*m - 0.2) - 2*c + y + floor(y/4) + floor(c/4))%7
    w1=str(w)
    return days[w1]

vorodi="May 5 1992"
print(tarikh(vorodi))
