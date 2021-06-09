# l = []
# for i in range(2, 11, 2):
#     l.append(i)
# print(l)


# <--------------------->

l = [i for i in range(1, 11) if i % 2 == 0]
print(l)
l2 = [i if not i % 2 else 0 for i in range(1, 11)]
print(l2)
l3 = [0 if i % 2 else 1 for i in range(10)]
print(l3)
l4 = [1 if i % 2 else 0 for i in range(10)]
print(l4)
l5 = [i for i in range(10, 0, -1)]
print(l5)

s = input(": ")
l6 = [i for i in s if i in "aeoyuiAEOYUI"]
print(l6)
l7 = [i for i in s if i not in "aeoyuiAEOYUI"]
print(l7)
l8 = [i for i in s if i in "a e o y u i A E O Y U I".split(" ")]
print(l8)
