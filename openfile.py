def list_from_file(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.read()
    a=data.split('\n')
    return a
file_name='my.txt'

print(list_from_file(file_name))
        
