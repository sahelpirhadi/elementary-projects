def calculate_factorial(n):
    if n<=1:
        return 1
    else:
        final=n*calculate_factorial(n-1)
        return final

n=10
print(calculate_factorial(n))
