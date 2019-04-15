import yagmail

# 帐号、地址信息
yag = yagmail.SMTP(user='dengw_w@163.com', password='deng3172', host='smtp.163.com')

#邮箱正文
contents = ['使用yagmail发送附件']

# 发送邮件
yag.send('495822910@qq.com', 'yalmail测试', contents, ['E:/selenium/code/send_mail/log1.txt'])