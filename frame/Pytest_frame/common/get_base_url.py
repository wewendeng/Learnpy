from os.path import abspath, dirname
import configparser as cparser


base_dir = dirname(dirname(abspath(__file__)))
file_path = base_dir + "/data_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host_xxx1 = cf.get("base_url", "url_xxx1")
host_xxx2 = cf.get("base_url", "url_xxx2")
host_xxx3 = cf.get("base_url", "url_xxx3")

# 获取Fiiipay的请求url
def get_url_xxx1():
    return host_xxx1

# 获取Fiiipos的请求url
def get_url_xxx2():
    return host_xxx2

# 获取FiiiposWeb的请求url
def get_url_xxx3():
    return host_xxx3
