# class A:
# 	def __init__(self):
# 		pass


# 	@staticmethod
# 	def decorator(meth):
# 		def wrapper(*args):
# 			print("argumentsa before calling function --> {}".format(args))
# 			res = meth(*args)
# 			print('function done!')
# 			return res
# 		return wrapper

# 	@decorator
# 	def None_data(self):
# 		pass

# 	@decorator
# 	def with_data(self, a):
# 		return 'hello world' + str(a)



# x = ''

# paramter = x if x else False
# print(paramter)



# requ = ['dum']
# parameter = requ[1] if len(requ) >= 2 else False

# print(parameter)

def test(*args):
	print(type(args))
	# self_, command = args[0:2]
	# parameter = args[2] if len(args)>=2 else False

	# print(self_)
	# print(command)
	# print(parameter)

test('selfi', 'goooo')