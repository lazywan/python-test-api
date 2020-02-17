#-*-conding:utf-8-*-
#@Time :2020/2/1521:35
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:learn-re.py

##1什么是正则表达式
##2正则表达式的组成方式，元字符(/d)和原义字符（123）  假设要匹配mp123,
##3如何用python解析,
     # .点 匹配除“\n”和"\r"之外的任何单个字符。要匹配包括“\n”和"\r"在内的任何字符，请使用像“[\s\S]”的模式。
##4 使用正则表达式场景，
    #----参数化
    #----查找一些特殊字符，邮箱，手机号码，身份证号码
import re
from API6.common.get_data import GetData
target="{'mobilephone':'#normal_user#','password':'#normal_pwd#'}"
p='normal_user' #原意字符的查找
p2='#(.*?)#'  #圆括号在正则表达式里代表组的概念，点表示匹配任意字符，星号表示匹配多次，后面再加个问号表示最多找一次

# p='a'
# target='abcde'
# m=re.match(p,target)
# print(m)

s=re.search(p2,target)  ## 在目标字符串里面根据正则表达式来查找，有匹配的字符串就返回对象
print(s)
print(s.group())# 不传参的时候返回表达式和匹配的字符串一起,#normal_user#
print(s.group(1))# # 传参就是只返回匹配的字符串，也就是当前组的匹配字符,normal_user

# f=re.findall(p2,target)# 找到所有匹配的字符，返回的是一个列表 ['normal_user', 'normal_pwd']
# print(f)
#
# target2 = re.sub(p2,'18688775656',target) #re.sub.查找并替换 把p2在target查找并把找到的替换为rep1
# print(target2)  #{'mobilephone':'18688775656','password':'18688775656'}
#
# target2 = re.sub(p2,'18688775656',target,count=1) #re.sub.查找并替换 count表示匹配替换次数，把p2在target查找并把找到的替换为rep1
# print(target2) #替换一个 {'mobilephone':'18688775656','password':'#normal_pwd#'}
while re.search(p2,target):
    m=re.search(p2,target)
    key=m.group(1) #normal_user
    value=getattr(GetData,key) #获取normal_user值即18114800000
    target=re.sub(p2,value,target,count=1) #替换target种normal_user值为18114800000

print(target) #最终结果 {'mobilephone':'18114800000','password':'123456'}
print(type(target))