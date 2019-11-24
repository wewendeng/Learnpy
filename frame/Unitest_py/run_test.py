import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header



# =============定义发送邮件==========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("集成发自动发邮件-测试", 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("testingwtb@126.com", "a123456")
    smtp.sendmail("testingwtb@126.com", "testingwtb@126.com", msg.as_string())
    smtp.quit()
    print('email has send out !')


if __name__ == '__main__':

    suit = unittest.defaultTestLoader.discover(
           start_dir="./web_test_case",
           pattern='test_b*.py')

    now_time = time.strftime("%Y_%m_%d %H_%M_%S")

    report = "./report/"+ now_time +"result.html" #报告的名称

    f = open(report, 'wb')
    runner = HTMLTestRunner(
            stream=f,
            verbosity=1,
            title="百度测试报告",
            description="运行环境：Windows / Chrome, author: 虫师")

    runner.run(suit)
    f.close()
    send_mail(report)

    #runner = unittest.TextTestRunner()
    #runner.run(suit)

 #  集成HTMLTestRunner
 #  集成自动发邮件功能
