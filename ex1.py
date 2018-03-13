

import time
"""

# 输出指定格式的时间
nowtime = int(time.time())
print(nowtime)

timestruct = time.localtime(nowtime)
strTime = time.strftime("%Y-%m-%d", timestruct)
print(strTime)
"""
now_time = time.strftime("%Y-%m-%d %H-%M-%S")
print(now_time)
"""
# 判断文件是否存在
import os

if os.path.exists("README.md"):
    print("falus")
"""

# 排序
a = [1, 4, 6, 3,7]
b = sorted(a)  # 从小到大
c = sorted(a,reverse=True)  # 从大到小
print(b)
print(a)
print(c)