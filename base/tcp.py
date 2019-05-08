## tcp连接
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.baidu.com",80))

s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com \r\nConnection: close\r\n\r\n')

buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#关闭连接
s.close()


## 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)


# 监听端口:
s.bind(('127.0.0.1', 9999))