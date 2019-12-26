# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction, CheckUpdateBtn, ClearBackgroundApps, CheckOTAIsRunAtBackground, \
    DataToWIFIDownload


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    DataToWIFIDownload()
    ConnectAppium.driver.implicitly_wait(5)
    ClearBackgroundApps()
    assert CheckOTAIsRunAtBackground() == True, 'WiFi状态下，清除任务管理器后，判断系统更新应用是否在后台运行（即OTA自动重启）'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])