
"""
# 高阶-传入函数
def add(x, y, f):   
    return f(x) + f(y)

print(add(-5, -6, abs))
"""
"""
# map函数 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x

r = map(f,[1,2,3,4,5])
print(list(r))
"""

"""
# sum()累加函数
l1 = [1, 2, 3, 4, 5, 6, 7]
print(sum(l1))

# 利用reduce函数拼接
from functools import reduce
def fn(x, y):
    return x * 10 + y

print(reduce(fn, l1))

# 利用map函数实现首字母大写，其余小写
def normalize(name):
    return name.capitalize()
l2 = ['ada', 'apple', 'Jimi']
print(list(map(normalize,l2)))

# 利用reduce函数实现求积
def mul(x, y):
    return x * y
def prod(L):
    return reduce(mul , L)

print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print("测试成功")
else:
    print("测试失败")
"""

"""
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000', list(output))
if list(filter(is_palindrome, range(1, 40))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33]:
    print("Ture")
else:
    print("False")
"""

# 排序
a = [1, 4, 6, 3,7]
b = sorted(a)  # 从小到大
c = sorted(a,reverse=True)  # 从大到小
print(b)
print(a)
print(c)

def by_name(t):
    return t[0].lower()

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key= by_name)
print(L2)

        

