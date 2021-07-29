import string
import module


class NameTooShortError(Exception):
    print('Name is too short, need more than 3 symbols. Try again.')


class NameStartsFromLowError(Exception):
    print('Name should start from capital letter. Try again.')


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


ch = 0
while ch < 3:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        ch += 1
    except NameStartsFromLowError:
        ch += 1
print("YYYYY")