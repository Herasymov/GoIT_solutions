# keys = [1, 2, 3]
# values = [4, 5, 6]
# d = {}
# for i, val in enumerate(keys):
#     d[val] = values[i]
# print(d)

# <---------------------------->

d = {"math": 4, "english": 5, "biology": 4, "russian": 5, "ukrainian": 3}
# marks = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
marks = {i: 0 for i in range(1, 6)}

# for i in d.values():
#     marks[i] += 1
# print(marks)

print(sum(d.values())/len(d))
# print(max(d.values()))

# keys = [1, 2, 3, 7]
# values = [4, 5, 6]
# print(dict(zip(keys, values)))