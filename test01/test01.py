"""
    作者：zf
    功能：
    版本：1.0
    日期：20181116
    新增功能：
"""
# ['小明'] ['小明'] ['小明']


class Person:
    name = []


p1 = Person()
p2 = Person()
p1.name.append('小明')
print(p1.name)
print(p2.name)
print(Person.name)