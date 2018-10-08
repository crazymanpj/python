# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-08
# Author:  pangjian
from mock import Mock
fake_obj = Mock()
fake_obj.return_value = 'This is a mock object'
print(fake_obj())

def b():
    print('This is b')

fake_obj.side_effect = b
fake_obj()

# fake_obj.side_effect = KeyError('This is b')
# fake_obj()

fake_obj.fake_a.return_value = 'This is fake_obj.fake_a'
print(fake_obj.fake_a())

fake_obj1 = Mock(side_effect=[1,2,3])
print(fake_obj1())
print(fake_obj1())
print(fake_obj1())
