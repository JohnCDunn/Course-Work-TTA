Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> length = len("How epic are buitl-in functions, huh?")
>>> print length
37
>>> x=23
>>> print str(x)
23
>>> x=2.32
>>> print str(x)
2.32
>>> y = float(40).float(7)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    y = float(40).float(7)
AttributeError: 'float' object has no attribute 'float'
>>> y = float(40)/float(7)
>>> print y
5.71428571429
>>> yInt = int(y)
>>> print yInt
5
>>> print routd(y)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print routd(y)
NameError: name 'routd' is not defined
>>> print round(y)
6.0
>>> print int(round(y))
6
>>> 
