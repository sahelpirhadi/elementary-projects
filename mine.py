def find_mismatch(s1,s2):
    if len(s1) != len(s2):
        return 2
    s1=s1.lower()
    s2=s2.lower()
    number_of_mismatches=0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            number_of_mismatches=number_of_mismatches+1
            if number_of_mismatches>1:
                return 2
    return number_of_mismatches

def single_insert_or_delete(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1==s2:
        return 0
    if abs(len(s1)-len(s2))!=1:
        return 2

    if len(s1)>len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    else: # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1
def spelling_corrector(s1,correct_spelled):
    s1=s1.split()
    final=""
    for x in s1:
        x=x.lower()
        done=False
        if len(x)<=2:
            final=final+x+" "
        else:
            for y in correct_spelled:
                y=y.lower()
                number=single_insert_or_delete(x,y)
                number2=find_mismatch(x,y)
                if number==0:
                    final=final+x+" "
                    done=True
                    break
                if number==1:
                    final=final+y+" "
                    done=True
                    break
                if number2==1:
                    final=final+y+" "
                    done=True
                    break
            if done==False:
                final=final+x+" "               
    final=final.strip()
    print(final)
               
           
s1="Wee lpve Pythen"	
l1=['we', 'Live', 'In', 'Python']
spelling_corrector(s1,l1)
      
