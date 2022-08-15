def adad(a):
    dade={'0':'','1':' one','2':' two','3':' three','4':' four','5':' five','6':' six','7':' seven','8':' eight','9':' nine','10':' ten','11':' eleven','12':' twelve','13':' thirteen','14':' fourteen','15':' fifteen',
        '16':' sixteen','17':' seventeen','18':' eighteen','19':' nineteen','20':' twenty','30':' thirty',
      '40':' forty','50':' fifty','60':' sixty','70':' seventy','80':' eighty',
        '90':' ninety','100':' one hundred','200':' two hundred','300':' three hundred','400':' fourhundred','500':' five hundred',
      '600':' six hundred','700':' seven hundred','800':' eight hundred','900':' nine hundred'}
    new=''
    sadgan=str(((a//100)%10)*100)
    strdade=str(a)
    if strdade[2]=='1':
        new=dade[strdade[0]]+' '+'thousand'+dade[sadgan]+dade[strdade[2:]]
    else:
        dahgan=str(((a//10)%10)*10)
        new=dade[strdade[0]]+' '+'thousand'+dade[sadgan]+dade[dahgan]+dade[strdade[3]]
    new=new.strip()
    return new

a=1122
print(adad(a))
