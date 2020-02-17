#-*-conding:utf-8-*-
#@Time :2020/2/516:54
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:do_mysql.py
from mysql import connector
from API5.common.read_config import ReadConfig
from API5.common import project_path

class DoMysql:
    def do_mysql(self,query,flag=1):
        '''query:表示sql查询语句
           flag:1表示查询结果有以条，2表示查询结果有 多条'''
        db_config =ReadConfig(project_path.config_path).get_other('DB','db_config')#从配置文件获取数据库链接的ip等
        cnn = connector.connect(**db_config)
        cursor = cnn.cursor()
        cursor.execute(query)  # 查询不需要commit

        if flag==1:
            res = cursor.fetchone()  # 返回的元组
            #print('查询数据库结果为：{}'.format(res))
        else:
            res = cursor.fetchall()  # 返回的列表嵌套元组,[(140066,), (140067,), (140068,), (140071,), (140086,), (140087,)]
            #print('查询数据库结果为：{}'.format(res))
        return res
        # #增删改数据库，update
        # update="update member set RegName='caowanwan' where id='1139812'"
        # cursor.execute(update)
        # cursor.execute('commit')#提交

if __name__=='__main__':
    query="select LeaveAmount from member where mobilephone = 18114800000"    #"select min(id) from member where id>'1139813'# "
    sq=DoMysql().do_mysql(query,2)
    print('查询数据库结果为：{}'.format(sq))
   # {'sql': 'select LeaveAmount from member where mobilephone = "18114800000"'}

