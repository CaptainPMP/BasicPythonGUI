Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Hello():
	print('Hello Rebert')

	
>>> Hello()
Hello Rebert
>>> def Sawatdee(name):
	print('สวัสดีครับ')
	print('สบายดีไหม '+ name)
	print('-----')

	
>>> Sawatdee(Captain)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    Sawatdee(Captain)
NameError: name 'Captain' is not defined
>>> Sawatdee('Captain')
สวัสดีครับ
สบายดีไหม Captain
-----
>>> Sawatdee('แมนยู')
สวัสดีครับ
สบายดีไหม แมนยู
-----
>>> 