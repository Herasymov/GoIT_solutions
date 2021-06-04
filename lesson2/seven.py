# 4! = 1*2*3*4 =24
# 5! = 1*2*3*4*5 = 120
# n! = 1*2*....*n
# 0! = 1

#<------for------->
# n = int(input(": "))
# ans = 1
# for i in range(1, n+1):
#     ans *= i
# print(f"{n}! = {ans}")

#<------while------->
n = int(input(": "))
ans = 1
while n:
    ans *= n
    n -= 1
print(f"{n}! = {ans}")
