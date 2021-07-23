# написать генератор 3 простых чисел между 1 и 10 без повторов
from random import randint
def generator():
    answer = []
    while len(answer)<10:
        print(answer)
        i = randint(1, 10)
        if i not in answer:
            yield i
            answer.append(i)

gen = generator()
k = 0
print("-------------")
next(gen)
print("-------------")
next(gen)
print("-------------")
for i in gen:
    print(k)
    k += 1
    # print(i)