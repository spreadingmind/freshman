'''This decorator greatly enhances the speed of recursive function
    by simply hashing(memoizing) function results'''


def memoize(func):
    memo = {}
    def log(arg):
        if arg not in memo:
            memo[arg] = func(arg)
        return memo[arg]
    return log

@memoize
def fibonacci(n):
    assert n >= 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


