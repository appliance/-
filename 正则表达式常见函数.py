import re
'''
    正则表达式常见函数
    re.match
    re.search
    re.sub
    全局匹配函数
'''

# 1、 re.match() 从源字符串的起始位置匹配一个模式(匹配的结果必须是包含源字符串头的)
string = "apythonhellomypythonispythonourpythonend"
pattern = ".python."
result = re.match(pattern, string)
# result2 = re.match(pattern, string).span()          # 返回匹配成功的结果在源字符串中的位置
# print(result)
# print(result2)

# 2、re.search() 扫描整个字符串并进行对应的匹配
string2 = "hellomypythonhispythonourpythonend"
pattern2 = ".python."
result2 = re.match(pattern2, string2)
result2_1 = re.search(pattern2, string2)
# print(result2)
# print(result2_1)

# 3、全局匹配函数，将符合模式的内容全部都匹配出来，不仅仅只会匹配一个结果
string3 = "hellomypythonhispythonourpythonend"
pattern3 = re.compile(".python.")    #预编译
result3 = pattern3.findall(string3)   #找出符合模式的所有结果
# print(result3)

# 4、re.sub()利用正则表达式来实现替换某些字符串的功能
string4 = "hellomypythonhispythonourpythonend"
pattern4 = "python."
result4 = re.sub(pattern4, "php", string4)   # 将python. 用php全部替换
result5 = re.sub(pattern4, "php", string4, 2)   # 最多替换2次
print(result4)
print(result5)