
"""
# 高阶-传入函数
def add(x, y, f):   
    return f(x) + f(y)

print(add(-5, -6, abs))
"""

# map函数
def f(x):
    return x * x

r = map(f,[1,2,3,4,5])
R = list(r)
print(R)
