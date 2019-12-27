# coding:utf-8 #设置编码格式
import os

import pytest

from test_case.Config import ConnectAppium, platformName, platformVersion, deviceName
from test_case.OTAUtil import ConnectAppiumAndAction, CheckDownloadFinishMD5Checked, CheckOTAFullStorageTips, \
    ReleaseFillDataApp, isElement, ClearAppData


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    ClearAppData('System Update')
    ConnectAppium.DisConnectAppium()
    setting_desired_caps = {'platformName': platformName,
                            'platformVersion': platformVersion,
                            'deviceName': deviceName,
                            'appPackage': 'cn.test.filldata',
                            'appActivity': 'cn.test.filldata.FillData',
                            'newCommandTimeout': '2000'}
    ConnectAppium.driver.start_session(setting_desired_caps, None)
    print("断开重新建立APPIUM连接成功,进入设置应用")
    CheckOTAFullStorageTips()
    ConnectAppium.driver.implicitly_wait(3)
    FlagTips = 0
    if isElement('id', 'com.sunmi.ota:id/dialog_title'):
        print('Success：进入系统更新应用，提示内存空间不足，点击取消退出应用')
        ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/cancle').click()
        ConnectAppium.driver.implicitly_wait(5)
        FlagTips = 1
    elif isElement('id', 'android:id/button1'):
        print('Success：进入系统更新应用，提示内存空间不足，点击取消退出应用')
        ConnectAppium.driver.find_element_by_id('android:id/button1').click()
        ConnectAppium.driver.implicitly_wait(5)
        FlagTips = 1
    else:
        ConnectAppium.driver.implicitly_wait(3)
    ReleaseFillDataApp()
    assert FlagTips == 1, '判断存储空间满时，进入OTA检查是否有弹框提示'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])