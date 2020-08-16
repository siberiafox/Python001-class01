from time import time
from functools import wraps

"""
list: 容器序列 & 可变序列
tuple: 容器序列 & 不可变序列
str: 扁平序列 & 不可变序列
dict：容器序列 & 可变序列
collections.deque： 容器序列 & 可变序列
"""

num = 0

def my_map(func, *iterable_obj):
    try:
        if len(iterable_obj) == 1:
            for i in iterable_obj:
                yield func(i)
        else:
            for args in zip(*iterable_obj):
                yield func(*args)
    except TypeError:
        print('error: obj must be iterable')

g = my_map(lambda x, y: x+y, [1, 2, 3], [100, 1])
print(list(g))

def printer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        avg_runtime = func(*args, **kwargs)
        print(f'args: {args},{kwargs}')
        print(f'{inner.__name__} func avg_runtime is: {avg_runtime:.5f} s')
    return inner

def timer(num_loop):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start = time()
            for _ in range(num_loop):
                func(*args, **kwargs)
            end = time()
            return (end - start) / num_loop
        return inner
    return outer

@printer
@timer(5)
def counter(begin, end = 10000000):
    global num
    for i in range(begin, end):
        num += 1

counter(0, end = 10000000)

print(f'after counter func processed,global var num equals {num}')
