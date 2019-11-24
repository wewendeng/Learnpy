import time, sys
sys.path.append('./testcase')
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import pprint



# =============定义发送邮件==========
def send_mail(file_new):

    msg = MIMEMultipart() # 带附件实例
    with open(file_new, "rb") as fp:
        mail_body = fp.read() # 读取报告文件内容
    msg.attach(MIMEText(mail_body, 'html', 'utf-8')) # 邮件正文
    att = MIMEText(mail_body,"base64",'utf-8') # 附件格式
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"]='attachment;filename="report_test.html"' # filename是附件名字
    msg.attach(att)

    msg['Subject'] = Header("接口自动化测试报告", 'utf-8') # 邮件正文标题
    msg['from'] = 'weiwen.deng@xxx.com' # 邮件发送者
    msg['to'] = "dengweiwen2@xxx.com,495822910@xxx.com" # 邮件接收者
    
    # 连接SMTP服务器，并发送邮件
    smtp = smtplib.SMTP() 
    smtp.connect("smtp.exmail.qq.com")
    smtp.login("weiwen.deng@xxx.com", "HZT8caKd5ic5mSak")
    smtp.sendmail("weiwen.deng@xxx.com", msg['to'].split(','), msg.as_string())
    smtp.quit()
    pprint.pprint('email has send out !')

# 指定测试用例为当前文件夹下的 testcase 目录
test_dir = './testcase'
testsuit = defaultTestLoader.discover(test_dir, pattern='test_*.py')


if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='接口自动化测试',
                            description='运行环境：api-test, Requests, unittest ')
    runner.run(testsuit)
    fp.close()
    send_mail(filename)
