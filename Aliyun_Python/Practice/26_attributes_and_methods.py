# Task: Get familiar with attributes and methods in class.


class Person:
    type = 'mammal'

    def say_hello(self):
        print(self)


p1 = Person()
p2 = Person()

p1.name = '大野'
p2.name = '杉山'

p1.say_hello()
print(p1)
p2.say_hello()
print(p2)
