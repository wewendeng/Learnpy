from selenium.webdriver import Remote
import time

'''
发邮件？
1、登录mail.126.com /  user/pawd  接收：标题，正文 附件

2、客户端：foxmail  user/pawd 协议：SMTP P0P3 接收：标题，正文 附件
'''

def add(a, b):
    '''
        add() 方法需要接收到两个变量，返回两个参数相加的结果。
    例：
        add(3,5)
    '''
    return a + b


if __name__ == '__main__':
    print(time.strftime("%Y_%m_%d %H_%M_%S"))
