Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list()
[]
>>> list1 = []
>>> type(list1)
<class 'list'>
>>> list1.append(123)
>>> list1
[123]
>>> list1.append(4.56)
>>> list1
[123, 4.56]
>>> list1.append(True)
>>> list1
[123, 4.56, True]
>>> list1.append("Hello")
>>> list1
[123, 4.56, True, 'Hello']
>>> list1.append([1, 2, 3, 4, 5])
>>> list1
[123, 4.56, True, 'Hello', [1, 2, 3, 4, 5]]
>>> None
>>> print(None)
None
>>> print(list1.append(123))
None
>>> list1
[123, 4.56, True, 'Hello', [1, 2, 3, 4, 5], 123]
>>> list1[0]
123
>>> list1[5]
123
>>> list1[4]
[1, 2, 3, 4, 5]
>>> list1[-1]
123
>>> list1[-2]
[1, 2, 3, 4, 5]
>>> list1[-6]
123
>>> list1
[123, 4.56, True, 'Hello', [1, 2, 3, 4, 5], 123]
>>> list1.insert(4, 20)
>>> list1
[123, 4.56, True, 'Hello', 20, [1, 2, 3, 4, 5], 123]
>>> list1.insert(0, 20)
>>> list1
[20, 123, 4.56, True, 'Hello', 20, [1, 2, 3, 4, 5], 123]
>>> list1.insert(100, 20)
>>> list1
[20, 123, 4.56, True, 'Hello', 20, [1, 2, 3, 4, 5], 123, 20]
>>> list1.insert(-1, 100)
>>> list1
[20, 123, 4.56, True, 'Hello', 20, [1, 2, 3, 4, 5], 123, 100, 20]
>>> list1.insert(-5, 100)
>>> list1
[20, 123, 4.56, True, 'Hello', 100, 20, [1, 2, 3, 4, 5], 123, 100, 20]
>>> list1.insert(-500, 100)
>>> list1
[100, 20, 123, 4.56, True, 'Hello', 100, 20, [1, 2, 3, 4, 5], 123, 100, 20]
>>> print(list1.insert(6, 60))
None
>>> list1
[100, 20, 123, 4.56, True, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20]
>>> list1.extend("Hello")
>>> list1
[100, 20, 123, 4.56, True, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'l', 'o']
>>> list1.extend([1, 2, 3, 4, 5])
>>> list1
[100, 20, 123, 4.56, True, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5]
>>> list1.extend(123)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list1.extend(123)
TypeError: 'int' object is not iterable
>>> list1.extend(1.345)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    list1.extend(1.345)
TypeError: 'float' object is not iterable
>>> list1.extend(False)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list1.extend(False)
TypeError: 'bool' object is not iterable
>>> list1.extend({10, 20, 30})
>>> list1
[100, 20, 123, 4.56, True, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5, 10, 20, 30]
>>> list1.pop()
30
>>> list1
[100, 20, 123, 4.56, True, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5, 10, 20]
>>> value = list1.pop(-1)
>>> value
20
>>> list1
[100, 20, 123, 4.56, True, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> print(list1.pop(4))
True
>>> list1
[100, 20, 123, 4.56, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> list1.pop(100)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    list1.pop(100)
IndexError: pop index out of range
>>> list1.pop(-100)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    list1.pop(-100)
IndexError: pop index out of range
>>> list1
[100, 20, 123, 4.56, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> list1.remove('l')
>>> list1
[100, 20, 123, 4.56, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> list1.remove(100)
>>> list1
[20, 123, 4.56, 'Hello', 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> list1.remove("""Hello""")
>>> list1
[20, 123, 4.56, 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> list1.remove('''Hello''')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list1.remove('''Hello''')
ValueError: list.remove(x): x not in list
>>> list1.clear()
>>> list1
[]
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list1 = [20, 123, 4.56, 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> list1
[20, 123, 4.56, 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> 'H' in list1
True
>>> 'Hello' in list1
False
>>> list1.count(20)
3
>>> list1.count(100)
2
>>> list1.count(5)
1
>>> list1
[20, 123, 4.56, 60, 100, 20, [1, 2, 3, 4, 5], 123, 100, 20, 'H', 'e', 'l', 'o', 1, 2, 3, 4, 5, 10]
>>> list1.count("Hello")
0
>>> list1.index(60)
3
>>> list1.index(20)
0
>>> list1.index("Hello")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    list1.index("Hello")
ValueError: 'Hello' is not in list
>>> list1 = [1, 2, 3, 4, 5]
>>> list1.reverse()
>>> print(list1)
[5, 4, 3, 2, 1]
>>> list1
[5, 4, 3, 2, 1]
>>> print(list1.reverse())
None
>>> list1
[1, 2, 3, 4, 5]
>>> list1 = [8, 4, 9, 6, 2, 7]
>>> list1.sort()
>>> list1
[2, 4, 6, 7, 8, 9]
>>> list1 = [8, 4, 9, 6, 2, 7]
>>> list1.sort(reverse = True)
>>> list1
[9, 8, 7, 6, 4, 2]
>>> list1 = [8, 4, 9, 6, 2, 7]
>>> list1.sort()
>>> list1.reverse()
>>> list1
[9, 8, 7, 6, 4, 2]
>>> len, list, str, int
(<built-in function len>, <class 'list'>, <class 'str'>, <class 'int'>)
>>> len(list1)
6
>>> len(123456)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    len(123456)
TypeError: object of type 'int' has no len()
>>> num1 = 5
>>> num2 = 5
>>> num1 ==  num2
True
>>> num1 is num2
True
>>> str1 = "Hello World !"
>>> str2 = "Hello World !"
>>> str1 == str2
True
>>> str1 is str2
False
>>> str1 = "Hello"
>>> str2 = "Hello"
>>> str1 == str2
True
>>> str1 is str2
True
>>> float1 = 1.456
>>> float2 = 1.456
>>> float1 == float2
True
>>> float1 is float2
False
>>> num1 = 12345
>>> num2 = 12345
>>> num1 == num2
True
>>> num1 is num2
False
>>> num1 = 56
>>> num2 = 56
>>> num1 == num2
True
>>> num1 is num2
True
>>> str1 = "Hello"
>>> str2 = "Hii"
>>> str3 = "Hello"
>>> str1 == str3
True
>>> str1 is str3
True
>>> id(str1)
1968810945968
>>> id(str3)
1968810945968
>>> id(str2)
1968810943984
>>> num1 = 56
>>> num2 = 56
>>> id(num1)
1968773550160
>>> id(num2)
1968773550160
>>> id(56)
1968773550160
>>> list1 = [1]
>>> list2 = [1]
>>> list1 == list2
True
>>> list1 is list2
False
>>> list1 = [1, 2, 3, 4, 5]
>>> list2 = [1, 2, 3, 4, 5]
>>> list1 == list2
True
>>> list1 is list2
False
>>> id(list1)
1968810200832
>>> id(list2)
1968810993344
>>> list3 = list1
>>> id(list3)
1968810200832
>>> list1 == list3
True
>>> list2 == list3
True
>>> list1 is list2
False
>>> list1 is list3
True
>>> list1.append(6)
>>> list1
[1, 2, 3, 4, 5, 6]
>>> list3
[1, 2, 3, 4, 5, 6]
>>> list3.clear()
>>> list3
[]
>>> list1
[]
>>> list1 = [1, 2, 3, 4, 5]
>>> list3 = list1.copy()
>>> list1
[1, 2, 3, 4, 5]
>>> list3
[1, 2, 3, 4, 5]
>>> list1 == list3
True
>>> list1 is list3
False
>>> list1.clear()
>>> list1
[]
>>> list3
[1, 2, 3, 4, 5]
>>> list1 = [1, 9, 4, 8, 2, 1, 9, 2, 4, 6, 5]
>>> list1
[1, 9, 4, 8, 2, 1, 9, 2, 4, 6, 5]
>>> list1.sort()
>>> list1
[1, 1, 2, 2, 4, 4, 5, 6, 8, 9, 9]
>>> list1 = ["z", '', '', '', '', ''"a", 'abc', "ab", 'zab']
>>> list1 = ["z", 'aa', 'za', 'zb', 'aac', 'ad', 'zabd', "a", 'abc', "ab", 'zab', 'bcd', 'f', 'aag']
>>> list1
['z', 'aa', 'za', 'zb', 'aac', 'ad', 'zabd', 'a', 'abc', 'ab', 'zab', 'bcd', 'f', 'aag']
>>> list1.sort()
>>> list1
['a', 'aa', 'aac', 'aag', 'ab', 'abc', 'ad', 'bcd', 'f', 'z', 'za', 'zab', 'zabd', 'zb']
>>> list1 = ['z', 'aa', 'za', 'zb', 'aac', 'ad', 'zabd', 'a', 'abc', 'ab', 'zab', 'bcd', 'f', 'aag']
>>> list1.sort(key = len)
>>> list1
['z', 'a', 'f', 'aa', 'za', 'zb', 'ad', 'ab', 'aac', 'abc', 'zab', 'bcd', 'aag', 'zabd']
>>> list1 = ['z', 'aa', 'za', 'zb', 'aac', 'ad', 'zabd', 'a', 'abc', 'ab', 'zab', 'bcd', 'f', 'aag']
>>> list1.sort()
>>> list1.sort(key = len)
>>> list1
['a', 'f', 'z', 'aa', 'ab', 'ad', 'za', 'zb', 'aac', 'aag', 'abc', 'bcd', 'zab', 'zabd']
>>> print(1, 2, 3)
1 2 3
>>> print(1, 2, 3, end = "Hello")
1 2 3Hello
>>> print(1, 2, 3, end = "\n")
1 2 3
>>> print(1, 2, 3, sep = "-")
1-2-3
>>> print(1, 2, 3, sep = "---------")
1---------2---------3
>>> print(1, 2, sep = "---------")
1---------2
>>> print(1, sep = "---------")
1
>>> print(1, end = "---------")
1---------
>>> 
= RESTART: C:/Users/admin/Desktop/2023/NBKR - Nov - 2/maximum in list.py
5
1
2
3
4
5
1 2 3 4 5 
>>> input()
asfgy 2 ui32r bs
'asfgy 2 ui32r bs'
>>> 'asfgy 2 ui32r bs'.split()
['asfgy', '2', 'ui32r', 'bs']
>>> 'asfgy 2 ui32r bs'.split(" ")
['asfgy', '2', 'ui32r', 'bs']
>>> 'asfgy 2 ui32r bs'.split("2")
['asfgy ', ' ui3', 'r bs']
>>> input()
1 2 3 4 5 6 7 8 9
'1 2 3 4 5 6 7 8 9'
>>> '1 2 3 4 5 6 7 8 9'.split()
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
<map object at 0x0000015A434D0A90>
>>> list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9']))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(map(int, input().split()))
1 2 3 4 5 6
[1, 2, 3, 4, 5, 6]
>>> 
= RESTART: C:/Users/admin/Desktop/2023/NBKR - Nov - 2/maximum in list.py
5
1 2 3 4 5
1 2 3 4 5 
>>> size
5
>>> list1
[1, 2, 3, 4, 5]
>>> for i in range(size):
	print(list1[i], end = " ")

	
1 2 3 4 5 
>>> for i in list1:
	print(i, end = " ")

	
1 2 3 4 5 
>>> size = 5
>>> for i in range(size):
	print(i, end = " ")

	
0 1 2 3 4 
>>> for i in range(size):
	i += 1
	print(i, end = " ")

	
1 2 3 4 5 
>>> for i in range(size):
	i += 2
	print(i, end = " ")

	
2 3 4 5 6 
>>> size
5
>>> for i in range(size):
	size += 1
	print(i, end = " ")

	
0 1 2 3 4 
>>> size
10
>>> 
= RESTART: C:/Users/admin/Desktop/2023/NBKR - Nov - 2/maximum in list.py
5
1 2 3 4 5 6 7 8 9
1 2 3 4 5 
>>> 
= RESTART: C:/Users/admin/Desktop/2023/NBKR - Nov - 2/maximum in list.py
5
1 2 3 4 5 6 7 8 9
1 2 3 4 5 1
2
3
4
5
6
7
8
9
>>> 