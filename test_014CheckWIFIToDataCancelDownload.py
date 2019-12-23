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
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/cancle').click()
    ConnectAppium.driver.implicitly_wait(5)
    DownloadBtn = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').text
    assert DownloadBtn == 'Continue to download', '判断当前下载网络切换至数据网络下载后取消立即下载是否继续下载更新包'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])