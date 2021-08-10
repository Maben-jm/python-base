# python-base

## 数据类型转换注意事项

### eval注意事项

> `eval()`方法使用，不能规划字符串本身，否则会报错

```python
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
```

结果：

````
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
````

## 运算符注意事项

### 数学运算符

> 优先级：`()`高于`**`高于`*`、`/`、`//`、`%`高于`+`、`-`

```python
# 除法 (只要是除法，结果一定是float)
print(10/3)
print(10/2)
# 整除
print(10//3)
# 冥函数
print(2**3)
# 优先级判断
print(2 * 3 ** 2)
```

输出结果：

```
3.3333333333333335
5.0
3
8
18
```

### 赋值运算符

> 多变量赋值需要注意一哈

```python
n1, f1, s1 = 1, 1.1, 's1'
print(f'n1={n1},f1={f1},s1={s1}')
"""
结果：
n1=1,f1=1.1,s1=s1
"""
```

### 复合赋值运算符

> 这点和Java中的一样

```python
n2 = 10
n2 *= 1+2
print(n2)
```

**结果：**

```
30
```

### 逻辑运算符

> 与Java对比

    and  相当于Java中的&&
    or   相当于Java中的||
    not  相当于Java中的!
> 注意数字之间的逻辑运算符（Java中不允许数字之间进行逻辑运算）

```python
a = 0
b = 1
c = 2
d = 0
# and 运算符，只要有一个数字为0，则结果返回0；否则返回最后一个非0数字
print(a and b)
print(b and c)
print(c and b)
# or 运算符，只有所有数字都为0才返回0；否则返回第一个非0数字
print(a or b)
print(b or c)
print(c or b)
print(a or d)
```

**结果**

```
0
2
1
1
1
2
0
```

## 打印语句

### 取消换行

```python
# 换行(默认)
print('xxxx',end='\n')
# 取消换行
print('xxxx',end='')
```

## 循环语句

### 循环配合else使用

````python
print("***************else使用**************")
k = 0
while k < 3:
    print(k)
    k += 1
else:
    print("这里是while配合else使用1")

print("***************break使用（break会彻底打断循环，跳出循环后不会走else了！！！）**************")
k = 0
while k < 3:
    if k == 2:
        break
    print(k)
    k += 1
else:
    print("这里是while配合else使用1")
````

**结果**

```
***************else使用**************
0
1
2
这里是while配合else使用1
***************break使用（break会彻底打断循环，跳出循环后不会走else了！！！）**************
0
1
```



## 字符串学习

### 回车对字符串的作用

````python
print("*****************学习字符串********************")
x1 = 'hello ' \
    'world'
print(x1)

# 这里的换行符会被完美的打印出来
x2 = '''hello
    world
'''
print(x2)
print("***********************************************")
````

**输出结果**

```
*****************学习字符串********************
hello world
hello
    world

**********************************************
```

### 切片用法

```python
# 字符串切片 语法： 序列名[开始位置下标:结束位置下标:步长]
x3 = '1234567890'
print(x3[0: 6])
print(x3[0: 6:2])
# 如果开始位置不写，默认从0开始
print(x3[: 6])
# 如果结束不写，默认结束位置到最后
print(x3[2:])
# 步长是-1，目的：倒序
print(x3[::-1])
# 起始位置和结束位置为负数，从后开始，结束位置最大是-1，
# 因为结束位置不获取，所以这种方式不能获取最后一个位置的值
print(x3[-4:-1])
print(x3[-4:0])  # 不能选取数据 因为最大位置是-1
print(x3[-4:-1:-1])  # 不能选取数据 -4到-1选取方向是从左向右   步长-1选取方向是从右向左  方向冲突
print(x3[-1:-4:-1])  # 这样就能获取数据了
print("***********************************************")
```

**输出结果**

```
123456
135
123456
34567890
0987654321
789


098
***********************************************
```

### 常用方法注意事项

#### find和index的区别

> find函数在找不到的情况下返回-1
>
> index函数在找不到的情况会报错

#### join

> join的语法是： 字符串.join(多字符串组成的序列)

## 列表学习

### append和extend的区别

```python
list2 = ['1', '2']
list2.append(['3','4']) # 这样获取的结果是['1','2',['3','4']]
list2.extend(['3','4']) # 这样获取的结果是['1','2','3','4']
```

### remove

```python
list1 = ['1','2','3','3','4']
list1.remove('3')
print(list1)
返回结果：（如果列表中有多个和移除相同的数据，则只是移除最后一个）
['1', '2', '3', '4']
```

