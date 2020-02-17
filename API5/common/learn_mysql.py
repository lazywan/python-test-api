#-*-conding:utf-8-*-
#@Time :2020/1/3016:55
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:learn_mysql.py

# pymysql mqsql-connetor-python 两个安装任何一个都可以
# pip install pymysql
# pip install mysql-connector-python
# 47.107.168.87 端口3306 用户名 python 密码python666
from mysql import connector
#第一步 链接数据库
db_config={'host':'47.107.168.87',
        'port':'3306',
        'username':'python',
        'password':'python666',
        'database':'future'}
cnn=connector.connect(**db_config) #关键字参数加两个星号表示db_config还是个字典，表示建立一个连接
#第二步 获取游标即鼠标或者光标，获取操作数据库权限
cursor=cnn.cursor()
#第三步:操作数据库表
query="select id from member where id>'1139810'# "
cursor.execute(query) # 查询不需要commit

#第四步:打印结果
res=cursor.fetchone()  #返回的元组
res1=cursor.fetchall()   #返回的列表嵌套元组
print('查询数据库结果为：{}'.format(res))
print('查询数据库结果为：{}'.format(res1))

# #增删改数据库，update
# update="update member set RegName='caowanwan' where id='1139812'"
# cursor.execute(update)
# cursor.execute('commit')#提交



# def test(**kwargs):
#     print(kwargs)
# db_config={'host':'47.107.168.87',
#         'port':'3306',
#         'username':'python',
#         'password':'python666',
#         'database':'future'}
#
# test(**db_config)



