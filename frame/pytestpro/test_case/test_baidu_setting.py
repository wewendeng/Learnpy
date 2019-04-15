# coding=utf-8
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import pytest
try:
    from page_obj.baidu_page import BaiduPage
except ImportError:
    from .page_obj.baidu_page import BaiduPage


# 百度搜索设置--跳过测试
@pytest.mark.skip(reason="no way of currently testing this")
def test_baidu_a_setting(browser):
    bd = BaiduPage(browser, timeout=10)
    bd.open()
    bd.setings()
    bd.search_setting()
    bd.save_seting()


if __name__ == "__main__":
    pytest.main(["-s","test_baidu_setting.py"])
