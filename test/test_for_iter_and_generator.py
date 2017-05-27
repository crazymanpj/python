# !/usr/bin/env python
# encoding=utf-8
# try:
# 	open(r"")
# except FileNotFoundError as e:
# 	print ("file not exist...")
# except IOError as e:
# 	print ("io error is true...")
# else:
# 	print ("file exist..")
# finally:
# 	print ("always do...")


# class Person():

# 	def __init__(self, name):
# 		self.name = name	
# 		Person.name = name
	
# 	def sayname(self):
# 		print "myname is :" + self.name
# 		print "classname is: " + Person.name

# 	def changeclassname(self, name):
# 		Person.name = name

# 	def __del__(self):
# 		print (self.name + " is realse")

# m = Person("joe")
# m.sayname()
# print "m.name : " + m.name
# m.test="tt"
# print m.test
# j = Person("jason")
# j.sayname()
# j.changeclassname(j.name)
# m.sayname()

# print "-" *100

# class Fibs(object):
# 	"""docstring for Fibs"""
# 	def __init__(self, max):
# 		self.max = max
# 		self.a = 0
# 		self.b = 1

# 	def __next__(self):
# 		fib = self.a
# 		if fib > self.max:
# 			raise StopIteration
# 		self.a, self.b = self.b, self.a + self.b
# 		return fib

# 	#返回迭代器
# 	def __iter__(self):
# 		return self

# fib = Fibs(1000)
# for f in fib:
# 	print(f, end= " ")

# x = list(range(20))
# #获取迭代器
# it = iter(x)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print("-" * 100)
 
# #---------------------------------------------------
# def getfibs(max):
# 	a = 0
# 	b = 1
# 	while a < max:
# 		value = a
# 		a, b= b, a+b
# 		yield value

# print(getfibs(1000))
# for i in getfibs(1000):
# 	print(i)

# #----------------------------------------------------
# def gen():
# 	yield "hello"
# 	yield "how"
# 	yield "are"
# 	yield "you"

# for i in gen():
# 	print(i)
# g= gen()
# print(next(g))
# print(next(g))

# for i in range(2):
# 	print i
# 	print(next(g))




# def test1():
# 	yield 1

# def test2():
# 	for i in test1():
# 		yield i
# 	yield 2

# for i in test2():
# 	print i 

