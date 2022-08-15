def find_word_vertical(a,b):
    list_find=[]
    if b==''or a==[]:
        return None
    else:
        for i in range(0,len(a[0])):
            stt=''
            for j in range(0,len(a)):
                stt=stt+a[j][i]
            if stt.find(b)!=-1:
                list_find.append(stt.find(b))
                list_find.append(i)
                return list_find
crosswords=[]
word='mtkj'

print(find_word_vertical(crosswords,word))          
            
    
