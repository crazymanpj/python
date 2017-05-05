import logging
def funcD(a, b, *c):
	print a
	print b
	print "length of c is %d"%len(c)
	print c


funcD(1,2,3,4)

def funcF(a, **b):
	'test'
	print a
	for x in b:
		print x + ":" +str(b[x])


funcF(100, c='xx', b=200)
print "-" *100
print funcF.__doc__
print help(funcF)
print funcF.__name__

print "-"*100
def outer(func):
	def inner():
		print('do before')
		func()
		print('do after')

	return inner

@outer
def f1():
	print 1+2

f1()

print "-" *100
def use_logging(func):
	def wrapper(*args, **kwargs):
		logging.warn("%s is running"%func.__name__)
		return func(*args, **kwargs)
	return wrapper

@use_logging
def bar():
	print "i am bar"

# bar = use_logging(bar)
# bar()
bar()