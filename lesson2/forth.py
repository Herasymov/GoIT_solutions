n = int(input(": "))
if n > 0:
    k = 1
else:
    k = -1
n = abs(n)
answer = 0
while n:
    answer = answer * 10 + n % 10
    n //= 10
print(k * answer)

# 1
# 1*10 + 2
# 12*10 +3
# 123 = 100 + 20 + 3
# 321 = 300 + 20 + 1
# 321