

# 输出纯数字
print(3) # =3
# 简单算术
print(1 + 1) # =2
print(8 - 1) # =7
print(10 * 2) # =20
print(35 / 7) # =5

# 除法有点不一样，默认是做整数除法
print(5 / 2) # =2

print(2.0) # 这是浮点数
print(11.0 / 4.0) # =2.75

# 可以强制返回整数，正数负数都可以
print(5 // 3) # =1
print(5.0 / 3.0) # =1.0
print(-5 // 3) # =-2
print(-5.0 / 3.0) # =-2.0

# 可以import division模块
# from __future__ import division
print(11 / 4) # =2.75
print(11 // 4) # =2

# 模\取余操作
print(7 % 3) # =1
# 乘方(x的y次方)
print(2 ** 4) # =16
# 用括号强行改变算术规律
print((1 + 3) * 2) # =8

# 布尔值的操作或者叫逻辑运算
# 主意‘and’和‘or’是分大小写的
print(True and False) # False
print(False or True) # True

# 记住布尔值和整数搅在一起的时候
print( 0 and 2) # =0
print(-5 or 0) # =-5
print(0 == False) # True
print(2 == True) # False
print(1 == True) # False

# 用not来逻辑取反
print(not True) # False
print(not False) # True

# 相等判断用==
print(1 == 1) # True
print(2 == 1) # False

# 不等用!=
print(1 != 1) # False
print(2 != 1) # True

# 更多的比较
print(1 < 10) # Trur
print(1 > 10) # False
print(2 <= 2) # True
print(2 >= 2) # True

# 可以串起来比较
print(1 < 2 < 3) # True
print(2 < 3 < 2) # False

# 用‘’或“”创建字符串
print('This is a string')
print("This is also a string")

# 字符串也是可以相加的
print("Hello" + "World")
# 不用+号也可以相加
print("Hello" "World")
# 甚至也可以相乘
print("Hello" * 3)
# 字符串可以当成是字符组成的列表
print("This is a string"[0])
# 可以拿到字符串的长度
print(len("This is a string"))

# 可以用%格式化字符串
x = 'apple'
y = 'lemon'
print("The items in the basket are %s and %s" %(x, y))

# 新的格式化方式是使用format方法
print("{} is a {}".format("This", "placeholder"))
print("{0} is a {1}".format("string", "formatted"))
# 也可以使用关键词
print("{name} wants to eat {food}".format(name="Bob", food="lasagna"))

# Noce是一个对象
# 所以你是有对象的
print(None)

# 不要用‘==’符号进行对象和None的比较
# 要使用‘is’
print("etc" is None) # False
print(None is None) # True
# ‘is’符号用来测试对象之间的相当性
# 在比较类型的时候可能用处不大
# 不过在对象的比较方面确实非常有用的

# 任何的对象都可以在布尔值的上下文中使用
#  下面的会被认为是false
#   - None
#   - 任何数字类型的0（比如：0，0L，0.0，0j）
#   - 空序列（比如：''，()，[]）
print(bool(0)) # False
print(bool("")) # False