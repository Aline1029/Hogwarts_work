# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-07   20:08
# 文件名称    : test_fixture  PY
# 开发工具    : PyCharm
import pytest

@pytest.fixture()
def login():
    print('登陆操作')
    print('获取token')

def test_case1(login):
    print("测试用例1")


def test_case2():
    print('测试用例2')


def test_case3(login):
    print('测试用例3')