import unittest

def setUpModule():               #用例模块之后只执行一次
    print('=== setUpModlue ===')


def tearDownModule():            #用例模块之前只执行一次
    print('===  teardownmodule ===')

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):              #用例类之后只执行一次
        print('--- setupclass ---')

    @classmethod
    def tearDownClass(cls):          #用例类之前只执行一次
        print('--- teardownclass ---')


    def setUp(self):                #单用例之后只执行一次
        print('... setup ...')

    def tearDown(self):           #单用例之前只执行一次
        print('... teardown ...')


    def test_a(self):
        print('a')

    def test_B(self):
        print('B')

class Test_BB(unittest.TestCase):
    def test_BB(self):
        print('BB')


if __name__=='__main__':
    unittest.main()