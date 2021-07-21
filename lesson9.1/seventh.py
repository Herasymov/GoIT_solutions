#сделать глобальную переменную age. Написать функцию которая делает print("Hello, world!")
#написать декоратор который заменяет вывод функции, если age < 18
AGE = 11

def check(func):
    global AGE
    if AGE >= 18:
        func()
    else:
        print("Deny")

@check
def hello_world():
    print("Hello, World!")

hello_world