import unittest
from selenium import webdriver
from time import sleep


class BaiduTest(unittest.TestCase):
    """ 百度搜索测试 """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        pass

    def search_key(self, search_key):
        search_input_text = self.driver.find_element_by_id("kw")
        search_input_text.send_keys(search_key)
        search_input_text.submit()
        sleep(2)
        self.assertEqual(self.driver.title, search_key+"_百度搜索")

    def test_baid_case(self):
        """ 搜索关键字：HMTLTestRunner """
        self.search_key("HMTLTestRunner")

    def test_baid_case2(self):
        """ 搜索关键字：unittest """
        self.search_key("unittest")

    def test_baid_case3(self):
        """ 搜索关键字：python """
        self.search_key("python")


if __name__ == '__main__':
    unittest.main()






















#
