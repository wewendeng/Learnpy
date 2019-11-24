import yagmail

#链接邮箱服务器
yag = yagmail.SMTP(user="testingwtb@126.com",
password="a123456",
host='smtp.126.com')

# 邮箱正文
f = open("D:\\result.html", "r", encoding='utf-8')
contents = f.read()
f.close()

#contents = ['This is the body, and here is just text http://somedomain/image.png',
#            'You can find an audio file attached.']

# 发送邮件
yag.send('testingwtb@126.com', '通过yagmail发送邮件', contents, ["d://result.html"])
















##
