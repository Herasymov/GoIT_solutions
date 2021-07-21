def adder(val):
    def inner(x):
        return x + val
    return inner


two_adder = adder(2)
#    def two_adder(x):
#         return x + 2
print(two_adder(3)) # 5
print(two_adder(5)) # 7
print( adder(2)(3) )
#    def three_adder(x):
#         return x + 3
three_adder = adder(3)
print(three_adder(5))   # 8
print(three_adder(-3))  # 0

print( adder(2)(3) )