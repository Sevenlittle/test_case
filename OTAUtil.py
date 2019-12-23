import os
import subprocess
# 引入appium库中和webdriver包
import time

from test_case.Config import ConnectAppium, appPackage, appActivity


def ConnectAppiumAndAction():
    ConnectAppium.driver.implicitly_wait(5)
    ConnectAppium.driver.find_element_by_id("com.sunmi.ota:id/btn_main").click()
    ConnectAppium.driver.implicitly_wait(3)
    print("暂停下载")
    # ConnectAppium.driver.quit()
    # comm = 'adb reboot'
    # pi = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
    # time.sleep(60)
    command = 'adb devices'
    pi = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    print(pi.stdout.read())


def CheckUpdateBtn():
    ConnectAppium.driver.implicitly_wait(3)
    updatename = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_title').text
    if updatename == 'System Update':
        print('Success to Enter the System Update App')
        return True
    else:
        print('Fail to Enter the System Update App')
        return False


def CheckNewVersion():
    ConnectAppium.driver.implicitly_wait(3)
    newversionname = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_check_version').text
    if 'Discover new version' in newversionname:
        print('Success To Find New Version')
        return 1
    elif 'Current version is already the latest' in newversionname:
        print('Fail to find new version , the version is the latest !')
        return 2
    else:
        print('There are some errors in finding new version!')
        return 3


def CheckDownloadLimtedBtn():
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_speed_setting').click()
    ConnectAppium.driver.implicitly_wait(3)
    speedlimtedname = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/dialog_title').text
    if speedlimtedname == 'Download speed limit':
        print('Success to Enter the DownloadSpeedLimit dialog')
        return True
    else:
        print('Fail to Enter the DownloadSpeedLimit dialog')
        return False


def CheckAutoWIFIDownloadBtn():
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/iv_function').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_update_settings').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.save_screenshot('Test006_DefaultWIFIBtn.png')
    ConnectAppium.driver.keyevent(187)
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.android.systemui:id/clean').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.start_activity(appPackage, appActivity)
    DownloadBtn = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').text
    if DownloadBtn == 'Suspend the download':
        print('WIFI-Auto-Download has opened , Success to find suspend downloadBtn')
        return True
    else:
        print('WIFI-Auto-Download has closed , Failed to find suspend downloadBtn')
        return False


def CheckOngoingDownloadBtn():
    time.sleep(3)
    ConnectAppium.driver.find_element_by_id("com.sunmi.ota:id/btn_main").click()
    Ongoingupdatename = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').text
    if Ongoingupdatename == 'Suspend the download':
        print('Success to continue to download')
        return True
    else:
        print('Fail to continue to download')
        return False


def CheckClosedWIFIAutoDownloadBtn():
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/iv_function').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_update_settings').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.save_screenshot('Test007_BeforeChangeWIFIBtn.png')
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/switch_button').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.save_screenshot('Test007_AfterChangeWIFIBtn.png')
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.keyevent(187)
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.android.systemui:id/clean').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.start_activity(appPackage, appActivity)
    DownloadBtn = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').text
    if DownloadBtn == 'Continue to download':
        print('WIFI-Auto-Download has Closed , Success to find suspend downloadBtn')
        return True
    else:
        print('WIFI-Auto-Download has Opened , Failed to find suspend downloadBtn')
        return False


def CheckdefalutDownloadSpeed():
    DownloadLimitBtn = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_speed_setting').text
    if '20KB/s' in DownloadLimitBtn:
        print('Success to find DownloadLimitBtn-20KB/s')
        return True
    else:
        print('Fail to find DownloadLimitBtn-20KB/s')
        return False


def CheckChangeWIFIDownloadSpeed(SettingSpeed):
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_speed_setting').click()
    ConnectAppium.driver.implicitly_wait(3)
    i = 70
    while i > 0:
        ConnectAppium.driver.swipe(i, ConnectAppium.height/2-42, i+2, ConnectAppium.height/2-42, 3000)
        ConnectAppium.driver.implicitly_wait(3)
        if ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_current_speed').text == SettingSpeed:
            i = -1
            print("Success to swipe to SettingSpeed")
        else:
            i = i+3
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/ok').click()
    checksettingspeed = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_speed_setting').text
    if SettingSpeed in checksettingspeed:
        print('Success to save the SettingSpeed')
        return True
    else:
        print('Fail to save the SettingSpeed')
        return False


def CheckChangeWIFIDownloadSpeedCancelSaved(SettingSpeed):
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_speed_setting').click()
    ConnectAppium.driver.implicitly_wait(3)
    i = 70
    while i > 0:
        ConnectAppium.driver.swipe(i, ConnectAppium.height/2-42, i+2, ConnectAppium.height/2-42, 3000)
        ConnectAppium.driver.implicitly_wait(3)
        if ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_current_speed').text == SettingSpeed:
            i = -1
            print("Success to swipe to SettingSpeed")
        else:
            i = i+3
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/cancle').click()
    checksettingspeed = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_speed_setting').text
    if '20KB/s' in checksettingspeed:
        print('Success to Cancel Save the SettingSpeed')
        return True
    else:
        print('Fail to Cancel Save the SettingSpeed')
        return False


