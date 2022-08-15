def my_encryption(my_string):
    character_set="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key="Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    for x in my_string:
        for y in range(len(character_set)):
            if x==character_set[y]:
                my_string=my_string.replace(x,secret_key[y])
    return my_string

    
s="Lets meet at the usual place at 9 am"

print(my_encryption(s))

def my_encryption(my_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    encrypted_message = ""
    for character in my_string:
        index = character_set.find(character)
        encrypted_message = encrypted_message + secret_key[index] 
  
    return encrypted_message
