
# Python的print语句
print("I am python")
# 从控制台获取输入的简便方法
input_string_var = raw_input(
    "Enter some data") # 返回字符串
input_var = input("Enter some data") # 把输入作为Python代码执行
# 警告：使用input方法是必须小心
# Python3没有raw_input方法，只有input方法

# 给变量赋值前不需要声明
some_var = 5 # 一般使用_去给变量分词
print(some_var) # 5

# 没有定义的变量会抛出异常
print(some_other_var) # Raises a name error

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
print(li.index(7)) # 抛出ValueErro，7不在列表内
# 用‘in’来检查值是否为列表中
print(1 in li) # Ture
# 用‘len（）’来返回列表的长度
print(len(li)) # 6

tuple = (1, 2, 3)
print(tuple)
print(tuple[1])
# tuple[0] = 3

print(len(tuple))
print(tuple + (4, 5, 6))
print(tuple[:2])
print(2 in tuple)

a, b, c = (1, 2, 4)
print(a)
print(b)
print(c)

empty_dict = {}
filter_dict = {"one": "1", "two": "2", "three": "3"}
print(filter_dict["one"])
print(filter_dict.keys())
print(filter_dict.values())
print(filter_dict.items())

print("one" in filter_dict)
print("1" in filter_dict)
print(1 in filter_dict)
# print(filter_dict["four"])

print(filter_dict.get("one"))
print(filter_dict.get("four"))

print(filter_dict.get("one", 4))
print(filter_dict.get("four", 4))
print(filter_dict)

filter_dict["four"] = "4"
print(filter_dict)

filter_dict.setdefault("five", "5")
print(filter_dict)
filter_dict.setdefault("five", "6")
print(filter_dict)