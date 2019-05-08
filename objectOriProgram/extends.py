## 继承
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass


# 判断某个变量是否是某个类型，可以用isinstance判断
a = list()
b = Animal()
isinstance(a, list)
isinstance(b, Animal)

# python动态语言，并不需要object是Animal或者之类有run方法，只要保证传入的对象有一个run方法就可以
class Timer(object):
    def run(self):
        print('Start...')

# 类属性，Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
class Student(object):
    name = 'Student'

s = Student()

# 实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性，但是Student.name仍然可以访问，
# 删除实例属性后，类的name属性就显示出来了
# 注意：千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
print(s.name)
print(Student.name)

s.name = 'Mick'
print(s.name)
print(Student.name)

del s.name
print(s.name)

