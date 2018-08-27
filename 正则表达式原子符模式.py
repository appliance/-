import re

# 以原子为核心
# 原子是正则表达式中最基本的组成单位,一个原子代表了字符串中的一个位置

# 1、普通字符作为原子
# 此处使用yue作为原子使用，这里有三个原子，分别是 y u e
pattern1 = "yue"
string1 = "http://yum.iqianyue.com"
result1 = re.search(pattern1, string1)
# top, tail = result1.span()
# print(top)
# print(tail)
# print(string1[top:tail])


# 2、非打印字符作为原子
# 非打印字符指用于格式控制的符号，比如换行符等
# \n换行符 \t制表符
pattern2 = "\n"
string2 = "http://yum.iqianyue.com http://baidu.com"
result2 = re.search(pattern2, string2)
# print(result2)


# 重点：
# 3、通用字符作为原子，即一个字符可以匹配一类字符
'''
    \w  匹配任意一个字母，数字或下划线     \W  匹配除了任意一个字母，数字或下划线以外的任意一个其他字符
    \d  匹配任意一个十进制数      \D  匹配除了任意一个十进制数以外的任意一个其他字符
    \s  匹配任意一个空白字符      \S  匹配除了空白字符以外的任意一个其他字符 
'''
pattern3 = "\w\dpython\w"
string3 = "abdfgphp345pythony_pythonlalala"
result3 = re.search(pattern3,string3)
top, tail = result3.span()
# print(string3[top:tail])


# 重点：
# 4、原子表，可以定义一组地位平等的原子，然后匹配的时候会取该原子表中的任意一个原子进行匹配
# [xyz] 此原子表表示，匹配xyz其中一个原子
# [^xyz] 除了xyz以外的原子均可匹配
pattern4_1 = "\w\dpython[xyz]\w"
pattern4_2 = "\w\dpython[^xyz]\w"
string4 = "abdcfphp345pythony_py"
result4_1 = re.search(pattern4_1,string4)
result4_2 = re.search(pattern4_2,string4)
# print(result4_1)
# print(result4_2)


# 重点中的重点
# 5、元字符，具有一些特殊含义的字符，比如重复n次前面的字符等
'''
    .       匹配除了换行符以外的任意字符
    
    ^       匹配字符串的开始位置
    $       匹配字符串的结束位置
    
    *       匹配0次、1次或多次前面的原子
    ?       匹配0次或1次前面的原子
    +       匹配1一次或多次前面的原子
    
    {n}     前面的原子恰好出现n次
    {n,}    前面的原子至少出现n次
    {n,m}   前面的原子至少出现n次，至多出现m次
    
    |       模式选择符
    ()      模式单元符
'''
# 5.1、 任意匹配元字符
pattern5_1 = ".python..."
string5_1 = "abdcfphp345pythony_py"
result5_1 = re.search(pattern5_1, string5_1)
# print(result5_1)

# 5.2、边界限制元字符，字符以什么为开始，又以什么为结束
pattern5_2 = "^abd"
pattern5_2_1 = "py$"
string5_2 = "abcdcfphp345pythony_py"
result5_2 = re.search(pattern5_2, string5_2)
result5_2_1 = re.search(pattern5_2_1, string5_2)
# print(result5_2)
# print(result5_2_1)

# 5.3、限定符
pattern5_3 = "py.*n"
pattern5_3_1 = "cd{2}"
pattern5_3_2 = "cd{3}"
pattern5_3_3 = "cd{2,}"
string5_3 = "abcdcfphp345pythony_py"
result5_3 = re.search(pattern5_3, string5_3)
result5_3_1 = re.search(pattern5_3_1, string5_3)
result5_3_2 = re.search(pattern5_3_2, string5_3)
result5_3_3 = re.search(pattern5_3_2, string5_3)
# print(result5_3)
# print(result5_3_1)
# print(result5_3_2)
# print(result5_3_3)

# 5.4、模式选择符，可以设置多个模式
pattern5_4 = "python|php"
string5_4 = "abcdcfphp345pythony_py"
result5_4 = re.search(pattern5_4,string5_4)
# print(result5_4)

# 5.5、模式单元符，利用()将一些原子组合成一个大原子使用
pattern5_5 = "(cd){1,}"
pattern5_5_1 = "cd{1,}"
string5_5 = "abcdcdcdcdgphp345pythony_py"
result5_5 = re.search(pattern5_5, string5_5)
result5_5_1 = re.search(pattern5_5_1,string5_5)
# print(result5_5)
# print(result5_5_1)


# 6、模式修正，通过模式修正符号改变表达式的含义，从而实现一些匹配结果的调整功能
'''
    I           匹配时忽略大小写
    M           多行匹配
    L           做本地化识别匹配
    U           根据Unicode字符及解析字符
    S           是的.元符可以匹配任意的字符
'''

pattern6 = "python"
string6 = "abcdcfphp345Pythony_py"
result6 = re.search(pattern6,string6)
result6_1 = re.search(pattern6,string6,re.I)
# print(result6)
# print(result6_1)


# 7、贪婪模式，懒惰模式
pattern7 = "p.*y"   # 贪婪模式
pattern7_1 = "p.*?y"    # 懒惰模式      .*后加上？即可转化为懒惰模式
string7 = "abcdcfphp345Pythony_py"
result7 = re.search(pattern7, string7)
result7_1 = re.search(pattern7_1, string7)
print(result7)
print(result7_1)