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

s1="helloi"
s2="helloo"

print(single_insert_or_delete(s1,s2))
