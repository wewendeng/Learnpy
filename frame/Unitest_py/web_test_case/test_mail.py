import unittest
from selenium import webdriver
from time import sleep


class MailTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://mail.126.com")

    def test_mail_1(self):
        driver = self.driver
        sleep(2)
        driver.switch_to.frame('x-URS-iframe')
        driver.find_element_by_name("email").send_keys("")
        driver.find_element_by_name("password").send_keys("")
        driver.find_element_by_id("dologin").click()
        hint = driver.find_element_by_class_name("ferrorhead").text
        self.assertEqual(hint, "请输入帐号")
        driver.switch_to.default_content()


if __name__ == '__main__':
    unittest.main()






















#
