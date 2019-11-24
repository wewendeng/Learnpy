# pyse2 Web UI 自动化项目

#### 特点：
* 整个测试过程只需要打开/关闭一次浏览器，大大缩短测试时间。

* 测试用例运行失败自动截图。

* 测试用例运行失败可以重跑。

* 测试数据参数化。

#### 依赖库：
__selenium：__ Web自动化测试库
https://pypi.python.org/pypi/selenium

__pytest：__ 单元测试框架
https://pypi.python.org/pypi/pytest

__pytest-html：__ 生成html测试报告
https://pypi.python.org/pypi/pytest-html

__pytest-rerunfailures：__ 失败重跑
https://pypi.python.org/pypi/pytest-rerunfailures

#### 安装：

```
pip install -r requirements.txt
```

#### demo：

```python
@pytest.mark.parametrize(
    "name, searchkey",
    [("1", "Selenium"),
     ("2", "pytest文档"),
     ])
def test_baidu_search(name, searchkey, browser):
    bd = BaiduPage(browser)
    bd.open()
    bd.search_input(searchkey)
    bd.search_button()
    sleep(1)
    title = bd.search_title()
    assert title == searchkey+"_百度搜索"
```
