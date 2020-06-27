Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'apple'
>>> price = 2121351354
>>> print(f'list: {name} price:{price}')
list: apple price:2121351354
>>> print(f'list: {name} price:{price:,d}')
list: apple price:2,121,351,354
>>> account = 54646.5475574
>>> print('list: {} price: {:,.2f}'.format(name,account))
list: apple price: 54,646.55
>>> print(f'list: {name} price:{account:,.0f}')
list: apple price:54,647
>>> import math
>>> x = 13.35
>>> round(x)
13
>>> x = 13.50
>>> round(x)
14
>>> round(13.4999999999)
13
>>> math.ceil(13.4)
14
>>> 