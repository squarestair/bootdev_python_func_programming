def factorial_r(x):
    if x <= 1:
        return 1
    if x == 2:
        return 2
    return x * factorial_r(x-1)
