# def func1():
#     def func2():
#         print(2)
#         return 3
#     print(1)
#     a = func2()
#     print(a)
# func1()
# # func2()
#


# <----------------------->
def summ(a=0, b=0):
    return a + b

def subtraction(a=0, b =0):
    return a - b

def multiplication(a=0, b=0):
    return a * b

def division(a=0, b=1):
    return a / b

def calc(a=0, b=0, c=""):
    if c == "+":
        return summ(a, b)
    elif c == "-":
        return subtraction(a, b)
    elif c == "*":
        return multiplication(a, b)
    elif c == "/" and b != 0:
        return division(a, b)
    else:
        return "Error"


if __name__ == '__main__':
    print(calc(1, 2, "/"))

print(calc(2, 2, "/"))
