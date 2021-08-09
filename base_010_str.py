"""
字符串详细学习
"""
print("*****************学习字符串********************")
x1 = 'hello ' \
     'world'
print(x1)

# 这里的换行符会被完美的打印出来
x2 = '''hello
    world
'''
print(x2)

print("*********************切片学习**************************")
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

print("*********************常用方法学习**************************")
x4 = 'hello world and maben and jiamei'

# find(查找字符串，起始位置，结束位置) 默认从左查找 （rfind 从右查找）
print('# find')
print(x4.find('and'))  # 12
print(x4.find('and', 13))  # 22
print(x4.find('and', 14, 999))  # 22
print(x4.find('xxx'))  # -1

# index(查找字符串，起始位置，结束位置) 默认从左查找 （rindex 从右查找）
print('# index')
print(x4.index('and'))  # 12
print(x4.index('and', 13))  # 22
print(x4.index('and', 14, 999))  # 22
# print(x4.index('xxx'))  # 找不到就会报错

# count 查找子串出现的次数
print('# count')
print(x4.count('and'))

# replace(旧字符串，新字符串，替换次数)
print('# replace')
print(x4.replace('and', 'axd'))  # hello world axd maben axd jiamei
print(x4.replace('and', 'axd', 1))  # hello world axd maben and jiamei

# split(分割字符，num)
print('# split')
print(x4.split("and"))  # ['hello world ', ' maben ', ' jiamei']
print(x4.split("and", 1))  # ['hello world ', ' maben and jiamei']

# 字符串.join(多字符串组成的序列)
print('# join')
list5 = x4.split("and")
print('axd'.join(list5))

# capitalize:将字符串第一个字符转换成大写
print('# capitalize')
print(x4.capitalize())  # Hello world and maben and jiamei

# title() 将字符串每个单词首字母转换成大写
print('# title')
print(x4.title())  # Hello World And Maben And Jiamei

# lower() 将字符串中所有大写转成小写
print('# lower')
print(x4.lower())  # hello world and maben and jiamei

# upper() 将字符串中所有小写转成大写
print('# upper')
print(x4.upper())  # HELLO WORLD AND MABEN AND JIAMEI

# strip() 删除字符串两侧空白字符 lstrip() 删除左侧  rstrip() 删除右侧
print('# lstrip')
print('  hello  hello '.strip())
print('  hello  hello '.lstrip())
print('  hello  hello '.rstrip())

# startswith(子串，开始位置，结束位置)
print('# startswith')
print('hello'.startswith('h'))  # True

# endswith(子串，开始位置，结束位置)
print('# endswith')
print('hello world'.endswith('world'))  # Ture
print('hello world'.endswith('world', 8))  # False

# isalpha() 字符串至少有一个字符，并且所有字符都是字母，则为True
print('# isalpha')
print('hello world'.isalpha())  # False
print('hwllo'.isalpha())  # True

# isdigit() 字符串至少有一个字符，字符串只包含数字返回True
print('# isdigit')
print(''.isdigit())  # False
print('1234'.isdigit())  # True

# isspace() 字符串至少有一个字符，字符串只包含空白返回True
print('# isspace()')
print(''.isspace())  # False
print('   '.isspace())  # True
print("***********************************************")
