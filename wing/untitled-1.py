def _product_of_two_vectors_sample_(a, b):
    import numpy
    product = (numpy.mat(a) * numpy.mat(b))     # returns a numpy array
    product_to_list = product.tolist()          # convert the numpy array to a standard list
    return product_to_list


a=[[2,3,4],
    [3,4,5]]

b=[[4,-3,12],
    [1,1,5],
    [1,3,2]]

print(_product_of_two_vectors_sample_(a, b))