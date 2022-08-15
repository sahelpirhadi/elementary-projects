def palindrome(s):
    l=[]
    l2=[]
    d=False
    y=0
    for x in s:
        l.append(ord(x))
    print(l)
    for z in range(len(s)-1,-1,-1):
        l2.append(ord(s[z]))
    while y<len(s):
        d=False
        if l[y]==l2[y] or abs(l[y]-l2[y])==32:
            d=True
            y=y+1
        else:
            break
    return d

s="baba"

print(palindrome(s))


def _is_palindrome_sample_(sample_string):
    # Check if the inverted string  equals the original string
    if str(sample_string).lower() == str(sample_string)[::-1].lower():
        return True     # Sample string is a palindrome
    else:
        return False    # Sample string is not a palindrome
