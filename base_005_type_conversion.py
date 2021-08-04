"""
数据类型转换学习
"""
num1 = 1
str1 = '10'

# float转换
print('*********float转化********')
print(float(num1))
print(type(float(num1)))
print(float(str1))

# tuple转换
print('*********tuple转化********')
list1 = [1, 2, 4]
print(tuple(list1))
print(type(tuple(list1)))

# list转化
print('*********list转化********')
tuple1 = (1, 3, 5)
print(list(tuple1))
print(type(list(tuple1)))

# eval 计算字符串中有效的Python表达式
# 注意： eval()表达式中不能是字符串，否则会报错
print('*********eval转化********')
str2 = '1'
str3 = '1.1'
str4 = '(1, 3, 5)'
str5 = '[1, 3, 5, 6]'
print(f'输入的内容是：{str2},type是：{type(str2)}')
print(f'eval结果是：{eval(str2)},eval之后类型是：{type(eval(str2))}')

print(f'输入的内容是：{str3},type是：{type(str3)}')
print(f'eval结果是：{eval(str3)},eval之后类型是：{type(eval(str3))}')

print(f'输入的内容是：{str4},type是：{type(str4)}')
print(f'eval结果是：{eval(str4)},eval之后类型是：{type(eval(str4))}')

print(f'输入的内容是：{str5},type是：{type(str5)}')
print(f'eval结果是：{eval(str5)},eval之后类型是：{type(eval(str5))}')

print(eval('dfd'))

"""
输出结果：
*********float转化********
1.0
<class 'float'>
10.0
*********tuple转化********
(1, 2, 4)
<class 'tuple'>
*********list转化********
[1, 3, 5]
<class 'list'>
*********eval转化********
输入的内容是：1,type是：<class 'str'>
eval结果是：1,eval之后类型是：<class 'int'>
输入的内容是：1.1,type是：<class 'str'>
eval结果是：1.1,eval之后类型是：<class 'float'>
输入的内容是：(1, 3, 5),type是：<class 'str'>
eval结果是：(1, 3, 5),eval之后类型是：<class 'tuple'>
输入的内容是：[1, 3, 5, 6],type是：<class 'str'>
eval结果是：[1, 3, 5, 6],eval之后类型是：<class 'list'>
Traceback (most recent call last):
  File "/Users/maben/Documents/projects/learn/python-base/base_005_type_conversion.py", line 44, in <module>
    print(eval('dfd'))
  File "<string>", line 1, in <module>
NameError: name 'dfd' is not defined
"""
