def calc(num1, num2, sign):
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "*":
        return num1 * num2
    elif sign == "/" and num2 != 0:
        return num1 / num2
    return "error"

a = int(input(": "))
b = int(input(": "))
print(calc(2, 3, "*"))
print(calc(2, 3, "-"))
print(calc(2, 3, "+"))
print(calc(2, 3, "/"))
print(calc(2, 0, "/"))
print(calc(a, b, "/"))
print(calc(int(input(": ")), int(input(": ")), "/"))
