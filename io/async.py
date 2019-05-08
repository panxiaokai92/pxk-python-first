#  为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读


# async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
# 1/ 把@asyncio.coroutine替换为async
# 2/ 把yield from替换为await

# 老代码
import asyncio
@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 新代码
async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")