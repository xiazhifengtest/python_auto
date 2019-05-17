import requests
import unittest
import json
import getToken

# url='https://yk.xox5.com/yk/grade/getGradeAndSubjectByUserRoleList'
# token=getToken.getToken()
# headers={'Authorization':token,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
# r=requests.post(url=url,headers=headers)
# print(r.text)


class TestUsergetinfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#用例只执行一次
        print('setupclass')
    # @classmethod
    # def tearDownclass(cls):
    #     print('teardownclass')
    url='https://yk.xox5.com/yk/grade/getGradeAndSubjectByUserRoleList'
    token=getToken.getToken()                               #调用gettoken方法获取token

    def test_login_getinfo_r(self):                         #正常情况
        headers={'Authorization':self.token,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        res=requests.post(url=self.url,headers=headers)     #header中加入获取token的方法所得到的的token
        self.assertIn('1',res.text)                         #断言
        print(res.text)


    def test_login_getinfo_w(self): #请求不带token的错误情况
        headers = {
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        res = requests.post(url=self.url, headers=headers)
        self.assertIn('1', res.text)
        print(res.text)



if __name__=='__main__':
        unittest.main(verbosity=2)




