dictofwords={}
final=""
tedad=int(input())
for a in range(tedad):
    kalamat=input()
    kalamat=kalamat.split(" ")
    dictofwords[kalamat[0]]=kalamat[1:4]
jomle=input()
dictvalue=list(dictofwords.values())
jomle=jomle.split(' ')
for b in jomle:
    conter=False
    for c in dictvalue:
        if b in c:
            conter=True
            h=list(dictofwords.keys())[dictvalue.index(c)]
            final=final+h+" "
        else:
            continue
    if conter==False:
        final=final+b+" "
print(final.strip())
