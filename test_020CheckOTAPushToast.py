# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction, CheckUpdateBtn, CheckOTAPushToast


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    assert CheckOTAPushToast() == True, '判断系统更新应用推送通知后，通知栏是否有消息提醒'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])