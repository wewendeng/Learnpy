
"""
控制流
"""

# 定义变量
some_var = 5

# 这是‘if’语句，注意缩进，在Python里面缩进非常重要
# 结果是打印“some_var is smaller than 10”
if some_var < 10 :
    print("some_var is totally bigger than 10")
elif some_var < 10: # elif分支是可选的
    print("some_var is smaller than 10")
else:
    print("some_var is indeed 10")

"""
用‘for’去遍历‘list’
打印结果为：
    dog is manmal
    cat is mammal
    mouse is mammal
"""
for animal in ["dog", "cat", "mouse"]:
    print("{0} is mammal".format(animal))

"""
“range(number)”返回一个列表，列表里包含一组数据
从0到number，不包括number
打印：
    0
    1
    2
    。
    。
"""
for i in range(4):
    print(i)

"""
while会一直循环一直到满足条件位置
打印：
    0
    1
    3
    。
    。
"""
x = 0
while x < 4:
    print(x)
    x += 1  # x = x + 1 的简写

# try/except 代码库用来处理异常
try:
    # 使用raise抛出异常
    raise IndexError
except IndexError as e:
    pass # pass 表示啥都不做，一般情况下，这里会进行异常处理
except (TypeError, IndexError):
    pass # 如果需要的话可以一次性捕抓多个异常
else: # else分支是可选，但必须出现在所有的except后
    print("All good")
finally: # 表示最后一定会执行的
    print("We can clean resources here")

# 除了使用try/finall之外，我们可以适当的使用 with 语句进行简化
with open("myfile.txt") as f:
    for line in f:
        print(line)