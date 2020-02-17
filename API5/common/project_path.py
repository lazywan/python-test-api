#-*-conding:utf-8-*-
#@Time :2020/1/1722:38
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:path.py
import os
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#print (project_path)

#测试用例路径
case_path=os.path.join(project_path,'test_data','test_api.xlsx')
print(case_path)

#配置文件路径
config_path=os.path.join(project_path,'conf','case.conf')
#print(config_path)

#输出的日志的路径
log_path=os.path.join(project_path,'test_result','test_log','testlog.txt')
#print(log_path)

#输出的html报告的路径
report_path=os.path.join(project_path,'test_result','test_report','test_report.html')
#print(log_path)