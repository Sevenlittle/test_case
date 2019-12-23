# coding:utf-8 #设置编码格式
import pytest
from test_case.OTAUtil import ConnectAppiumAndAction, CheckUpdateBtn


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppiumAndAction()
    assert CheckUpdateBtn() == True, '判断当前界面是否在系统更新界面'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])
