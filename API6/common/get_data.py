#-*-conding:utf-8-*-
#@Time :2020/1/3013:34
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:get_data.py
from API6.common.read_config import ReadConfig
from API6.common import project_path
import re

class GetData:
    '''可以用来动态的更改，删除 获取属性'''

    COOKIE=None
    #loanid=None 用到replace_re函数后，这个参数就不用了
    normal_user = ReadConfig(project_path.config_path).get_str('data','normal_user')
    normal_pwd = ReadConfig(project_path.config_path).get_str('data','normal_pwd')
    normal_memberid = ReadConfig(project_path.config_path).get_str('data','normal_memberid')

#利用正则重新定义一个函数，替换目标内容
def replace_re(target):
    p2 = '#(.*?)#'
    while re.search(p2, target):
        m = re.search(p2, target)
        key = m.group(1)  # normal_user
        value = getattr(GetData, key)  # 获取normal_user值即18114800000
        target = re.sub(p2, value, target, count=1)  # 替换target种normal_user值为18114800000

    print(target)
    return target

replace_re("{'mobilephone':'#normal_user#','password':'#normal_pwd#'}")

# print(getattr(GetData,'COOKIE')) #第一个参数是类名，第二个是属性的参数名，返回值是属性值
#
# print(hasattr(GetData,'COOKIE')) #第一个参数是类名，第二个是属性的参数名，返回值是布尔值
#
# print(setattr(GetData,'ABC','cde')) #第一个参数是类名，第二个是属性的参数名，第三个是要设置的新值，返回值是None
# print(getattr(GetData,'ABC'))  # 返回值是cde
# print(setattr(GetData,'COOKIE','efg')) #第一个参数是类名，第二个是属性的参数名，第三个是要设置的新值，返回值是None
# print(getattr(GetData,'COOKIE'))  # 返回值是cde
#
# ####删除类的某个属性###
# print(delattr(GetData,'COOKIE')) #删除类的某个属性
# print(getattr(GetData,'COOKIE'))

