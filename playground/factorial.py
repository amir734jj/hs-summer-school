def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def better_factorial(n):
    result = 1
    while n != 0:
        result = n * result
        n = n - 1
    return result

# print(factorial(30000))
print(better_factorial(30000))

