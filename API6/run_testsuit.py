#-*-conding:utf-8-*-
#@Time :2020/1/1721:53
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:run.py

from unittest import *
from API6.common import project_path
from API6.test_data.test_recharge_fanshe import AddTestRecharge
from API6.test_data.test_register import AddTestRegister
from API6.test_data.test_addloan import AddTestAddLoan
from API6.test_data.test_invest import AddTestInvest


import HTMLTestRunnerNew

suit=TestSuite()
loader=TestLoader()
#方法二，TestLoader加载多有测试用例,通过测试类来添加 ,ddt装饰的用例只能用loder的方式
suit.addTest(loader.loadTestsFromTestCase(AddTestRecharge))
suit.addTest(loader.loadTestsFromTestCase(AddTestRegister))
suit.addTest(loader.loadTestsFromTestCase(AddTestAddLoan))
suit.addTest(loader.loadTestsFromTestCase(AddTestInvest))

#方法三，通过测试模块来添加
# suit.addTest(loader.loadTestsFromModule(test_recharge))
# suit.addTest(loader.loadTestsFromModule(test_register))

with open(project_path.report_path,'wb') as file: #使用html结尾的文件，打开方式是wb,如果是wb格式，不需要指定encoding编码
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                            title='2020-02-16注册接口几条用例',
                                            description='注册接口用例报告',
                                            tester='caowanwan')
    runner.run(suit)#run方法执行测试套件里面的用例

# #方法一，一个一个添加测试用例到套件，addTest参数是测试类实例
# suit=TestSuite()
#suit.addTest(AddTest('test_001'))
# suit.addTest(AddTest('test_002'))
# suit.addTest(DevTest('test_003'))
# suit.addTest(DevTest('test_004'))


#执行测试用例+版本的生成用例报告的，可以用新版本的 TextTestRunner
# #stream=file 输出到文件，verbosity=2是最详细模式，
# with open('suitlog.txt','a',encoding='utf-8') as file:
#     run=TextTestRunner(stream=file, descriptions=True, verbosity=2)#老
#     run.run(suit)  #run方法执行测试套件里面的用例