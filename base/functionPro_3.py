## 匿名函数 =========================================
## 关键字lambda表示匿名函数，冒号前面的x表示函数参数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

f = lambda x: x * x
f(5)

## 匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


## 装饰器  decorator ================================
## 在代码运行期间动态增加功能的方式，称之为“装饰器",本质上，decorator就是一个返回函数的高阶函数
## 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2015-3-25')

f = now
f()

## name属性可以拿到函数名
print(now.__name__)
print(f.__name__)

## now = log(now)
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()


## 偏函数  partial
import functools
print(int('12345', base=8))

def int2(x, base=2):
    return int(x,base)

print(int2('100000'))

## functions.partial, 某些参数设置默认值，返回一个新函数，调用新函数
int3 = functools.partial(int, base=2)
print(int3('1000000'))

print(int3('100000', base=10))
