from os.path import abspath, dirname
import configparser as cparser


base_dir = dirname(dirname(abspath(__file__)))
file_path = base_dir + "/data_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host_Fiiipay = cf.get("base_url", "url_xxx")
host_Fiiipos = cf.get("base_url", "url_xxx")
host_FiiiposWeb = cf.get("base_url", "url_xxx")

# 获取Fiiipay的请求url
def get_url_xxx():
    return host_Fiiipay

# 获取Fiiipos的请求url
def get_url_xxx():
    return host_Fiiipos

# 获取FiiiposWeb的请求url
def get_url_xxx():
    return host_FiiiposWeb
