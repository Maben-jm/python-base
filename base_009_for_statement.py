"""
for循环学习
    九九乘法表
"""

print("********************九九乘法表********************")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print('')

print("*******************1-100的偶数和*********************")
sum = 0
for k in range(0, 101, 2):
    sum += k
print(f'1-100的偶数和是:{sum}')
