'''
A decorators that logs function arguments and it's results
'''

def logger(func):

    def log_1(*argum, **kwargs):
        kwargs = [i for i in kwargs.values()]
        arguments = 'You called {}'.format(func.__name__) + \
                    '(' + ','.join([str(i) for i in argum]) + \
                     ',' +  ','.join([str(i) for i in kwargs]) + ')'
        return arguments

    def log_2(*argum, **kwargs):
        message = 'Function returned: '+ str(argum) + str(kwargs)
        return message
    return log_1(), log_2()


@logger
def my_func(*args, **kwargs):
    return args, kwargs.values()

print(my_func(5, 6, this=1, that=3))
