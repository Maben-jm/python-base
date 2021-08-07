"""
while 条件学习
    1.打印九九乘法表
    2.配合else使用
    3.配合break使用（注意：break会打断循环，也就不会走else了）
"""
print("***************九九乘法表**************")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{i}*{j}={i * j} ', end='')
        j += 1
    print('')
    i += 1

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
