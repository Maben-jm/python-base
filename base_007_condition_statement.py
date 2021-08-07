"""
条件语句学习
"""
age = int(input("请输入您的年龄："))
while age < 0 or age > 100:
    age = int(input('输入的年龄不符，请重新输入：'))

if 18 <= age <= 60:
    print(f'年龄是{age},可以上网')
    if age >= 24:
        print('已经到了工作年龄，不要沉迷网络，赶紧工作去吧')
    else:
        print('还是可以浪的年龄，继续浪吧')
elif age > 60:
    print(f'您都这么大了，会上网不？回家看电视去吧')
else:
    print(f'用户还是未成年，不允许上网')

print('系统结束')
