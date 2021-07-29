class Mammal:
    phrase = ''
    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'



class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'

class Person:
    phrase = "Hello, World!"


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


def example_func(animal):
    a = animal()
    print(a.phrase)


rec = Recorder

r = rec()
cat = Cat()
dog = Dog()
example_func(Cat)
person = Person()
strange_animal = Chupakabra()

r.record_animal(cat)            # Recorded "Meow!"
r.record_animal(dog)            # Recorded "Bark!"
r.record_animal(strange_animal) # Recorded "Whooooo!!!"
