

# Python的print语句
print("I am python")
# 从控制台获取输入的简便方法
# input_string_var = raw_input(
#    "Enter some data") # 返回字符串
input_var = input("Enter some data") # 把输入作为Python代码执行
# 警告：使用input方法是必须小心
# Python3没有raw_input方法，只有input方法

# 给变量赋值前不需要声明
some_var = 5 # 一般使用_去给变量分词
print(some_var) # 5

# 没有定义的变量会抛出异常
# print(some_other_var) # Raises a name error

# if可以作为表达式使用
print("yahoo!" if 3 > 2 else 2) # "yahoo!"

# 定义一个非空列表
li = []
# 使用append方法向列表尾部添加元素
li.append(1) # [1]
li.append(2) # [1, 2]
li.append(3) # [1, 2, 4]
li.append(4) # [1, 2, 4, 3]
print(li)
# 使用pop将元素从列表尾部移除
li.pop()
print(li) # [1, 2, 4]

li.append(3)
print(li) # [1, 2, 4, 3]
# 访问列表的元素和访问数组元素语法是相同的
print(li[0]) # 1
# 可以给已经赋值的索引重新赋值
li[0] = 42
print(li[0]) # [42, 2, 4, 3]
# 设置回原先的值
li[0] = 1
print(li) # [1, 2, 4, 3]

# 访问最后一个元素
print(li[-1]) # 3

# 访问越界会抛出异常 IndexError
# print(li[4])

# 使用切片（slice）语法可以访问列表中的部分元素
print(li[1:3]) # [2, 4]
# 忽略开头
print(li[:3]) # [1, 2, 4]
# 忽略结尾
print(li[2:]) # [4, 3]
# 每隔2个元素取一个
print(li[::2])
# 反转列表，即倒转排序
print(li[::-1])

# 使用‘del’来删除列表任何元素
del li[2]
print(li) # [1, 2, 3]

# 列表可以相加，li和other_list都没有变化
other_list = [4, 5, 6]
print(li + other_list) # [1, 2, 3, 4, 5, 6]
# 使用‘extend’方法来连接列表，li列表发生改变
print(li.extend(other_list)) # [1, 2, 3, 4, 5, 6]

# 移除第一个满足条件的值
print(li.remove(2)) # [1, 3, 4, 5, 6]
# print(li.remove(2)) # 抛出异常ValueError，2已经不在列表内

# 在特定的索引（index）插入数据
print(li.insert(1, 2)) # [1, 2, 3, 4, 5, 6]
# 返回第一个满足条件的值的索引
print(li.index(2)) # 1
# print(li.index(7)) # 抛出ValueErro，7不在列表内
# 用‘in’来检查值是否为列表中
print(1 in li) # Ture
# 用‘len（）’来返回列表的长度
print(len(li)) # 6

# 元组跟列表很像，区别是元组是不可变的
tuple = (1, 2, 3)
print(tuple)
print(tuple[0]) # 1
# tuple[0] = 3 # 抛出TyprError异常

# 可以在元组上做一些一下操作
print(len(tuple)) # 3
print(tuple + (4, 5, 6)) # (1, 2, 3, 4, 5, 6)
print(tuple[:2]) # (1, 2)
print(2 in tuple) # True

#可以把元组unpack成变量
a, b, c = (1, 2, 3)
print(a) # 1
print(b) # 2
print(c) # 3
# 不加括号也可以，可以用逗号隔开，但是不用逗号，默认会创建元组，比如 g = 4，5， 6 =>（4， 5， 6）
d, e, f = 4, 5, 6
print(d) # 4
print(e) # 5
print(f) # 6

# 字典是用来存储属性名‘key’和属性值‘value’的
empty_dict = {} # 这是一个空字典
filter_dict = {"one": "1", "two": "2", "three": "3"}
# 用[]来查找属性的值‘value’
print(filter_dict["one"]) # 1
# 用key()来返回所有的key列表，字典key的顺序不保证
print(filter_dict.keys()) # ["one", "two", "three"]
# value()返回所有的value值，排序问题同上
print(filter_dict.values()) # [1, 2, 3]
# items()返回所有的键值对的元组组成的列表
print(filter_dict.items()) # [("one", 1), ("two", 2), ("three", 3)]

# 用‘in’来判断某个属性名或者键是否存在
print("one" in filter_dict) # True
print("1" in filter_dict) # False
print(1 in filter_dict) # False

# 访问不存在的属性名\键时抛出KeyError
# print(filter_dict["four"])

# 用‘get’方法可以避免KeyError
print(filter_dict.get("one")) # 1
print(filter_dict.get("four")) # None
# ‘get’支持当属性名\键不存在时返回一个设定的默认值，但不会设置字典的值
print(filter_dict.get("one", 4)) # 1
print(filter_dict.get("four", 4)) # 4
print(filter_dict)
# 为某个属性名\键赋值和列表方法差不多
filter_dict["four"] = "4"
print(filter_dict) # {"one": 1, "two": 2, "three": 3, "four": 4}

# setdefault方法会给属性名\键不存在是插入具体的值
filter_dict.setdefault("five", "5") # 现在“five”的值为5
print(filter_dict) # {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
filter_dict.setdefault("five", "6") # five的值仍为5
print(filter_dict) # {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

# 集合是存储...好吧，集合（跟列表差不多，只是不能有重复的项）
empty_set = set()
# 初始化的时候赋一些值
some_set = set([1, 2, 2, 3, 4]) # some_set现在等于set([1, 2, 3, 4])

# 顺序是不能被保障了，即使看起来是有顺序的
another_set = set([4, 3, 2, 2, 1]) # anther_set现在是set([1, 2, 3, 4])

# 从Python2.7开始，{}可以用于生命集合
filled_set = {1, 2, 2, 3, 4}
print(filled_set) # {1, 2, 3, 4}

# 往集合里面添更多项
print(filled_set.add(5)) # {1, 2, 3, 4, 5}

# 用&来取交集
other_set = {3, 4, 5, 6}
print(filled_set & other_set) # {3， 4， 5}
# 用 | 来取并集
print(filled_set | other_set) # {1， 2， 3， 4， 5， 6}
# 用 - 来取差集
print(filled_set - other_set) # {1， 2}
# 用 ^ 来取对称差集
print(filled_set ^ other_set) # {1， 2， 6}

# 判断左边的集合是不是右边的超集
print({1, 2} >= {1, 2, 3}) # False
# 判断左边的集合是不是右边的子集
print({1, 2} <= {1, 2, 3}) # True

# 用‘in’来判断元素是否存在
print(2 in filled_set) # True
print(10 in filled_set) # False