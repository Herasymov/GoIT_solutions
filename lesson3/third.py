# c = [[11, 1, 1], 2, 3, 4]
# print(len(c[0]))

# <----------------------------->

# c = [[1, 2, 3], [3], [4, 5]]
# print(len(c[0]), len(c[1]), len(c[2]))
# for i in c:
#     print(len(i), end=" ")
# print()

# <---------------------------------->

# c = [[1, 2, 3], [3], [4, 5]]
# answer = []
#
# for i in c:
#     s = 0
#     for j in i:
#         s += j
#     answer += [s]
# print(answer)

# <---------------------------------->

# c = [[1, 2, 3], [3], [4, 5]]
# answer = []
#
# for i in c:
#     answer += [sum(i)]
# print(answer)

#<------------------------------------>

c = [[1, 2, 3], [3], [4, 5]]
answer = []
for i, val in enumerate(c):
    if 3 in val:
        answer += [i]
print(answer)

