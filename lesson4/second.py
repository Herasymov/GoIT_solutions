from collections import Counter, defaultdict


# d = {1:2, "hello": "world"}
# print("<------keys------->")
# for i in d.keys():
#     print(i, end=", ")
#
# print("\n<------values------->")
# for i in d.values():
#     print(i, end=", ")
#
# print("\n<-------items------->")
# for key, value in d.items():
#     print(key, ":", value)

# <------------------------------->

# d = {1: 2, 3: 4, 2: 2, 2: 2}
# answer = 0
# for key, value in d.items():
#     if key == 2:
#         answer += 1
#
#     if value == 2:
#         answer += 1
# print(answer)

# <------------------------------->

s = list("hello ")
d = {}

d1 = Counter(s)
print(dict(d1))

d2 = defaultdict(int)
for i in s:
    d2[i] += 1

print(dict(d2))

for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)

