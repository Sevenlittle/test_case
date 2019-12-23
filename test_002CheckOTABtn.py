# content of test_sample.py
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import _find_by_scroll, CheckUpdateBtn, ConnectAppiumAndAction


def test_main():
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    ConnectAppium.driver.start_activity('com.android.settings', 'com.android.settings.Settings')
    ConnectAppium.driver.implicitly_wait(5)
    print("Success:切换进入设置应用成功")
    _find_by_scroll('About device')
    _find_by_scroll('System updates')
    assert CheckUpdateBtn() == True, '进入设置后查找系统更新按钮，进入后判断当前界面是否在系统更新界面'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])