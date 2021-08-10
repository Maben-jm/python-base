"""
list方法学习
"""
list1 = ['hello', 'world', 'hi', 'his', 'her', 'hi']

print('******************start******************')
# index(数据，开始下标，结束下标) 返回首次出现的位置和str的语法一致
print('# index')
# print(list1.index('h'))# 找不到会报错
print(list1.index('hi'))  # 2
print(list1.index('hi', 3))  # 5

# count(数据) 返回出现的总次数
print('# count')
print(list1.count('hi'))  # 2
print(list1.count('h'))  # 0

# len(数据) 返回数据的长度
print('# len')
print(len(list1))  # 6

# in  如果数据在列表中返回True
print('# in')
print('hi' in list1)  # True
print('h' in list1)  # False

# not in 如果数据不再列表中返回True
print('# not in')
print('hi' not in list1)
print('d' not in list1)

# append(数据) 列表增加数据
print('# append')
list1.append('she')
list1.append('she')
print(list1)  # ['hello', 'world', 'hi', 'his', 'her', 'hi', 'she', 'she']
list1.append(['her', 'his'])
print(list1)  # ['hello', 'world', 'hi', 'his', 'her', 'hi', 'she', 'she', ['her', 'his']]

# extend(数据)
list2 = ['1', '2']
print('# extend')
list2.extend('3')
# list2.extend(4) # 报错
print(list2)
list2.extend(['3', '4'])
print(list2)  # ['1', '2', '3', '3', '4']

# insert(位置坐标,数据)
print('# insert')
list2.insert(1, '7')
print(list2)
list2.insert(10, '8')  # 超出最大，会在最后添加
print(list2)

# del 删除
print('# del')
# del list1
# print(list1)  # 报错 因为整个list1已经被删除了
del list1[0]
print(list1)  # 不会报错，只是删除的第一个

# pop(位置坐标) 删除并返回一个数据(默认是从最后一个开始)
print('# pop')
str1 = list1.pop()
print(list1)
print(str1)
str2 = list1.pop(0)
print(list1)

# remove(数据) 如果里面有两个相同的，会移除最后一个
print('# remove')
print(list1.remove('she'))  # None
print(list1)

# clear 清空列表
print('# clear')
print(list1.clear())  # None
print(list1)  # []
print('******************end******************')
