Python 3.8.6 (default, Jan 27 2021, 15:42:20) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[[1,2,3],[4,5,6],[7,8,9]]
>>> b=[]
>>> b=[value for sublist in a for vulue for sublist]
SyntaxError: invalid syntax
>>> b=[value for sublist in a value in sublist]
SyntaxError: invalid syntax
>>> b=[value for sublist in a  for value in sublist]
>>> print(b)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b=[1,2,3,4,5]
>>> c=[]
>>> c=[a*11 for a in b]
>>> print(c)
[11, 22, 33, 44, 55]
>>> 