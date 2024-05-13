import unittest
from test.case.user.test_xzs_reg import MyTestCase as regtest
from test.case.user. test_xzs_login import MyTestCase as logintset
from lib.HTMLTestRunner import  HTMLTestRunner
from config.config import *
class MyTestCase(unittest.TestCase):
    def test_suit(self):

        suit=unittest.TestSuite()

        suit.addTest(regtest("test_reg_ok"))

        suit.addTests([logintset("test_login_ok"),logintset("test_login_err")])
        unittest.TextTestRunner(verbosity=2).run(suit)
        # self.assertEqual(True,False)
    def test_makesuit(self):

        suit1=unittest.makeSuite(regtest,"test_reg_ok")

        suit2=unittest.makeSuite(logintset)
        suit5=unittest.TestSuite([suit1,suit2])
        with open(report_file,"w")as f:
           unittest.TextTestRunner(verbosity=2).run(suit5)
    def test_loader(self):

        suit3=unittest.TestLoader().loadTestsFromTestCase(logintset)
        with open(report_file, "wb") as f:
            HTMLTestRunner(
                stream=f,
                title="xzs登录用例",
                description="xzs登录用例集",
                verbosity=2
            ).run(suit3)

    # def test_discover(self):
    #     suit4=unittest.TestLoader().discover("./")
    #     unittest.TextTestRunner(verbosity=2).run(suit4)

if __name__ == '__main__':
    unittest.main()
