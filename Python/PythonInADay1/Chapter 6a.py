Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x == 5

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x == 5
NameError: name 'x' is not defined
>>> print x == 5

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print x == 5
NameError: name 'x' is not defined
>>> x = 5
>>> print x == 5
True
>>> print x == 4
False
>>> print x < 7
True
>>> print x > 7
False
>>> print x != 3
True
>>> print x >= 5
True
>>> print x <= 5
True
>>> print x > 5
False
>>> x = 10
>>> ================================ RESTART ================================
>>> 
x = 10
>>> 
