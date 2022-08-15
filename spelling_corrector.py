def spelling_corrector(s1,l1):
    s1=s1.split()
    final=""
    count=0
    for x in s1:
        done=False
        x=x.lower()
        if len(x)>=3:
            for y in l1:    
                y=y.lower()
                if done==True:
                    break
                if x==y:
                    final=final+x+" "
                    break
                elif len(x)==len(y):
                    for z in range(0,len(x)):
                        if x[z]!=y[z]:
                            count=count+1
                    if count==1:
                        final=final+y+" "
                        done=True
                        break
                elif abs(len(x)-len(y))==1:  
                    if len(x)>len(y):
                        for w in range(0,len(y)):  
                            if x[w]!=y[w]:
                                if x[w+1:]==y[w:]:
                                    final=final+y+" "
                                    done=True
                                    done2=True
                                    break
                                else:
                                    final=final+x+" "
                                    done=True
                                    break
                            final=final+y+" "
                            break
                    else:
                        for q in range(0,len(x)):
                            if x[q]!=y[q]:
                                if x[q:]==y[q+1:]:
                                    final=final+y+" "
                                    done=True
                                    break
                                if x[q]==y[q]:
                                    break
                                else:
                                    final=final+x+" "
                                    done=True
                                    break
                            final=final+y+" "
                            break
                    
        else:
            final=final+x+" "
    final=final.strip()
    print(final)
   
    


s1="Thes is the Firs cas"	
l1=['that','first','case','car']
spelling_corrector(s1,l1)



