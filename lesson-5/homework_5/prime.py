### Task 5
# Define a function `is_prime(n)` which returns `True` 
# if the given n is _prime number_, otherwise returns `False`.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

        