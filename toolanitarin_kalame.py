def find_longest_word(input_string):
    input_string=input_string.split()
    maximum=0
    longest=""
    for x in input_string:
        if len(x)>=maximum:
            maximum=len(x)
            longest=x

    return longest
        




s="i am the longestt word in this sentence."

print(find_longest_word(s))

