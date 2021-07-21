from collections import namedtuple
# person = tuple([1, 2])
# print(person)
Person = namedtuple('Person', ['name', 'age'])
person = Person("Masha", 18)
person = Person("Vasya", 21)
print(person)
print(person.name)
print(person.age)
