
"""
函数
"""

# 用‘def’来定义函数
def add(x, y):
    print("x is {0} and y is {1}".format(x, y))
    return x + y # 用‘return’语句从函数中返回具体的值
# 调用函数并传入参数
print(add(5, 6)) # 打印--x is 5 and y is 6 并返回11
# 另外一种调用方式
print(add(x=5, y=6)) # 结果同上

# 可以定义不定长的固定位置参数
# 使用 *加参数名的方式
# 参数将被解析成元组
def varargs(*args):
    return args
print(varargs(1, 2, 3)) # (1, 2, 3)

# 可以定义不定长的关键字参数
# 使用 *加参数名的方式
# 参数将被解析成字典
def keyword_args(**kwargs):
    return kwargs
# 调用看看
print(keyword_args(big="foot", loch="ness")) # ={"big":"foot", "loch":"ness"}
# 也可以将两种方式结合起来用
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

print(all_the_args(1, 2, a=3, b=4)) 
'''
(1, 2) 
{"a":3, "b":4}
'''

# 调用函数其实就是对‘args’和‘kwargs’做反向操作
# 使用 * 来展开固定位置参数‘args’， 用 ** 去展开关键字参数‘kwargs’
args = (1, 2, 3, 4)
kwargs = {"a":3, "b":4}
print(all_the_args(*args)) # 相当与调用了 foo(1, 2, 3, 4)
print(all_the_args(**kwargs)) # 等于 foo(a=3, b=4)
print(all_the_args(1, 2, 3, 4, a=3, b=4)) # 等于 foo(1, 2, 3, 4, a=3, b=4)

# 你可以将函数参数里的‘args’和‘kwargs’传到其他函数里去
# 分别使用 * 和 **
def pass_all_the_args(*args, **kwargs):
    all_the_args(*args, **kwargs)
    print(varargs(*args))
    print(keyword_args(**kwargs))

# 函数作用域
x = 5

def set_x(num):
    # 本地变量‘x’和全局变量‘x’是不一样的，尽管同名
    x = num # = 43
    print(x)
print(set_x(43))

def set_global_x(num):
    global x
    print(x)
    x = num # 全局变量‘x’现在被设置成6
    print(x)
print(set_global_x(6))

# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_10 = create_adder(10)
print(add_10(3)) # =13

# 这是匿名函数
print((lambda x: x > 2)(3)) # True
print((lambda x, y: x ** 2 + y ** 2)(2, 1)) # = 5

# 这是内置的高阶函数
add_map = map(add_10, [1, 2, 3])
max_map = map(max, [1, 2, 3], [4, 2, 1])
print(add_map) # =[11, 12, 13]
print(max_map) # =[4, 2, 3]

filter_num = filter(lambda x: x > 5, [3, 4, 5, 6, 7])
print(filter_num) # =[6, 7]

# 也可以用字典表达式来构造集合和字典
str_dick = {x for x in 'abcdefghijk' if x in 'abc'}
num_dick = {x: x ** 2 for x in range(5)}
print(str_dick) # ={'a', 'b', 'c'}
print(num_dick) # ={0:0, 1:1, 2:4, 3:9, 4:16}

