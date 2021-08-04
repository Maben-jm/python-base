"""
变量命名规则：
    1.由数字、字母、下划线组成
    2.不能使用数字开头
    3.不能使用内置关键字
    4.严格区分大小写
"""
tom = "this is tom"
print(tom)

jerry = 'this is jerry'
print(jerry)

print('*****************数据类型**************')

'''
数据类型
    1.数值类型
        int -- 整数类型
        float -- 浮点型
    2.布尔型
        true
        false
    3.str字符串
    4.list列表
    5.tuple元组
    6.set集合
    7.dict字典
'''
num1 = 1
num2 = 1.1
print('type num1 ', type(num1))
# result: type num1  <class 'int'>
print('type num2', type(num2))
# result: type num2 <class 'float'>

str1 = '123'
print('type str1 ', type(str1))
# result: type str1  <class 'str'>

b1 = True
print('type b1 ', type(b1))
# result: type b1  <class 'bool'>

list1 = [10, 20, 30]
print('type list1', type(list1))
# result: type list1 <class 'list'>

tuple1 = (1, 2, 3)
print('type tuple1 ', type(tuple1))
# result: type tuple1  <class 'tuple'>

set1 = {1, 2, 3}
print('type set1 ', type(set1))
# result: type set1  <class 'set'>

dict1 = {
    'name': 'tom',
    'age': '18'
}
print('type dict1 ', type(dict1))
# result: type dict1  <class 'dict'>

