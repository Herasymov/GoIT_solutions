# написать функцию которая по знаку возращает нужную функцию действия

def sub(x, y):
    return x - y


def summ(x, y):
    return x + y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y if y != 0 else "Error"


def error():
    return "Error"


def calc(sign):
    return dict_op.get(sign, error)


dict_op = {
    "+": summ,
    "-": sub,
    "*": mult,
    "/": div
}

n1 = int(input(": "))
n2 = int(input(": "))
sign = input(": ")
func = calc(sign)
if func != error:
    print(func(n1, n2))
else:
    print(func())
