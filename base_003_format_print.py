name = 'tom'
age = 18
weight = 75.5
stu_id = 1
money = 10000

print("学生姓名是%s" % name)
print("学生年龄是%d" % age)
print('学生体重是%f' % weight)
print('学生体重是%.2f' % weight)
print('学生学号是%03d' % stu_id)
print('学生所缴学费%03d' % money)
print('姓名：%s,年龄：%d,今天报道成功' % (name, age))
# Python3.6新增语法
print(f'姓名：{name},年龄：{age},今天报道成功')

'''
result:
    学生姓名是tom
    学生年龄是18
    学生体重是75.500000
    学生体重是75.50
    学生学号是001
    学生所缴学费10000
    姓名：tom,年龄：18,今天报道成功
'''

