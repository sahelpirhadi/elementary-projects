def dafaate_tekrar(s,n):
    A=s.lower()
    count=A.count(n)
    return count

s="man emrooz 2 bar chai khordam 2 bar raftam biron"
n="2"

print(dafaate_tekrar(s,n))


def _count_character_sample_(input_string, input_character):
    # Instantiate a variable for counting
    my_count = 0
    # Iterate through each character in the given string
    # and check if the input character is equal to the
    # character in the string. If it does increase the
    # count by 1 and finally return the count
    for character in input_string.lower():
        if character == input_character.lower():
            my_count = my_count + 1
    return my_count
