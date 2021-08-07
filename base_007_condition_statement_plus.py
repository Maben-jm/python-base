"""
条件语句学习扩展-猜拳游戏
    注意：导入random模块
"""
import random

content = int(input('请输入(石头-1；剪刀-2；布-3)： '))
while content > 3 or content < 1:
    content = input('输入不符合要求，请重新输入')
while True:
    computer = random.randint(1, 3)
    if (content == 1 and computer == 2) or (content == 2 and computer == 3) or (content == 3 and computer == 1):
        print('玩家获胜，恭喜恭喜')
    elif computer == content:
        print("平局，再来一次")
    else:
        print("电脑获胜，再接再厉吧")
    isContinue = int(input('是否再来一次(再来一次-1；退出-2)？ '))
    while isContinue != 1 and isContinue != 2:
        print('输入不合法，请重新输入~')
        isContinue = int(input("是否再来一次(再来一次-1；退出-2)？ "))
    if isContinue == 2:
        break
    content = int(input('请输入(石头-1；剪刀-2；布-3)： '))

print('系统结束')
