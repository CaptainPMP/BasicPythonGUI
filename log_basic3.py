Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> expenselist = {'rice':'ข้าว','coffee':'กาแฟ','taxi':}
SyntaxError: invalid syntax
>>> 
>>> expenselist = {'rice':'ข้าว','coffee':'กาแฟ','taxi':'ค่าแท็กซี่'}
>>> print(expenselist['])
		  
SyntaxError: EOL while scanning string literal
>>> print(expendelist['rice'])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(expendelist['rice'])
NameError: name 'expendelist' is not defined
>>> print(expenselist['rice'])
ข้าว
>>> print(expenselist['coffee'])
กาแฟ
>>> print(expenselist['taxi'])
ค่าแท็กซี่
>>> expenselist = {'rice':{'name':'ข้าว', 'price':20},'coffee':'กาแฟ','taxi':'ค่าแท็กซี่'}
>>> print(expenselist['rice'])
{'name': 'ข้าว', 'price': 20}
>>> print(expenselist['rice']['name'])
ข้าว
>>> 