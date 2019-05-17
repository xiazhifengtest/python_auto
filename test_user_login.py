import unittest
import json
import requests

class TessUserlogin(unittest.TestCase):
    @classmethod           #用例类只执行一次
    def setUpClass(cls):
        pass
    # @classmethod
    # def tearDownClass(cls):
    #     pass
    url='https://yk.xox5.com/yk/login'


    def test_user_login_t(self):                       #正确的登录情况
        data={'username':'mayanju','password':'031064'}
        res=requests.post(url=self.url,data=data)
        self.assertIn('1',res.text)
        print(res.text)


    def test_user_login_f(self):                            #错误的登录情况
        data={'username':'mayanju','password':'03106'}
        res=requests.post(url=self.url,data=data)
        self.assertIn('1',res.text)
        print(res.text)



if '__name__'=='__main__':
    unittest.main()



