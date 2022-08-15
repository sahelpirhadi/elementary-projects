def find_word_horizontal(a,b):
    list_find=[]
    if b=='':
        return None
    else:
        for i in range(0,len(a[0])):
            stt=''
            for j in range(0,len(a)):
                stt=stt+a[j][i]
            print(stt)

crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='c'

print(find_word_horizontal(crosswords,word)) 
