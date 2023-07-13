# 默认参数必须放在非默认参数后面：否则如果只传一个参数，不知道是给默认参数还是非默认参数
# def foo(a=2, b):
def foo(b, a=2):
    return a + b


print(foo(3))
print(foo(3, 4))