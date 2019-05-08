# 动态给实例、类绑定属性，方法
class Student(object):
    pass

s = Student()
s.name = 'Mick'

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

# 给一个实例绑定方法，对另一个实例是不起作用的，对类绑定方法，所有实例起作用
s2 = Student()
#s2.set_age(25)   # 会提示异常

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)

# slots 限制实例的属性
class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'pxk'
s.age = 12
s.score = 23    # 由于score没有在slots的列表中，不能绑定属性

# 注意：__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的




