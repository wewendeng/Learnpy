import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# 发送邮箱服务器
smtpserver = 'smtp.126.com'
# 发送邮箱用户/密码
user = 'testingwtb@126.com'
password = 'a123456'
# 发送邮箱
sender = 'testingwtb@126.com'
# 接收邮箱
receiver = 'testingwtb@126.com'
# 邮件主题
subject = 'pyse17 发送邮件附件'

# 发送的附件
sendfile = open('D:\\result.html', 'rb').read()
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="result.html"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)


smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
