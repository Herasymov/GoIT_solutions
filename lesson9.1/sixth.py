def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


@logged_func
def complicated(x, y, ):
    return x / y

@logged_func
def summ(x, y):
    return x + y

print(complicated(2, 3))
print(summ(2, 3))