def CheckChangeWIFIDownloadSpeedSaved(SettingSpeed):
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_speed_setting').click()
    ConnectAppium.driver.implicitly_wait(3)
    i = 70
    while i > 0:
        ConnectAppium.driver.swipe(i, ConnectAppium.height/2-42, i+2, ConnectAppium.height/2-42, 3000)
        ConnectAppium.driver.implicitly_wait(3)
        if ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_current_speed').text == SettingSpeed:
            i = -1
            print("Success to swipe to SettingSpeed")
        else:
            i = i+3
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/ok').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.keyevent(187)
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.android.systemui:id/clean').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.start_activity(appPackage, appActivity)
    checksettingspeedsaved = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_speed_setting').text
    if SettingSpeed in checksettingspeedsaved:
        print('Success to save the SettingSpeed after clear app background')
        return True
    else:
        print('Fail to save the SettingSpeed after clear app background')
        return False


def WIFIDownloadToDataDownload():
    if ConnectAppium.driver.network_connection == ConnectAppium.DATA_ONLY:
        print(GetConnectState())
    else:
        print(GetConnectState())
        ConnectAppium.driver.set_network_connection(ConnectAppium.DATA_ONLY)


def GetConnectState():
    info={0: "NO_CONNECTION",
        1: "AIRPLANE_MODE",
        2: "WIFI_ONLY",
        4: "DATA_ONLY",
        6: "ALL_NETWORK_ON"}
    state = ConnectAppium.driver.network_connection
    print(state)
    return info.get(state)


def DataToWIFIDownload():
    if ConnectAppium.driver.network_connection == ConnectAppium.WIFI_ONLY:
        print(GetConnectState())
    else:
        print(GetConnectState())
        ConnectAppium.driver.set_network_connection(ConnectAppium.WIFI_ONLY)


def ExceptionConnectionHandler():
    ExceptionConnectTips = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/main_function_tv').text
    print(GetConnectState())
    if 'error' in ExceptionConnectTips:
        ConnectAppium.driver.implicitly_wait(3)
        ConnectAppium.driver.find_element_by_id("com.sunmi.ota:id/btn_main").click()
    elif 'timeout' in ExceptionConnectTips:
        ConnectAppium.driver.implicitly_wait(3)
        ConnectAppium.driver.find_element_by_id("com.sunmi.ota:id/btn_main").click()
    elif 'anomaly' in ExceptionConnectTips:
        ConnectAppium.driver.implicitly_wait(3)
        ConnectAppium.driver.find_element_by_id("com.sunmi.ota:id/btn_main").click()
        ConnectAppium.driver.implicitly_wait(3)
        ConnectAppium.driver.find_element_by_id("com.sunmi.ota:id/btn_main").click()
    else:
        print('There are some wrongs on Internet, please check !!!')


def CheckDownloadFinishMD5Checked():
    downloadbtn = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').text
    dengdai = 99
    while dengdai < 100:
        if 'Reboot the update' in downloadbtn:
            print('UpdatePackage download finish -100%')
            dengdai = 100
        elif downloadbtn == 'Continue to download':
            print('Stop downloading, now continue to download!')
            ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').click()
            ConnectAppium.driver.implicitly_wait(5)
            dengdai = dengdai - 1
        else:
            print('Have not finished download, wait for 3-seconds to continue download! ')
            ConnectAppium.driver.implicitly_wait(5)
            # ExceptionConnectionHandler()
            dengdai = dengdai - 1


def _find_by_scroll(item_name):
    item = ConnectAppium.driver.find_element_by_android_uiautomator \
        ('new UiScrollable(new UiSelector().resourceId("com.android.settings:id/dashboard")).'
         'scrollIntoView(new UiSelector().textContains("'
         + item_name + '"))')
    ConnectAppium.driver.implicitly_wait(5)
    item.click()


def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def swipeUp(driver, t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


def adbScreenOn(self):
    try:
        cmd = 'adb shell input keyevent 26'
        print(cmd)
        text = os.popen(cmd)
        content = text.read()
        print
        content + '手机屏幕亮屏成功'.decode('UTF-8').encode('GBK')
    except Exception as e:
        print(str(e))


def IsScreenOn(self):
    try:
        cmd = 'adb shell dumpsys window policy^|grep mScreenOnFully'
        print(cmd)
        text = os.popen(cmd)
        content = text.read()
        print
        content
        if 'mScreenOnEarly=true mScreenOnFully=true' in content:
            print
            'Pass: 手机屏幕已经是亮屏'.decode('UTF-8').encode('GBK')
        else:
            adbScreenOn()
    except Exception as e:
        print(str(e))
