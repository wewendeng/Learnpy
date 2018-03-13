
# 使用try-except来保证test.py和该文件都能import count成功
try:
	from .count import A
except ModuleNotFoundError as e:
	from count import A

#from .count import A

class B(A):
	def sub(self, a, b):
		return a - b 

resule = B().add(1, 2)
print(resule)

"""if __name__ == '__main__':
	c = new_add(3, 5)
	print(c)"""