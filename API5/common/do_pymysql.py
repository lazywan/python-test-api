#-*-conding:utf-8-*-
#@Time :2020/2/516:54
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:do_mysql.py
import pymysql
from API5.common.read_config import ReadConfig
from API5.common import project_path

class DoMysql:
    def do_mysql(self,query,flag=1):
        '''query:表示sql查询语句
           flag:1表示查询结果有以条，2表示查询结果有 多条'''
        db_config1 =ReadConfig(project_path.config_path).get_other('DB','db_config1')#从配置文件获取数据库链接的ip等
        # cnn = pymysql.connect(host="test.lemonban.com",
        #                user="test",
        #                password="test",
        #                db="future",
        #                port=3306,
        #                charset="utf8",
        #                cursorclass=pymysql.cursors.DictCursor)
        cnn=pymysql.connect(**db_config1)
        cursor = cnn.cursor()
        cursor.execute(query)  # 查询不需要commit
        # 插入更新删除需要手动提交
        cnn.commit()

        if flag==1:
            res = cursor.fetchone()  # 返回的元组
            #print('查询数据库结果为：{}'.format(res))
        else:
            res = cursor.fetchall()  # 返回的元组嵌套元组！！((140066,), (140067,), (140068,), (140071,), (140086,), (140087,))
            #print('查询数据库结果为：{}'.format(res))
        # 4.关闭连接
        cursor.close()  # 先关游标对象
        cnn.close()  # 然后再关连接对象

        return res
        # #增删改数据库，update
        # update="update member set RegName='caowanwan' where id='1139812'"
        # cursor.execute(update)
        # cursor.execute('commit')#提交

if __name__=='__main__':
    query="select id from loan where MemberID='293366';"    #"select min(id) from member where id>'1139813'# "
    sq=DoMysql().do_mysql(query,2)
    print('查询数据库结果为：{}'.format(sq))
    print('查询数据库结果为：{}'.format(sq[0]))
