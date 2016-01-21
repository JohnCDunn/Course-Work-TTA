Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = "Guido"
>>> print name(0)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print name(0)
TypeError: 'str' object is not callable
>>> print name
Guido
>>> print name(1)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print name(1)
TypeError: 'str' object is not callable
>>> print name.upper()
GUIDO
>>> print name.lower()
guido
>>> print name.capitalize()
Guido
>>> date="11/12/2015"
>>> date_manip = date.split('/')
>>> print date_manip
['11', '12', '2015']
>>> print date_manip[0]
11
>>> print date_manip[1]
12
>>> print date_manip[2]
2015
>>> print 'Month: ' + date_manip[0]
Month: 11
>>> print 'Day" ' + date_manip[1]
Day" 12
>>> print 'Year: ' + date_manip[2]
Year: 2015
>>> print (Month: ' + date_namip[0] +
       
SyntaxError: invalid syntax
>>> print ('Month: ' + date_manip[0] + ' Day: ' + date_manip[1] + ' Year: ' + date_manip[2])
Month: 11 Day: 12 Year: 2015
>>> 
