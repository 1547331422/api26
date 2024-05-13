import unittest
def setUpModule():#当前模块只执行一次
    print('=== setupmodel ===')
def tearDownModule():
    print('=== tearDownModule ===')
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass')
    #在所有的用例执行之后都会运行一次
    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass')
    #在每个用例执行之前都会运一次
    def setup(self):
        print('setup')
    #在每个用例执行之后都运行一次
    def tearDown(self):
        print('teardown')
    #在所有的测试用例必须以test开头
    def test_01(self):
        print('test01')
        self.assertEqual(True,True)
    def test_02(self):
        print('tset02')
        self.assertIn('h','hello')
    def test_03(self):
        print('test03')
        self.assertIsNot(2,4/2)
    def test_04(self):
        print('test04')
        self.assertGreater(7,4)
    def test_05(self):
        print('test05')
        self.assertIsInstance([1,2],list)

if __name__ == '__main__':
    unittest.main()
