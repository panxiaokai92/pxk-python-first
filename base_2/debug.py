# assert断言 调试bug
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError
# 解释器 -O 参数关闭assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')


# logging - debug ,info, warning, error
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


# python调试器： pdb
# 参数-m pdb，定位到下一步要执行的代码


# pdb.set_trace(),需要import pdb
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

