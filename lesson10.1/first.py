class Human:
    name = ''
    def voice(self):
        print(f"Hello! My name is {self.name}")


class Developer(Human):
    field_description = "My Programming language"
    value = ""

    def make_some_code(self):
        return f"{self.field_description} is {self.value}"


class PythonDeveloper(Developer):
    name = "Slava"
    value = "Python"

    def voice(self):
        print(f"Hello! I'm {self.name}")


class JSDeveloper(Developer):
    value = "JavaScript"


p_dev = PythonDeveloper()
p_dev.voice()   # Hello! My name is Bob
print(p_dev.make_some_code())  # My Programming language is Python


js_dev = JSDeveloper()
js_dev.name = "Bob"
js_dev.voice()
print(js_dev.make_some_code())  # My Programming language is JavaScript

c_dev = Developer()
c_dev.value = "c"
print(c_dev.make_some_code())
