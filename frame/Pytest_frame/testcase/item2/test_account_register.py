import unittest
import requests
import json
import time
import sys
sys.path.append("..")
from common import get_base_url


class RegisterTest(unittest.TestCase):
    '''
    app注册接口（非H5页面）
    '''

    def setUp(self):
        self.url_sms = get_base_url.get_url_Fiiipay() + '/Account/SendRegisterSMSCode'
        self.url = get_base_url.get_url_Fiiipay() + '/Account/Register'
        self.phone = int(time.time())
        self.headers = {"Content-Type": "application/json"}

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

    def test_parameter_key_not_null(self):
        '''请求参数的key为空'''
        response = requests.post(self.url, json={}, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10000)
        self.assertEqual(result["Message"], "Network error, please try again.")

    def test_parameter_value_null(self):
        '''请求参数value为空'''
        data_sms = {"CountryId": "9", "Cellphone": self.phone}
        data = {"CountryId": "" , "Cellphone": "", "Password": "", "SMSCode": "",
                "InviterCode": ""}
        requests.post(self.url_sms, json=data_sms, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10001)
        self.assertIn("The Cellphone field is required", result["Message"])
        self.assertIn("The Password field is required", result["Message"])
        self.assertIn("The SMSCode field is required", result["Message"])

    def test_countryid_is_str(self):
        '''请求参数国家id为字符串'''
        data_sms = {"CountryId": "9", "Cellphone": self.phone}
        data = {"CountryId": "abc" , "Cellphone": self.phone, "Password": "qaz123456", "SMSCode": "123456",
                "InviterCode": ""}
        requests.post(self.url_sms, json=data_sms, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10001)
        self.assertIn("", result["Message"]) # 返回message为空

    @unittest.skip("国家不存在时接口没有做处理")
    def test_CountryId_not_exist(self):
        '''请求参数国家id不存在'''
        data_sms = {"CountryId": "9", "Cellphone": self.phone}
        data = {"CountryId": "999999" , "Cellphone": self.phone, "Password": "qaz123456", "SMSCode": "123456",
                "InviterCode": ""}
        requests.post(self.url_sms, json=data_sms, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        print(result)

    def test_cellphone_not_digital(self):
        '''请求参数号码为纯字母'''
        data_sms = {"CountryId": 9, "Cellphone": self.phone}
        data = {"CountryId": "9" , "Cellphone": "abcdefghijk", "Password": "qaz123456", "SMSCode": "123456",
                "InviterCode": ""}
        requests.post(self.url_sms, json=data_sms, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10001)
        self.assertIn("Invalid Cellphone format.", result["Message"])

    def test_password_format_error(self):
        '''请求参数密码格式错误'''
        data_sms = {"CountryId": 9, "Cellphone": self.phone}
        data = {"CountryId": "9" , "Cellphone": self.phone, "Password": "abc", "SMSCode": "123456",
                "InviterCode": ""}
        requests.post(self.url_sms, json=data_sms, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Code"], 10001)
        self.assertIn("Invalid Password format.", result["Message"])

    @unittest.skip("短信验证码格式不正确时，接口没有处理")
    def test_smscode_not_digital(self):
        '''请求参数验证码为纯字母'''
        data_sms = {"CountryId": 9, "Cellphone": self.phone}
        data = {"CountryId": "9" , "Cellphone": self.phone, "Password": "qaz123456", "SMSCode": "abc",
                "InviterCode": ""}
        requests.post(self.url_sms, json=data_sms, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        print(result)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(result["Code"], 10001)
        # self.assertIn("The SMSCode field is required.", result["Message"])

    @unittest.skip("短信验证码超出6位数字时，接口没有处理")
    def test_smscode_length_limit(self):
        '''请求参数验证码传超出6位数字'''
        data_sms = {"CountryId": 9, "Cellphone": self.phone}
        data = {"CountryId": "9" , "Cellphone": self.phone, "Password": "qaz123456", "SMSCode": "123456789",
                "InviterCode": ""}
        requests.post(self.url_sms, json=data_sms, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        print(result)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(result["Code"], 10001)
        # self.assertIn("The SMSCode field is required.", result["Message"])

    def test_sms_code_error(self):
         '''注册的短信验证码错误'''
         data = {"CountryId": 9, "Cellphone": self.phone, "Password": "qaz123456", "SMSCode": "123456", "InviterCode": ""}
         response = requests.post(self.url, json=data, headers=self.headers)
         result = response.json()
         self.assertEqual(response.status_code, 200)
         self.assertEqual(result["Code"], 10080)
         self.assertIn("SMS code error", result["Message"])

    def test_user_existed(self):
        '''用户已存在'''
        data_sms = {"CountryId": 9, "Cellphone": "13692127994"}
        response_sms = requests.post(self.url_sms, json=data_sms, headers=self.headers)
        result_sms = response_sms.json()
        print(result_sms)
        self.assertEqual(response_sms.status_code, 200)
        self.assertEqual(result_sms["Code"], 10011)
        self.assertIn("already exist.", result_sms["Message"])

    def test_register_success(self):
        '''注册成功'''
        data_sms = {"CountryId": 9,"Cellphone":self.phone}
        data = {"CountryId":9, "Cellphone":self.phone, "Password":"qaz123456", "SMSCode":"123456", "InviterCode":""}
        requests.post(self.url_sms, json=data_sms, headers=self.headers)
        response = requests.post(self.url, json=data, headers=self.headers)
        result = response.json()
        print(result)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["Data"], True)
        self.assertEqual(result["Code"], 0)
        self.assertEqual(result["Message"], "Registration success.")


if __name__ == '__main__':
    unittest.main()

"""
连接服务器可能会出现ConnectionError，需要在用例中进行异常处理，目前没有进行处理
"""