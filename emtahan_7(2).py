def construct_dictionary_from_lists(names, ages, scores):
    list1=[]
    my_dict={}
    for i in range(len(names)):
        list1=[]
        list1.append(ages[i])
        list1.append(scores[i])
        if scores[i]>=60:
            list1.append('pass')
        else:
            list1.append('fail')
        my_dict[names[i]]=list1
    return my_dict

names=["paul", "saul", "steve", "chimpy"]
ages=[28, 59, 22, 5]
scores=[59, 85, 55, 60]
construct_dictionary_from_lists(names, ages, scores)
        
def construct_dictionary_from_lists(names, ages, scores):
    sample_dict = {}
    for index in range(0, len(names)):
        if scores[index] >= 60:
            sample_dict[names[index]] = [ages[index], scores[index], "pass"]
        else:
            sample_dict[names[index]] = [ages[index], scores[index], "fail"]

    return sample_dict
