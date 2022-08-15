def find_word_horizontal(crosswords,word):
    list_find=[]
    if word=='' or crosswords==[]:
        return None
    else:
        for i in range(0,len(crosswords)):
            stt=''
            for j in range(0,len(crosswords[0])):
                stt=stt+crosswords[i][j]
            if stt.find(word)!=-1:
                list_find.append(i)
                list_find.append(stt.find(word))
                return list_find
    return None
def find_word_vertical(crosswords,word):
    list_find=[]
    if word=='' or crosswords==[]:
        return None
    else:
        for i in range(0,len(crosswords[0])):
            stt=''
            for j in range(0,len(crosswords)):
                stt=stt+crosswords[j][i]
            if stt.find(word)!=-1:
                list_find.append(stt.find(word))
                list_find.append(i)
                return list_find
    return None
def capitalize_word_in_crossword(crosswords,word):
    horizontal=find_word_horizontal(crosswords,word)
    vertical=find_word_vertical(crosswords,word)
    if horizontal!=None:
        new=crosswords
        for i in range(len(word)):
            iterable=horizontal[1]+i
            new[horizontal[0]][iterable]=new[horizontal[0]][iterable].swapcase()
        return new
    elif vertical!=None:
        new=crosswords
        for i in range(len(word)):
            iterable=vertical[0]+i
            new[iterable][vertical[1]]=new[iterable][vertical[1]].swapcase()
        return new
    else:
        return crosswords

crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word=''

print(capitalize_word_in_crossword(crosswords,word))

        
    
        
    
