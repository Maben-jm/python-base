"""
学习类型转换，使用input语法配合
"""
content = input("请输入数字：")
print(f'输入的数字是：{content},type是：{type(content)},转化之后结果：{type(int(content))}')

