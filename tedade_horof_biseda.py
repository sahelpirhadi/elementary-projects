def count_consonants(sample_string):
    sample_string=sample_string.lower()
    count=0
    sound="aeiou "
    for y in sample_string:
        for x in sound:
            if x==y:
                count=count+1
                break
    return(len(sample_string)-count)
    








s="hellothere"
print(count_consonants(s))
