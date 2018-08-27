'''
    实例1：匹配.com或.cn后缀的URL网址
    实例2：匹配电话号码
'''
import re

# 匹配.com或.cn后缀的URL网址
string1 = "<a href='http://www.baidu.com'>百度首页</a>"
# pattern1 = "http://w{3}.*.com"
pattern1 = "[a-zA-Z]+://[^\s]*[.com|.cn]"
res = re.search(pattern1, string1)
# print(res)



# 匹配电话号码
string2 = "0513-18770915493手机号码"
pattern2 = "\d{4}-\d{11}"
res2 = re.search(pattern2,string2)
print(res2)