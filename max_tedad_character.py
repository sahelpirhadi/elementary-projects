def max_character(s):
    A="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    B=s.lower().replace(" ","")
    count=0
    maximum=0
    port=0
    for x in A:
        count=B.count(x)
        if count>maximum or count==maximum:
            maximum=count
            port=x
    return port
            
            
s="khob man sahelam va in yek test hast"

print(max_character(s))


def _most_common_character_(sample_string):
    stripped_string = sample_string.replace(" ", "")    # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()    # convert to lower case
    sample_character = None
    sample_maximum_count = 0

    # Iterate through the given string and for each character
    # set a count, among these counts,  return the character whose count is maximum
    # On case of tie, return the last character that occurs that has the most count
    for character in lowercase_stripped_string:
        each_character_count = lowercase_stripped_string.count(character)
        if each_character_count >= sample_maximum_count:
            sample_maximum_count = each_character_count
            sample_character = character
    return sample_character
