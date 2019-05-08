# type()函数判断基本类型
print(type(123))

type(123) == type(456)
type(123) == int
type('abc') == type('123')
type('abc') == str
type('abc') == type(123)


# type() 等同于 isinstance()
isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)

isinstance([1, 2, 3], (list, tuple))

# types 判断是否是函数
import types

def fn():
    pass

type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType


# len()函数获取对象长度
len('ABC')
'ABC'.__len__()

'ABC'.lower()

# dir() 获得一个对象的所有属性和方法
dir('ABC')

# getattr(), setattr(), hasattr() 操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x')
hasattr(obj, 'y')
setattr(obj, 'y', 19)

getattr(obj, 'y')

# 获取default参数，参数不存在，就返回默认值
getattr(obj,'z',404)


