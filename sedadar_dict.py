def harf_sedadar(s):
    s=s.replace(" ",'').lower()
    sedadar="aeiou"
    final={}
    for x in s:
        if x in sedadar:
            final[x]=s.count(x)
    return final



s="salaaamm man sahelamiii"

print(harf_sedadar(s))
                
    
