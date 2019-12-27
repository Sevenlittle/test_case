# coding:utf-8 #设置编码格式
import pytest

from test_case.Config import ConnectAppium
from test_case.OTAUtil import ConnectAppiumAndAction, CheckUpdateBtn, GetAndSetSystemLanguage, \
    CheckChangelogLanguageContainChinese


def test_main():
    # 通过webdriver包下面的Remote方法打开App
    ConnectAppium.DisConnectAppium()
    ConnectAppium.driver.start_session(ConnectAppium.desired_caps, None)
    print("断开重新建立APPIUM连接成功")
    ConnectAppiumAndAction()
    # language include '中文 (简体)' / 'English (United States)'
    GetAndSetSystemLanguage('English (United States)')
    assert CheckChangelogLanguageContainChinese() == False, '判断当前系统语言为英语时，日志语言是否包含中文'


if __name__ == '__main__':
    pytest.main(['--html=./report.html', 'test_022CheckChangelogLanuageContainChinese.py'])