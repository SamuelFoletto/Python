def my_decorator(function):
    def wrapper():
        print('Antes de executar a função')
        function()
        print('Depois de executar a função')
    return wrapper


def upper_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper


def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper