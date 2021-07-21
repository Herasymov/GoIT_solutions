from collections import Counter, defaultdict, OrderedDict
d = {}
s = "qwerty 1234 qwerty"
print(s)
# d = dict(Counter(s))
# print(d)


# for i in s:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1


# d = defaultdict(int)
# for i in s:
#     d[i] += 1
# print(dict(d))


for i in s:
    d[i] = 1
d['q'] = 2
print(d)

d2 = OrderedDict()
for i in s:
    d2[i] = 1
d2['q'] = 2
print(d)