def find_integer_with_most_divisors(input_list):
    biggest=0
    m=0
    for x in input_list:
        count=0
        for y in range(1,x+1):
            if x%y==0:
                count=count+1
                if biggest==count:
                    continue
                if count>biggest:
                    biggest=count
                    m=x
            
    return m

a=[8, 12, 18, 6]

print(find_integer_with_most_divisors(a))
