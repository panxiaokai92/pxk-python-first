 #list是有序集合
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print(len(classmates))
print(classmates[0])
print(classmates[-1])

#末尾追加元素
classmates.append("Adam")
print(classmates)

#插入指定位置
classmates.insert(1,"Jack")
print(classmates)

#删除末尾元素
classmates.pop()
print(classmates)

#删除指定位置元素
classmates.pop(1)
print(classmates)

#获取php
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][1])


#tuple:有序列表元组，一旦初始化，不能进行修改
tup = (1,2)
print(tup)

#定义一个只有一个元素的元组，需要添加'逗号',为了避免跟tup = (1)混淆
tup = (1)
print(tup)

tup = (1,)
print(tup)

#tuple初始化后，不改变，指的是指向的对象不改变，但该对象的值能变
tup = ('a','b',['A','B'])
tup[2][0] = 'X'
tup[2][1] = 'Y'
print(tup)

#if判断
#birthStr = input("birth: ")
birth = 1990
#birth = int(birthStr)
if birth >= 2000:
		print("00前")
elif	birth >= 1990:	
		print("90后")
else:
		print("管他呢")		
		
#for循环
sum	= 0
list = range(100)
for	x in list:
		sum = x + sum
print(sum)		 		 

#while循环，计算100以内的奇数之和
sum	= 0
n = 99
while n > 0:
		sum = sum + n
		n = n -2
print(sum)		

#注意：break可以结束整个循环，continue结束本轮循环，进入下一轮循环


#dict（类似map）
dic = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dic['Michael'])	

dic['Michael'] = 100
print(dic['Michael'])

#判断dict中的key是否存在
#1
print('Michael' in dic)
#2 get方法,key不存在，可以返回None或者指定的值（如：-1）
print(dic.get('Michaelq',-1))


#set :跟dict类似，一组key的组合，但不存储value。set中没有重复的key
s = set([1,2,3])
print(s)

s.add(4)
s.add(4)
print(s)

