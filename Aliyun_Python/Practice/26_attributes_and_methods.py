# Task: Get familiar with attributes and methods in class.


class Person:
    type = 'mammal'

    def say_hello(self):
        print(self)


p1 = Person()
p2 = Person()

p1.name = '大野'
p2.name = '杉山'

p1.say_hello()      # <__main__.Person object at 0x02D61F58>
print(p1)           # <__main__.Person object at 0x02D61F58>
p2.say_hello()      # <__main__.Person object at 0x02D7D040>
print(p2)           # <__main__.Person object at 0x02D7D040>
