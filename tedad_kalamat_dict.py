def tedad_kalamat_dict(s):
    s=s.lower()
    words=s.split()
    final={}
    for x in words:
        final[x]=words.count(x)

    return final



s="hello there I am the best and i am here"

print(tedad_kalamat_dict(s))
        
