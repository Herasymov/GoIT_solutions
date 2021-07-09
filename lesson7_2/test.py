login = input(": ")
password = input(": ")
c = 0
with open('test.txt', 'r') as f:
    for line in f:
        parts = line.split(" ")
        if parts[0] == login and parts[1][:-1] == password:
            print("Access")
            c = 1
            break
    if not c:
        print("Wrong")