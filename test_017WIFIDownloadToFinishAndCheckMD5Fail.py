# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction, CheckDownloadFinishMD5Checked


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').click()
    ConnectAppium.driver.implicitly_wait(3)
    assert CheckDownloadFinishMD5Checked() == 2, '判断下载更新包完成后校验MD5值失败后点击重新下载，停止重试'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])