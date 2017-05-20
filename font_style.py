'''
A decoratot that adds html tags for font style to a function that returns text
'''


def cursive(my_function):
    def decorate_with_cursive(text):
        return '<i>' + my_function(text) + '</i>'

    return decorate_with_cursive

def bold(my_function):
    def decorate_with_bold(text):
        return '<b>' + my_function(text) + '</b>'
    return decorate_with_bold

@cursive
@bold
def my_function(text):
    assert text == str(text)
    return text

print (my_function('text'))