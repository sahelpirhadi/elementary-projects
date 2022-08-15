def create_grades_dict(file_name):
    grade_dict={}
    tests=['Test_1','Test_2','Test_3','Test_4']
    fp=open(file_name,'r')
    lines=fp.readlines()
    fp.close()
    for line in lines:
        elements=line.strip().split(",")
        if elements and elements[0]:
            current_key=elements[0].strip()
            if len(current_key)==10:
                if grade_dict.get(current_key)==None:
                    # Key does not exist. Create it
                    grade_dict[current_key]=[elements[1].strip(),0,0,0,0,0]                
                for index in range(2,len(elements),2):
                    current_element=elements[index].strip()
                    if  current_element in tests:
                        grade_dict[current_key][int(current_element[-1])]=int(elements[index+1])
                grade_dict[current_key][5]=sum(grade_dict[current_key][1:5])/4.0
    return grade_dict
def print_grades(file_name):
    str1="{0:^10s}|{1:^16s}|{2:^6s}|{3:^6s}|{4:^6s}|{5:^6s}|{6:^6s}|".format('ID','Name','Test_1','Test_2','Test_3','Test_4','Avg.')
    print(str1)
    grades_dict=create_grades_dict(file_name)
    sorted1=sorted(grades_dict.keys())
    for i in sorted1:
        name,number1,number2,number3,number4,avg=grades_dict[i]
        str2="{0:<10s}|{1:<16s}|{2:>6d}|{3:>6d}|{4:>6d}|{5:>6d}|{6:>6.2f}|".format(i,name,number1,number2,number3,number4,avg)
        print(str2)
file_name='mine.txt'
print(create_grades_dict(file_name))
print_grades(file_name)
