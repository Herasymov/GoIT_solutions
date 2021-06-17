from collections import Counter


# def func(a, b=5, c=7):
#     print(a, b, c)
#
#
# func(3, 4)
# func(3)
# func(b=1, a=2)

# def func(l):
#     l.reverse()
#
# l1 = [1, 2, 3]
# func(l=l1)
# print(l1)


# <------------------------------>
def func(s=''):
    # return dict(Counter(s))
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d


s = "Hello"
print(func(s))
# {"H": 1, "e": 1, "l": 2, "o": 1}

