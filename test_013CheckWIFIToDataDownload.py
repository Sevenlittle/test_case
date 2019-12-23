# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction, WIFIDownloadToDataDownload, \
    GetConnectState


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    WIFIDownloadToDataDownload()
    ConnectAppium.driver.implicitly_wait(5)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').click()
    ConnectAppium.driver.implicitly_wait(10)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/ok').click()
    ConnectAppium.driver.implicitly_wait(5)
    assert GetConnectState() == 'DATA_ONLY', '判断当前下载网络是否是使用数据流量进行下载'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])