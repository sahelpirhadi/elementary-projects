def _product_of_two_vectors_sample_(a, b):
    if len(a[0]) != len(b):
        return None
    # Create the result matrix and fill it with zeros
    output_list=[]
    temp_row=len(b[0])*[0]
    for r in range(len(a)):
        output_list.append(temp_row[:])
    for row_index in range(len(a)):
        for col_index in range(len(b[0])):
            sum=0
            for k in range(len(a[0])):
                sum=sum+a[row_index][k]*b[k][col_index]
            output_list[row_index][col_index]=sum
    return output_list
s1=[[1,2,3],
    [4,5,6]]

s2=[[1,2,3],
    [4,5,6],
    [7,8,9]]


print(_product_of_two_vectors_sample_(s1,s2))
