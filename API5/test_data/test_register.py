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

COOKIES=None
@ddt
class AddTestRegister(TestCase):
    rc = ReadConfig(project_path.config_path)
    #sheet_name = rc.get_str('RechargeCase', 'sheet_name1')   #读取配置文件，sheet_name1=register
    ex = DoExcel(project_path.case_path, 'register')  # 这个也可以放到setup测试准备里
    test_data=ex.read_data('RegisterCase')#读取的所有测试用例，嵌套字典的列表
    my_log=ReadLog()

    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*test_data)  #test_data脱外套后用case变量接收
    #@unpack
    def test_register(self,case):
        global TestResult #声明TestResult为全局变量，下面有两个地方都用了这个变量。如果不在声明，会最后打印标黄
        global COOKIES
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])

        self.my_log.info('-------开始执行第{}条{}模块的用例'.format(case['CaseId'],case['Module']))
        self.my_log.info('测试数据是{}'.format(case))
        resp = HttpRequest().request(method, url, param,cookie=COOKIES)

        try:
            self.assertEqual(resp.json(),eval(case['ExpectedResult']))  #要字典比对比较方便，
            TestResult = 'Pass'
        except Exception as e:
            TestResult = 'Failed'
            self.my_log.error('测试failed,报错内容是{}'.format(e))
            raise e
        finally: #不管比较结果是否相同，都需要写入数据，即不管try里代码对不对都要执行finally
            #写回结果，接口实际结果和比较结果
            self.ex.write_back(case['CaseId'] + 1, 8, resp.text)  # 接口返回的结果写入表格第八列
            self.ex.write_back(case['CaseId'] + 1, 9, TestResult)  # 期望值和预期值的对比结果写入表格第9列

        self.my_log.info('接口实际返回结果：{}'.format(resp.text))



