# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction, CheckUpdateBtn, CheckDownloadLimtedBtn


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    CheckUpdateBtn()

    assert CheckDownloadLimtedBtn() == True, '判断当前界面是否在系统更新界面中的限速下载框'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])