from collections import namedtuple, deque
# import random
#
# lastname = ["Ivanov", "Petrov", "Kovalev", "Marchenko", "Dennisov"]
# Student = namedtuple("Student", ["last_name", "mark"])
# otlichniki = []
# for i in range(10):
#     s = Student(random.choice(lastname) + str(i), random.randint(1, 5))
#     print(s)
#     if s.mark >= 4:
#         otlichniki.append(s.last_name)
#
# print(f"Otlichniki: {otlichniki}")

# <------------------>

def isAPalindrom(s):
    d = deque(s)
    while d:
        if len(d) == 1:
            return "Yes"
        elif d.pop() != d.popleft():
            return "No"
    return "Yes"

print(isAPalindrom("арозаупаланалапуазора"))