Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dictionary_name = {'item_1':1, 'item_2':2, 'item_3':3}
>>> print dictionary_name['item_1']
1
>>> epic_programmers_dict = ["Tim Berners-lee" : 'tbl@gmail.com',"Guido van Rossum" : 'gvr@gmail.com', "Linus Torvalds" : lt@gmail.com', }

SyntaxError: invalid syntax
>>> epic_programmers_dict = ["Tim Berners-lee" : 'tbl@gmail.com',"Guido van Rossum" : 'gvr@gmail.com', "Linus Torvalds" : 'lt@gmail.com', }
SyntaxError: invalid syntax
>>> epic_programmers_dict = ["Tim Berners-lee" : 'tbl@gmail.com',"Guido van Rossum" : 'gvr@gmail.com', "Linus Torvalds" : 'lt@gmail.com', ]
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
>>> print epic_programmers_dict
{'Guido van Rossum': 'gvr@gmail.com', 'Tim Berners-lee': 'tbl@gmail.com', 'Linus Torvalds': 'lt@gmail.com'}
>>> print epic_programmers_dict["Tim Berners-lee"]
