import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.126.com'
# 发送邮箱用户/密码
user = 'testingwtb@126.com'
password = 'a123456'
# 发送邮箱
sender = 'testingwtb@126.com'
# 接收邮箱
receiver = 'testingwtb@126.com'
# 发送邮件主题
subject = 'pyse17自动发邮件'
# 编写 HTML 类型的邮件正文
msg = MIMEText('<html><h1> 你好！ </h1></html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()


'''
* 自已的邮箱（username,password）
* 对方的邮箱（帐号）
* 邮件（标题，正文，附件）

mail.qq.com
mail.126.com

foxamil(服务器：smtp.126.com/pop3.126.com)
'''
