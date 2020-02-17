#-*-conding:utf-8-*-
#@Time :2020/1/1812:42
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:read_logging.py
import logging
from API5.common.read_config import ReadConfig
from API5.common import project_path

class ReadLog:
    def __init__(self):
        rc=ReadConfig(project_path.config_path)
        self.log_name=rc.get_str('LOG','log_name')
        self.log_level=rc.get_str('LOG','log_level')
        self.stream_level = rc.get_str('LOG', 'stream_level')
        self.file_level = rc.get_str('LOG', 'file_level')
        self.format = rc.get_str('LOG', 'format')

    def my_log(self,level,msg):
        #1定义日志采集器名称和等级
        mylog=logging.getLogger(self.log_name)
        mylog.setLevel(self.log_level)

        # 2 定义输出渠道  StreamHandler输出到控制台 ,FileHandler输入到文件
        fm=logging.Formatter(self.format)#定义输出格式 #fm=logging.Formatter('%(asctime)s-%(levelname)s-%(name)s-%(filename)s-%(message)s')

        sh=logging.StreamHandler(stream=None)
        sh.setLevel(self.stream_level)
        sh.setFormatter(fm)

        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')  #文件地址用绝对路径
        fh.setLevel(self.file_level)
        fh.setFormatter(fm)

        #3 对接，最终输出的信息是两者交集（定义的级别和渠道的基本的交接
        mylog.addHandler(sh)
        mylog.addHandler(fh)

        # 4.调用mylogger，之前的对象是logging，现在变成mylogger
        if level.upper()=='DEBUG':
            mylog.debug(msg)

        elif level.upper() == 'INFO':
            mylog.info(msg)

        elif level.upper() == 'WARNING':
            mylog.warning(msg)

        elif level.upper() == 'ERROR':
            mylog.error(msg)

        elif level.upper() == 'CRITICAL':
            mylog.critical(msg)
        else:
            print('不支持这种格式日志')

        # 5.删除去掉，一定要删除渠道
        mylog.removeHandler(sh)
        mylog.removeHandler(fh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)
    def info(self,msg):
        self.my_log('INFO',msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__=='__main__':
    log=ReadLog()
    #log.my_log('ERROR')
    log.my_log('DEBUG','报错信息debug')