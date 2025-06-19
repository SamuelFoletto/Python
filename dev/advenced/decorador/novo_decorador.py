from decorator import my_decorator, upper_decorator, split_string

@my_decorator
def my_function():
    print('Dentro da função')

my_function()

@upper_decorator
def text():
    return 'Hello World'

print(text())


@split_string
@upper_decorator
def example():
    return 'Aprendendo sobre decoradores do Python'

print(example())