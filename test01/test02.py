"""
    作者：zf
    功能：
    版本：1.0
    日期：20181116
    新增功能：
"""
# 小红 小明 小明


class Person:
    name = '小明'


p1 = Person()
p2 = Person()
p1.name = '小红'
print(p1.name)
print(p2.name)
print(Person.name)


# 解析:
# 类变量就是供类使用的变量,实例变量就是供实例使用的。
# 这里p1.name="小红"是实例调用了类变量，就是函数传参的问题，p1.name一开始是指向的类变量name="小明"，
# 但是在实例的作用域里把类变量的引用改变了，就变成了一个实例变量。
# self.name不再引用Person的类变量name了。
