def sedadar(s):
    A=s.upper()
    count=A.count("A")+A.count("E")+A.count("I")+A.count("O")+A.count("U")
    print(count)

s="Hi there I am sahel"

sedadar(s)


def _total_vowels_sample_(sample_string):
    count = 0
    sample_string=sample_string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in sample_string:
        if char in vowels:
            count = count + 1
    return count
