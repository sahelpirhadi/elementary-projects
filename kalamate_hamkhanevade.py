def anagrams(my_string1, my_string2):
    my_string1=my_string1.lower()
    my_string2=my_string2.lower()
    second=my_string2
    if len(my_string1)==len(my_string2):
        for x in my_string1:
            if x in second:
                second=second.replace(x,"",1)
        if second=="":
            print(True)
        else:
            print(False)
    else:
        print(False)

def anagrams(my_string1, my_string2):
    if sorted(my_string1.lower()) == sorted(my_string2.lower()):
        return True
    else:
        return False





a="Orchestra"
b="Carthorse"

anagrams(a,b)
