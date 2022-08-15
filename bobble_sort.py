def _custom_bubble_sort_sample_(original_list):
    # This is an implementation of the
    # famous bubble sort algorithm
    # This can a very inefficient algorithm
    # when used with large data
         
    # our purpose here however is to show how to sort
    # a list without any built-in methods
	

    # make a copy of the original list
    my_list = original_list[:]
  
    # get the length of the list
    length = 0
    for element in my_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            # if next element is greater element then swap them
            if my_list[index] > my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable
                unSorted = True
    return my_list  
