# s = input(": ")
# c = 0
# for i in range(len(s)):
#     if s[i] == "a":
#         c = 1
#         print(i)
#         break
# if not c:
#     print(-1)
#
# #<--------------------------------->
#
# s = input(": ")
# if "a" not in s:
#     print(-1)
# else:
#     for i in range(len(s)):
#         if s[i] == "a":
#             print(i)
#             break

#<--------------------------------->
s = input(": ")
if "a" not in s:
    print(-1)
else:
    for i, val in enumerate(s):
        if val in "aA":
            print(i)
            break