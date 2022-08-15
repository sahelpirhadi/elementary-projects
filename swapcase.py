def _my_Swap(s):
    output_string=""
    for char in s:
        if (ord(char)<= 90) and (ord(char)>=65) :
            x=chr(ord(char)+32)
            output_string=output_string+x
        elif (ord(char)<= 122) and (ord(char)>=97):
            x=chr(ord(char)-32)
            output_string=output_string+x
        else:
            output_string=output_string+char
    return output_string
