def dict_letter(s):
    s1=s.replace(" ","")
    s1=s1.lower()
    new={}
    count=0
    for x in s1:
        count=s1.count(x)
        s1=s1.replace(x,'')
        if count!=0:
            new.setdefault(x,count)
    return new
            





s="Helllooo There what a good day"

dict_letter(s)


def _dictionary_of_letter_counts_sample_(sample_string):
    stripped_string = sample_string.replace(" ", "")        # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()     # convert to lower case
    sample_dictionary = {}
    # Iterate through the lowercase stripped string and set each
    # character as a key and its count as the value
    for character in lowercase_stripped_string:
        sample_dictionary[character] = lowercase_stripped_string.count(character)
    return sample_dictionary
