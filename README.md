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

