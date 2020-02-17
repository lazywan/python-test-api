#-*-conding:utf-8-*-
#@Time :2020/2/614:28
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:test_addloan.py

from unittest import *
from ddt import ddt,data,unpack
from API6.common import project_path
from API6.common.do_excel import DoExcel
from API6.common.read_config import ReadConfig
from API6.common.http_request import HttpRequest
from API6.common.read_logging import ReadLog
from API6.common.get_data import GetData
from API6.common.get_data import replace_re
from API6.common.do_mysql import DoMysql
import warnings

# COOKIES = None  # 这个变量必须放在这里，不能放在类里面作为全局变量
@ddt
class AddTestAddLoan(TestCase):
    rc = ReadConfig(project_path.config_path)
    #sheet_name = rc.get_str('RechargeCase', 'sheet_name3')  # 读取配置文件，sheet_name3=recharge
    ex = DoExcel(project_path.case_path, 'add_loan')  # 这个也可以放到setup测试准备里
    test_data = ex.read_data('RechargeCase')  # 读取的所有测试用例，嵌套字典的列表
    my_log = ReadLog()

    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)

    def tearDown(self):
        pass

    @data(*test_data)  #test_data脱外套后用case变量接收
    #@unpack
    def test_addloan(self,case):
        global TestResult #声明TestResult为全局变量，下面有两个地方都用了这个变量。如果不在声明，会最后打印标黄
        # global COOKIES  #声明COOKIES为全局变量
        method=case['Method']
        url=case['Url']
        # #在请求之前替换loanid
        # if case['Params'].find('loanid')!=1:#如果param这一栏能找到loanid这个字符串
        #     param=eval(case['Params'].replace('loanid',str(getattr(GetData,'LOAN_ID'))))  #记得eval,#因为拿到的数据是int类型 replace只能用在字符串之间的替换 所以用str强转一下
        # else:
        #     param=eval(case['Params'])
        param=eval(replace_re(case['Params']))

        #打印日志，发起请求
        self.my_log.info('-------开始执行第{}条{}模块的用例'.format(case['CaseId'],case['Module']))
        self.my_log.info('测试数据是{}'.format(case))
        resp = HttpRequest().request(method, url, param,cookie=getattr(GetData,'COOKIE'))

        #判断是否要查询数据库
        if case['Sql']!=None: #如果sql语句不为null，代表要进行查询数据库的 操作
            sql = eval(replace_re(case['Sql'])) #替换sql语句中的memberid
            loan_id=DoMysql().do_mysql(sql['sql'],1)  #查询数据库返回的是元组类型，切记！！！所以我们存储数据的时候，#最好是根据索引拿到值之后,再去进一步操作#
            self.my_log.info('获取的loanid是{}'.format(loan_id))
            setattr(GetData,'loanid',str(loan_id[0]))#利用反射,loan_id[0]是int类型，为了替换正则函数replace_re用，需要转为str

        # 判断cookies是否为空，如果不为空，把resp.cookies赋值给COOKIES
        if resp.cookies:
            setattr(GetData,'COOKIE',resp.cookies)#利用反射设置类里面的属性值

        try:
            self.assertEqual(resp.json(),eval(case['ExpectedResult']))  #要字典比对比较方便，
            TestResult = 'Pass'
        except Exception as e:
            TestResult = 'Failed'
            self.my_log.error('测试failed,报错内容是{}'.format(e))
            raise e
        finally: #不管比较结果是否相同，都需要写入数据，即不管try里代码对不对都要执行finally
            #写回结果，接口实际结果和比较结果
            self.ex.write_back(case['CaseId'] + 1, 9, resp.text)  # 接口返回的结果写入表格第9列
            self.ex.write_back(case['CaseId'] + 1, 10, TestResult)  # 期望值和预期值的对比结果写入表格第10列

        self.my_log.info('接口实际返回结果：{}'.format(resp.text))

