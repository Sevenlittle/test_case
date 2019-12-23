# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction,  CheckChangeWIFIDownloadSpeedCancelSaved


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    assert CheckChangeWIFIDownloadSpeedCancelSaved('40KB/s') == True, '判断当前界面关闭WiFi自动下载后，退出重新进入应用是否自动下载'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])