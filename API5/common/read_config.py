#-*-conding:utf-8-*-
#@Time :2020/1/1812:42
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:read_config.py
from configparser import ConfigParser
from API5.common import project_path
class ReadConfig:
    def __init__(self,filename):
        self.cf=ConfigParser()
        self.cf.read(filename,encoding='utf-8')  #读取文件，用read函数，而且要用utf-8格式

    def get_str(self,section,option):
        str=self.cf.get(section,option)
        return str

    def get_other(self, section, option):
        str = self.cf.get(section, option)
        return eval(str)

    def get_int(self,section,option):
        str=self.cf.getint(section,option)
        return str

    def get_float(self, section, option):
        str = self.cf.getfloat(section, option)
        return str

    def get_boolean(self,section,option):
        str=self.cf.getboolean(section,option)
        return str

if __name__=='__main__':
    ex=ReadConfig(project_path.config_path)
    b=ex.get_other('RechargeCase','case_id')
    print(b)
    print(type(b))