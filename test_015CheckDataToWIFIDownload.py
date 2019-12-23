# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium, appPackage, appActivity
from test_case.OTAUtil import ConnectAppiumAndAction, WIFIDownloadToDataDownload, \
    GetConnectState, DataToWIFIDownload


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    DataToWIFIDownload()
    ConnectAppium.driver.implicitly_wait(5)
    ConnectAppium.driver.keyevent(187)
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.android.systemui:id/clean').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.start_activity(appPackage, appActivity)
    ConnectAppium.driver.implicitly_wait(3)
    DownloadBtn = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').text
    assert DownloadBtn == 'Suspend the download', '判断当前下载网络是否是wifi网络，切换至WiFi网络后自动下载更新包'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])