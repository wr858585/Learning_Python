# Task 1: Get familiar with attributes and methods in class.
print('Task 1: Get familiar with attributes and methods in class.')
print()


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

print('-' * 100)

# Task 2: init method
print('Task 2: init method')


class Person:
    def __init__(self):
        print('init方法执行了')

    def say_hello(self):
        print('你好，我是%s' % self.name)


p1 = Person()
p2 = Person()

# It will display 'init方法执行了' twice even if without calling/printing anything, as init function will run immediately
# when instances are created as per class.

print('-' * 100)


class Person:
    def __init__(self):
        self.name = '小丸子'

    def say_hello(self):
        print('你好，我是%s' % self.name)


p1 = Person()
p2 = Person()

p1.say_hello()      # 你好，我是小丸子

print('-' * 100)


class Person():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('你好，我是%s' % self.name)


p1 = Person('大野')
p2 = Person('杉山')

p1.say_hello()
p2.say_hello()

print('-' * 100)

# Task 3. Create a class named Dog with necessary attributes and methods.


class Dog:
    def __init__(self, name, age, sex, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight

    def bark(self):
        print('对你汪汪叫')

    def bite(self):
        print()
