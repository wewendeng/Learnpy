
"""
模块
"""

# 你可以导入一个模块
import math

print(math.sqrt(16)) # =4

# 你可以从module里面导入一些函数
from math import ceil, floor

print(ceil(3.7)) # =4.0
print(floor(3.7)) # =3.0

# 可以把模块里面所有的函数都导出来
# 注意：不推荐使用这样方法
from math import *

# 模块名是可以有简写的
import math as m

print(math.sqrt(16) == m.sqrt(16)) # True

# Python的模块就是普通的Python文件
# 你可以自己创建模块，然后导入
# 模块就是文件的文件名

# 你可以找出模块定义了那些函数和属性
import math
print(dir(math))

# 如果你有一个math.py的文件
# 并且该文件和你的脚本在同一文件夹下
# 你导入math.py的时候将导入自己的版本
# 而不是Python标准库的math模块
# 这是因为本地文件夹的导入优先级比标准库高