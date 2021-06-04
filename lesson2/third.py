n = input(": ")
answer = 0
for i in n:
    answer += int(i)
print(answer)

# <--------------------->

n = int(input(": "))
n = abs(n)  # Модуль числа
answer = 0
while n:
    answer += n % 10
    n //= 10 #123
print(answer)
