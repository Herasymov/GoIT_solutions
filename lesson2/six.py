#s = input(": ")
#answer = 0
#for i in s:
#    if i in "0123456789":
#        answer += 1
#print(answer)

#<----------------------------->

s = input(": ")
answer = 0
for i in s:
    if i.isdigit():
        answer += 1
print(answer)