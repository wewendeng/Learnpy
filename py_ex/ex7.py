
"""
高级内容
"""

# 生成器
# 生成器会动态生成一些数据，而不是在使用数据前创建数据然后把这些数据储存起来

# 下面的方法（非生成器）会将所有的值翻倍，并存在double_arr变量中
# 如果iterable很大的话，double_arr将是巨大的
def double_arr(iterable):
    double_arr = []
    for i in iterable:
        double_arr.append(i + i)
    return double_arr

# 运行下面的代码意味着我们首先会将所有的值都加倍然后返回回来
# 最后再检查返回值是否符合特定条件
for value in double_numbers(range(100000)): # test_no_generator
    print(value)
    if value > 5:
        break

# 我们可以使用生成器动态加倍必要的值
def double_numbers_generator(iterable):
    for i in iterable:
        yield i + i

# 使用生成器运行之前的代码
# 现在我们可以根据运行时逻辑一个接一个进行加倍
# 一旦value>5，代码就会break
# 这样我们就不需要把所有的值都加倍一遍了（运行速度会快很多）
for value in double_numbers_generator(range(100000)): # test_generator
    print(value)
    if value > 5:
        break
# 注意到‘range’用在了‘test_no_generator’上，而‘xrange’用在了‘test_generator’上
# 就像‘double_numbers_generator’是‘double_numbers’的生成器一样
# ‘xrange’是‘range’的生成器
# ‘range’会返回包含100000个值的列表
# ‘xrange’会在我们调用的时候动态依次创建100000个值
# Python3中已经舍弃了xrange函数，合并成了range函数

# 你也可以像列表表达一样使用生成器表达式
values = (-x for x in [1, 2, 3, 4, 5])
for x in values:
    print(x) # = -1 -2 -3 -4 -5

# 你也可以直接把生成器转化成列表
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list) # [-1, -2, -3, -4, -5]

# 装饰器
# 装饰器是高阶函数，可以接受函数作为参数并返回函数
# 简单的例子 - add_apples 装饰器会将‘Apple’ 插入into
# 到目标函数（被装饰的函数）get_fruits返回的列表里
def add_apples(func):
    def get_fruits():
        fruits = func()
        fruits.append('Apple')
        return fruits
    return get_fruits

@add_apples
def get_fruits():
    return ["Banana", "Mango", "Orange"]

# 打印出的结果是包含‘Apple’元素的
# Banana, Mango, Orange, Apple
print(','.join(get_fruits())) 

# 下面的例子里面beg装饰了say
# Beg会调用say 如果say_please是True，那么beg会修改say的返回值
# message
def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please i am poor :(")
        return msg
    return wrapper

@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please

print(say()) # Can you buy me a beer
print(say(say_please=True)) # Can you buy me a beer? Please i am poor :)