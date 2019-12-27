# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction, CheckUpdateBtn, CheckDownloadSpeedBelowLimitedSpeed


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    assert CheckDownloadSpeedBelowLimitedSpeed('10.00MB/s') == True, '判断当前下载速度设置后，实际下载速度是否在设置速度值下方'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])