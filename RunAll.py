import unittest
import requests
import HTMLTestReportCN
suite=unittest.defaultTestLoader.discover('./')
# with open('suite.txt','w') as f:       #运行结果输出到文本文档
#     unittest.TextTestRunner(verbosity=2).run(suite)
f=open('2019-5-15自动化测试.html','wb')
HTMLTestReportCN.HTMLTestRunner(stream=f,title='接口测试结果',description='结果').run(suite)
f.close()





