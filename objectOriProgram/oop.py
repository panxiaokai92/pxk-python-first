# 面向过程
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print_score(std1)
print_score(std2)

## 面向对象编程
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self_1):
        print('%s: %s' % (self_1.name, self_1.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


# 特殊方法“__init__”前后分别有两个下划线！
# self 表示的是实例本身，不需要传值


# 属性名前双下划线'__'，私有变量private，内部访问，外部不能访问，例如：__name, 被包装成 _Student_name
# 通过get/set方法访问、赋值

# 属性名前单下划线'_', 外部可以访问，但是当看到这个变量时，意思：虽然我可以被访问，但是，请把我视为私有变量，不要随意访问

# 属性名前后 双下划线'__'(__xx__),特殊变量，可以直接访问，不是private变量
