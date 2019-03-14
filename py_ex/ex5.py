
"""
类
"""

# 以继承一个object方式来定义一个类
class Human(object):
    # 类属性，所有类都共享
    species = "H. sapiens"

    # 基本的构造函数，当类被实例化的时候自动被调用
    # 注意双下划线开头和结尾的变量是Python保留的
    # 你不应该定义类似风格的变量
    def __init__(self, name):
        # 将参数里面的值赋值给同名的实例属性
        self.name = name

        # 初始化属性
        self.age = 0

    # 实例化方法，第一个参数必须是‘self’
    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    # 类方法，所有实例共享
    # 调用的时候，第一个参数代表这个类的本身
    @classmethod
    def get_spcies(cls):
        return cls.species
    
    # 静态方法被调用的时候不需要传入实例或者类的引用（kls，self）的
    @staticmethod
    def grunt():
        return "*grunt*"

    # 属性有点像getter
    # 这个将age()方法变成同名的只读属性（调用的时候不用加括号了）
    @property
    def age(self):
        return self._age 

    # 这样就允许属性被赋值了
    @age.setter
    def age(self, age):
        self._age = age

    # 这样就允许属性被删除
    @age.deleter
    def age(self):
        del self._age 

# 实例化一个类
i = Human(name="Ian")
print(i.say("hi")) # ="Ian:hi"

j = Human("Joel")
print(i.say("hello")) # ="Joel:hello"

# 调用类方法
print(i.get_spcies) # ="H. sapiens"

# 修改类属性
Human.species = "H. neanderthalensis"
print(i.species) # "H. neanderthalensis"
print(j.species) # "H. neanderthalensis"

# 调用静态方法
print(Human.grunt()) # "*grunt*"

# 更新属性
i.age = 42
# 获取属性
print(i.age) # =42

# 删除属性
del i.age
print(i.age)