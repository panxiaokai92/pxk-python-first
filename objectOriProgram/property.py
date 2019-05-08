# property装饰器
# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 多继承
#class Dog( A , B)

# 定制类
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    print(Student('pxk'))