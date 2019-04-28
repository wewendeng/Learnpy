import unittest
import requests
import json
import time
import sys
sys.path.append("..")
from common import get_base_url


class SendSMSCodeTest(unittest.TestCase):
    '''
    验证注册短信验证码
    '''

    def setUp(self):
        self.url = get_base_url.get_url_Fiiipay() + '/Account/CheckRegisterSMSCode'
        self.url_sms = get_base_url.get_url_Fiiipay() + '/Account/SendRegisterSMSCode'
        self.headers = {"Content-Type": "application/json"}
        self.phone = int(time.time())

    def tearDown(self):
        pass

    def test_request_error(self):
        '''请求方法错误'''
        response = requests.get(self.url)
        result = response.json()
        self.assertEqual(response.status_code, 405)
        self.assertEqual(result["Message"], "The requested resource does not support http method 'GET'.")

    def test_parameter_not_json_format(self):
        '''请求参数不是JSON'''
        response = requests.post(self.url)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10000)
        self.assertEqual(result["Message"], "Network error, please try again.")

    def test_parameter_key_null(self):
        '''请求参数key为空，返回信息不准确'''
        response = requests.post(self.url, json={}, headers = self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10000)
        self.assertEqual(result["Message"], "Network error, please try again.")

    def test_parameter_velue_null(self):
        '''请求参数的value为空'''
        data = {"CountryId": "", "Cellphone": "", "SMSCode":""}
        response = requests.post(self.url, json=data, headers = self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10001)
        self.assertIn("Invalid Cellphone format", result["Message"])

    def test_countryid_is_str(self):
        '''请求参数国家id为字符串，接口返回信息不明确'''
        data = {"CountryId": "abc", "Cellphone": "13692127994", "SMSCode":"123456"}
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10001)
        self.assertIn("\r\n\r\n", result["Message"])

    def test_cellphont_not_digital(self):
        '''请求参数cellphone不是纯数字'''
        data = {"CountryId": "9", "Cellphone": "1369212abcd", "SMSCode":"123456"}
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10001)
        self.assertIn("Invalid Cellphone format.", result["Message"])

    def test_cellphont_add_code(self):
        '''请求参数cellphone包含地区码'''
        data = {"CountryId": "9", "Cellphone": "+86 13692127994", "SMSCode":"123456"}
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10001)
        self.assertIn("Invalid Cellphone format.", result["Message"])


    def test_cellphont_not_exist(self):
        '''号码不存在，接口返回信息不正确'''
        data = {"CountryId": "9", "Cellphone": self.phone, "SMSCode":"123456"}
        data_sms = {"CountryId": "9", "Cellphone":self.phone}
        requests.post(self.url_sms, json=data, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 0)
        self.assertIn("Verification passed.", result["Message"])


if __name__=='__main__':
    unittest.main()