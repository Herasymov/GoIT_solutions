# Создать функции действий(+,-,*,/) и функцию calc куда передаем числа и функцию действия.
# В main сделать ввод 2-х чисел и знака и вызвать функцию calc

def sub(x, y):
    return x - y


def summ(x, y):
    return x + y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y if y != 0 else "Error"


def error(x, y):
    return "Error"


def calc(x, y, func):
    return func(x, y)


dict_op = {
    "+": summ,
    "-": sub,
    "*": mult,
    "/": div
}

n1 = int(input(": "))
n2 = int(input(": "))
sign = input(": ")
print(calc(n1, n2, dict_op.get(sign, error)))
