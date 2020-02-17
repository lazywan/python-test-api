#-*-conding:utf-8-*-
#@Time :2020/1/1718:42
#@Author:caowanwan
#@Email:1127825076@qq.com
#@File:HTTP_.py

import requests

class HttpRequest:
    '''根据method来决定发起get请求还是post请求'''

    def request(self,method,url,param,cookie):
        '''url 发送的地址
        param 参数
        rtype有返回值，返回结果是响应报文'''
         #定义resp为全局变量，否则调用test_invest报错UnboundLocalError: local variable 'resp' referenced before assignment
        #global resp
        if method.upper()=='GET':
            try:
                resp=requests.get(url,params=param,cookies=cookie)
            except Exception as e:
                print(e)
        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param,cookies=cookie)
            except Exception as e:
                print(e)
        else:
            print('不支持该种方式')
            resp=None

        return resp

if __name__=='__main__':
    method='get'
    url='http://test.lemonban.com/futureloan/mvc/api/member/login'
    param={'mobilephone':18114800295,'pwd':123456,'regname':'caowanwan'}
    cookies=None
    rest=HttpRequest().request(method,url,param,cookies)
    cookie =rest.cookies
    print(rest.text)
    print(rest.headers)
    print(cookie)