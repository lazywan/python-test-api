#-*-conding:utf-8-*-
#@Time :2020/1/1812:44
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:test_case.py
from unittest import *
from ddt import ddt,data,unpack
from API5.common import project_path
from API5.common.do_excel import DoExcel
from API5.common.read_config import ReadConfig
from API5.common.http_request import HttpRequest
from API5.common.read_logging import ReadLog
from API5.common.get_data import GetData
from API5.common.do_mysql import DoMysql
import warnings

# COOKIES = None  # 这个变量必须放在这里，不能放在类里面作为全局变量
@ddt
class AddTestRecharge(TestCase):
    rc = ReadConfig(project_path.config_path)
    #sheet_name = rc.get_str('RechargeCase', 'sheet_name3')  # 读取配置文件，sheet_name3=recharge
    ex = DoExcel(project_path.case_path, 'recharge')  # 这个也可以放到setup测试准备里
    test_data = ex.read_data('RechargeCase')  # 读取的所有测试用例，嵌套字典的列表
    my_log = ReadLog()

    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
    def tearDown(self):
        pass

    @data(*test_data)  #test_data脱外套后用case变量接收
    #@unpack
    def test_recharge(self,case):
        #global TestResult #声明TestResult为全局变量，下面有两个地方都用了这个变量。如果不在声明，会最后打印标黄
        #global expect_amount #声明全局变量。否则标黄，或者报错。老师的没有声明却不报错，不知道为什么?
        #global COOKIES  #声明COOKIES为全局变量
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])

        self.my_log.info('-------开始执行第{}条{}模块的用例'.format(case['CaseId'],case['Module']))
        self.my_log.info('测试数据是{}'.format(case))
        # 投资前查询数据库获取余额保存
        if case['Sql'] != None:  # 如果sql语句不为null，代表要进行查询数据库的 操作
            before_amount = DoMysql().do_mysql(eval(case['Sql'])['sql'], 1)[0]
        resp = HttpRequest().request(method, url, param,cookie=getattr(GetData,'COOKIE'))
        if resp.cookies: #判断cookies是否为空，如果不为空，把resp.cookies赋值给COOKIES
            setattr(GetData,'COOKIE',resp.cookies)#利用反射设置类里面的属性值
        try:
            if case['Sql'] != None:  # 如果sql语句不为null，代表要进行查询数据库的 操作
                after_amount = DoMysql().do_mysql(eval(case['Sql'])['sql'], 1)[0]
                recharge_amount = int(param['amount'])# 转换为int类型
                expect_amount = before_amount+recharge_amount
                self.assertEqual(expect_amount, after_amount)
                #替换期望结果里的amount为期望值
                #expect_result=eval(case['ExpectedResult'])
            if case['ExpectedResult'].find('expectamount')>-1: #也可以写成>-1
                case['ExpectedResult']=case['ExpectedResult'].replace('expectamount',str(expect_amount)) #把整数转换为str,替换玩之后必须要用原来值接收

            self.assertEqual(resp.json(),eval(case['ExpectedResult']))  #要字典比对比较方便
            TestResult = 'Pass'
        except Exception as e:
            TestResult = 'Failed'
            self.my_log.error('测试failed,报错内容是{}'.format(e))
            raise e
        finally: #不管比较结果是否相同，都需要写入数据，即不管try里代码对不对都要执行finally
            #写回结果，接口实际结果和比较结果
            self.ex.write_back(case['CaseId'] + 1, 9, resp.text)  # 接口返回的结果写入表格第八列
            self.ex.write_back(case['CaseId'] + 1, 10, TestResult)  # 期望值和预期值的对比结果写入表格第9列

        self.my_log.info('接口实际返回结果：{}'.format(resp.text))



