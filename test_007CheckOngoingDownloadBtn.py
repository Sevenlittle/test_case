# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction, CheckUpdateBtn, CheckOngoingDownloadBtn


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    assert CheckOngoingDownloadBtn() == True, '判断当前界面暂停后点击继续下载是否能够继续下载'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])