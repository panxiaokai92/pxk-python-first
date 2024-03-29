# 协程 coroutine，
# yield from 语法可以让我们方便地调用另一个coroutine

import asyncio
@asyncio.coroutine
def hello():
    print('hello 1')
    for n in range(1, 4):
        print("Hello world!" + str(n))
        # 异步调用asyncio.sleep(1):
        r = yield from asyncio.sleep(1)
        print("Hello again!" + str(n) )

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()



import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# asyncio的异步网络连接来获取sina、sohu和163的网站首页
# 可见3个连接由一个线程通过coroutine并发完成
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()