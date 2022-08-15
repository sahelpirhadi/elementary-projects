def nomarat(input_file_name):
    my_dictionary={}
    f=open(input_file_name)
    reader=f.readlines()
    for line in reader:
        if line[0]=='#':
            continue
        name, course1, course2, course3, course4 = line.strip().split(',')
        if int(course1)>70 and int(course3)>70:
            my_dictionary[name] = [float(course1), float(course2), float(course3), float(course4)]
    return my_dictionary

input_file_name='my.txt'
print(nomarat(input_file_name))
