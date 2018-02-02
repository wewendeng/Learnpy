#import math

"""
#把定义的数字转换成十六进制
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
"""

"""
#解一元二次方程
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