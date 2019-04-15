#import math

"""
#把定义的数字转换成十六进制
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
"""

# 解一元二次方程
"""
def quadratic(a, b, c):
    sak = b^2-4*a*c
    x1 = 0
    x2 = 0
    if a == 0:
        print("a==0, 此方程非一元二次方程")
    elif sak > 0:
        x1 = (-b + math.sqrt(sak))/(2*a)
        x1 = (-b - math.sqrt(sak))/(2*a)
        print('x1 = d%' %x1)
        print('x2 = d%' %x2)
    elif sak == 0:
        x1 = -b/(2*a)
        x1 = x2
        print('x1 = d%' %x1)
        print('x2 = d%' %x2)
    else:
        print("无解")

a = int(input("请输入a="))
b = int(input("请输入b="))
c = int(input("请输入c="))

quadratic(a, b, c)
"""

# 求x的n次方
"""
def power(x, n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

a = power(5, 3)
print(a)
"""

"""
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

result = calc(1,2,3)
print(result)
"""

# 输入多个数相乘并输出结果
"""
def product(*numbers):
    sum = 1
    for n in numbers:
        sum = sum * n
    return sum
print('product(5) = ', product(5))
print('product(5,6) = ', product(5,6))
print('product(5,6,7) = ', product(5,6,7))
print('product(5,6,7,8) = ', product(5,6,7,8))

if product(5) != 5:
    print("测试失败1！")
elif product(5,6) != 30:
    print("测试失败2！")
elif product(5,6,7) != 210:
    print("测试失败3！")
elif product(5,6,7,8) != 1680:
    print("测试失败4！")
else:
    try:
        product()
        print("测试失败5！")
    except TypeError:
        print("测试成功6！")
"""

"""
# 递归函数1x2x3x...xn
def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)

s = fact(5)
print(s)
"""

"""
# 解决递归调用栈溢出的方法就是通过尾递归优化
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, produce):
    if num ==1:
        return produce
    return fact_iter(num -1, num * produce)

s = fact_iter(4,5)
print(s)
"""

"""
# 利用递归函数解决移动汉诺塔问题
def move(n, a, b, c):
    if n == 1:
        print('move', a , '--->', c) #n=1时直接从a移动到c
    else:
        move(n-1, a, c, b) #先把除了最大的所有圆盘（n-1）移动到b
        move(1, a, b, c) #再把最大的移动到c
        move(n -1, b, a, c) #最后把b上面的所有圆盘（n-1）移动到c

print('---', move(3, 'A', 'B', 'C'))
"""

"""
# 切片,取出列表连续的几个元素
L = ['a', 'b', 'c', 'd']
print(L[1:3]) # 取出索引1-3的元素，但不包括3

# 去除字符串首尾的空格输出
def trim(s):
    if s == None:
        print('输入为空')
    elif s[0] ==' ':
        return s[1:]
    elif s[-1] == ' ':
        return s[:-1]
    else:
        return s

print(trim(' hello hello '))
print(' hello hello ')
"""
"""
# 使用迭代方式找出一个list中的最大值和最小值，并返回一个tuple
def findMinAndMax(L):
    if L == []:
        return (None, None)
    Max=Min = L[0]
    for i in L:
        if Max < i:
            Max = i
        if Min > i:
            Min = i 
    return(Min, Max) #返回一个tuple

if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')
"""

"""
# 列表生成式
a = [x * x for x in range(1,11)]
print(a)
b = [x * x for x in range(1,11) if x % 2 ==0]
print(b)
c = [m + n for m in 'ABC' for n in 'xyz']
print(c)

#列出当前目录下的所有文件名和目录名
import os
d = [ d for d in os.listdir('.')]
print(d)

#输出当前list的字符串并小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
"""

#杨辉三角生成器（未成功）
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')