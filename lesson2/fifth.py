login = "admin"
password = "root"
ans = 1
while ans == 1:
    l = input("Enter login: ")
    p = input("Enter password: ")
    if l == login and p == password:
        print("Welcome!")
        break
    ans = int(input("Error! Would you like to continue?(1 - yes): "))
print("See you next time!")
