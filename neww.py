def n_letter_dictionary(my_string):
    d=[]
    my_string=my_string.lower()
    mydict={}
    mylist=my_string.split(' ')
    for i in mylist:
        x=len(i)
        mydict[x]=mydict.get(x,[i])
        if mydict[x].count(i)==0:
            mydict[x]=mydict.get(x,[i])+[i]
        else:
            continue
    for i in mydict:
        mydict[i].sort()
            
    return mydict
    
my_string='The way you see people is the way you treat them and the Way you treat them is what they become'
n_letter_dictionary(my_string)
