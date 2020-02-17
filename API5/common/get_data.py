#-*-conding:utf-8-*-
#@Time :2020/1/3013:34
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:get_data.py

class GetData:
    '''可以用来动态的更改，删除 获取属性'''

    COOKIE=None
    LOAN_ID=None

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

