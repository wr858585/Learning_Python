
# Task: Get familiar with a range of magic/special methods in class.


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __bool__(self):
        return self._age > 17

    def __gt__(self, other):
        return


p1 = Person('大野', 18)
p2 = Person('小丸子', 16)

result_1 = p1.__bool__()
result_2 = p2.__bool__()
print(result_1)
print(result_2)

