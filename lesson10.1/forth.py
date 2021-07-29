#написать дополнение к словарю - функцию проверки наличия значения переменной в ключах и значениях
from collections import UserDict


class ValueSearchableDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values() or value in self.data.keys()


as_dict = ValueSearchableDict()
as_dict[1] = 2

print(as_dict.has_in_values(1))    # True
print(as_dict.has_in_values(2))