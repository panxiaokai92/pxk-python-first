#高级特性
###########################################
## 取值前n个元素
r = []
n = 3
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

for i in range(n):
	r.append(L[i])
				
print(r)

#list、tuple的切片（slice）
L = list(range(100))
print(L[0:10])	
print(L[:10])
print(L[-5:])	
print(L[:10:2])		#前10个数，每2个取一个
print(L[::5])			#所有值，每5个取一个
print(L[:])				#原样复制一个list
print('ABCDEFG'[:3])		#字符串切片	
	
###########################################	
#迭代 ：for循环遍历list,tuple,其他可迭代的对象	
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:			
	print(key)

for value in d.values():
	print(value)	
	
for k,v in d.items():
	print("k:"+k)	
	print(v)
	
for ch in "ABC":
	print(ch)	
	
#	怎么判断该对象是否能进行迭代？-- 通过collections模块的Iterable类型
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# enumerate函数把list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
	
for x, y in [(1, 1), (2, 4), (3, 9)]:	
	print(x, y)
	
###########################################
#列表生成式
print(list(range(1, 11)))	

L = []
for x in range(1,11):
	L.append(x*x)
print(L)	

#通过‘列表生成式’改造
print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x%2 == 0])
print([m+n for m in 'ABC' for n in 'XYZ'])

d = {'x':'A','y':'B','z':'C'}
print([k + '=' + v for k, v in d.items()])	

L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])

## instantce函数判断一个变量是不是不字符串
x = 'abc';
y = 123;
print(isinstance(x, str))

###########################################	
#生成器  generator
L = [x * x for x in range(10)]
print(L)

## 取值g的下一个值
g = (x * x for x in range(10))
print(next(g))

for x in g:
    print(x)

##斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

##如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))

## generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)

## 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
       x = next(g)
       print('g:', x)
    except StopIteration as e:
       print('Generator return value:', e.value)
       break


###########################################
#迭代器 Iterator
## Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误

## for循环的对象统称为可迭代对象：Iterable

## 可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

