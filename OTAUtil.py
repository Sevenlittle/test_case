import os
import subprocess
# 引入appium库中和webdriver包
import time

from selenium.common.exceptions import NoSuchElementException

from test_case.Config import ConnectAppium, appPackage, appActivity, platformName, platformVersion, deviceName


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
    dengdai = 99
    CheckResult = 0
    while dengdai < 100:
        if 'Reboot the update' in ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').text:
            print('UpdatePackage download finish -100%')
            dengdai = 101
            CheckResult = 1
        elif 'Download again' in ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').text:
            ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').click()
            dengdai = 101
            CheckResult = 2
        else:
            print('Have not finished download, wait for 3-seconds to continue download! ')
            ConnectAppium.driver.implicitly_wait(5)
            # ExceptionConnectionHandler()
            dengdai = dengdai - 1
            CheckResult = 0
    return CheckResult


def ClearAppData(appname):
    ConnectAppium.driver.start_activity('com.android.settings', 'com.android.settings.Settings')
    ConnectAppium.driver.implicitly_wait(5)
    print("Success:切换进入设置应用成功")
    _find_by_scroll('Apps')
    ConnectAppium.driver.implicitly_wait(10)
    _findapp_by_scroll(appname)
    ConnectAppium.driver.implicitly_wait(5)
    storage = ConnectAppium.driver.find_element_by_android_uiautomator('new UiSelector().text("Storage")')
    ConnectAppium.driver.implicitly_wait(3)
    storage.click()
    ConnectAppium.driver.implicitly_wait(3)
    cleardata = ConnectAppium.driver.find_element_by_android_uiautomator('new UiSelector().text("Clear data")')
    ConnectAppium.driver.implicitly_wait(3)
    cleardata.click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('android:id/button1').click()
    ConnectAppium.driver.implicitly_wait(3)


def CheckOTAFullStorageTips():
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('cn.test.filldata:id/edit_fill_percent_value').clear()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('cn.test.filldata:id/edit_fill_percent_value').send_keys('100')
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('cn.test.filldata:id/btn_start_fill').click()
    i = 0
    while i >= 0:
        if isElement('id', 'android:id/alertTitle'):
            print('提示内存空间不足，点击取消')
            ConnectAppium.driver.find_element_by_id('android:id/button1').click()
            ConnectAppium.driver.implicitly_wait(5)
            i = i + 1
        elif ConnectAppium.driver.find_element_by_id('cn.test.filldata:id/text_available_space_value').text == '0MB':
            print('填充完成，退出应用')
            i = -1
        else:
            print('填充中，继续等待...')
            ConnectAppium.driver.implicitly_wait(5)
            i = i + 1
    ConnectAppium.driver.implicitly_wait(60)
    if 'Internal storage running out' in ConnectAppium.driver.find_element_by_id('android:id/alertTitle').text:
        ConnectAppium.driver.find_element_by_id('android:id/button1').click()
    ConnectAppium.driver.implicitly_wait(10)
    if isElement('id', 'android:id/alertTitle'):
        ConnectAppium.driver.find_element_by_id('android:id/button1').click()
        ConnectAppium.driver.implicitly_wait(5)
    # ConnectAppium.driver.start_activity(appPackage, appActivity)
    comm = 'adb shell am start -n com.sunmi.ota/com.sunmi.ota.ui.activity.UpgradeActivity'
    text1 = os.popen(comm)
    context1 = text1.read()
    print(context1)


def ReleaseFillDataApp():
    ConnectAppium.driver.start_activity('cn.test.filldata', 'cn.test.filldata.FillData')
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('cn.test.filldata:id/btn_clean_data').click()
    ConnectAppium.driver.implicitly_wait(5)


def isElement(identifyBy,c):
    """
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    """
    flag=None
    try:
        if identifyBy == "id":
            # self.driver.implicitly_wait(60)
            ConnectAppium.driver.find_element_by_id(c)
        elif identifyBy == "xpath":
            # self.driver.implicitly_wait(60)
            ConnectAppium.driver.find_element_by_xpath(c)
        elif identifyBy == "class":
            ConnectAppium.driver.find_element_by_class_name(c)
        elif identifyBy == "link text":
            ConnectAppium.driver.find_element_by_link_text(c)
        elif identifyBy == "partial link text":
            ConnectAppium.driver.find_element_by_partial_link_text(c)
        elif identifyBy == "name":
            ConnectAppium.driver.find_element_by_name(c)
        elif identifyBy == "tag name":
            ConnectAppium.driver.find_element_by_tag_name(c)
        elif identifyBy == "css selector":
            ConnectAppium.driver.find_element_by_css_selector(c)
        elif identifyBy == "text":
            ConnectAppium.driver.find_element_by_android_uiautomator('new UiSelector().text("'+c+'")')
        flag = True
    except NoSuchElementException as e:
        flag = False
    finally:
        return flag


def CheckChangelogLanguageContainChinese():
    ConnectAppium.driver.start_activity(appPackage, appActivity)
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/iv_arrow').click()
    ConnectAppium.driver.implicitly_wait(3)
    logcontext = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/version_content_tv').text
    for _char in logcontext:
        if '\u4e00' <= _char <= '\u9fa5':
            print('日志语言中包含中文，判断为中文')
            return True
    return False


def GetAndSetSystemLanguage(language):
    # language include '中文 (简体)' / 'English (United States)'
    ConnectAppium.driver.start_activity('com.android.settings', 'com.android.settings.Settings')
    ConnectAppium.driver.implicitly_wait(5)
    print("Success:切换进入设置应用成功")
    if '无线和网络' == ConnectAppium.driver.find_element_by_id('com.android.settings:id/category_title').text:
        _find_by_scroll('语言和输入法')
    elif 'Wireless & networks' in ConnectAppium.driver.find_element_by_id('com.android.settings:id/category_title').text:
        _find_by_scroll('Language & input')
    ConnectAppium.driver.implicitly_wait(5)
    if language in ConnectAppium.driver.find_element_by_id('android:id/summary').text:
        print('Success to get System language, System Language is equal to language', ConnectAppium.driver.find_element_by_id('android:id/summary').text)
    else:
        ConnectAppium.driver.find_element_by_id('android:id/summary').click()
        ConnectAppium.driver.implicitly_wait(5)
        _find_item_by_scroll(language)
        ConnectAppium.driver.implicitly_wait(5)
        if language in ConnectAppium.driver.find_element_by_id('android:id/summary').text:
            print('Success to set language')
        else:
            print('Fail to set Language!')


def CheckOTAIsRunAtBackground():
    if isElement('id', 'com.woyou.launcher:id/workspace'):
        print('当前界面在主菜单界面，不在系统更新应用')
    else:
        print('当前界面不在主菜单界面，按HOME键返回主界面')
        ConnectAppium.driver.keyevent(3)
        return False
    comm = 'adb shell "ps | grep ota"'
    runatbackground = os.popen(comm)
    context = runatbackground.read()
    print(context)
    if 'com.sunmi.ota' in context:
        print('系统更新应用运行在后台')
        return True
    else:
        print('系统更新应用不在后台运行')
        return False


def ClearBackgroundApps():
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.keyevent(187)
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.android.systemui:id/clean').click()
    ConnectAppium.driver.implicitly_wait(3)
    print('后台任务清除完成！')


def CheckOTAPushToast():
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/iv_function').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_update_settings').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.save_screenshot('Test020_BeforeChangeWIFIBtn.png')
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/switch_button').click()
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.save_screenshot('Test020_AfterChangeWIFIBtn.png')
    ClearBackgroundApps()
    comm = 'adb shell "am broadcast -a com.sunmi.ota"'
    pushotatoast = os.popen(comm)
    context = pushotatoast.read()
    print(context)
    ConnectAppium.driver.implicitly_wait(5)
    ConnectAppium.driver.open_notifications()
    ConnectAppium.driver.implicitly_wait(5)
    if 'discovered, please update!' in ConnectAppium.driver.find_element_by_id('android:id/text').text:
        print('Success：通知栏中找到了新版本消息提醒通知')
        ConnectAppium.driver.keyevent(4)
        return True
    else:
        print('Fail：通知栏中未找到了新版本消息提醒通知')
        ConnectAppium.driver.keyevent(4)
        return False


def CheckDownloadSpeedBelowLimitedSpeed(settingspeed):
    CheckChangeWIFIDownloadSpeed(settingspeed)
    num = settingspeed[:-4]
    print('设置的下载速度为', settingspeed)
    if 'MB/s' in settingspeed:
        num1 = string_to_float(num)*1024
    elif 'Speed not limited' in settingspeed:
        num1 = 100000
    elif 'KB/s' in settingspeed:
        num1 = string_to_float(num)
    print('设置的下载速度在截取字符串之后转换KB为', num1)
    ConnectAppium.driver.implicitly_wait(3)
    ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/btn_main').click()
    ConnectAppium.driver.implicitly_wait(3)
    time.sleep(3)
    if CorrentDownloadSpeed() - num1 > 0:
        print('Fail：当前下载速度在设置速度值之上')
        return False
    else:
        print('Success：当前下载速度在设置速度值之下')
        return True


def CorrentDownloadSpeed():
    currentspeed = ConnectAppium.driver.find_element_by_id('com.sunmi.ota:id/tv_current_speed').text
    if len(currentspeed) == 0:
        print('当前获取下载速度为空，等待3秒继续获取下载速度')
        time.sleep(3)
    else:
        print('当前下载速度为：', currentspeed)
        currentspeed1 = currentspeed[:-4]
        if 'MB/s' in currentspeed:
            num2 = string_to_float(currentspeed1) * 1024
        elif 'Speed not limited' in currentspeed:
             num2 = 100000
        elif 'KB/s' in currentspeed:
            num2 = string_to_float(currentspeed1)
        print('当前的下载速度在截取字符串之后转换KB为', num2)
    return num2


def string_to_float(str):
    return float(str)


def _find_item_by_scroll(item_name):
    i = 1
    while i > 0:
        if isElement('text', item_name):
            ConnectAppium.driver.find_element_by_android_uiautomator('new UiSelector().text("'+item_name+'")').click()
            ConnectAppium.driver.implicitly_wait(5)
            i = -1
        else:
            ConnectAppium.driver.swipe(400, 500, 400, 100, 1000)
            time.sleep(3)
            i = i + 1


def _find_by_scroll(item_name):
    item = ConnectAppium.driver.find_element_by_android_uiautomator \
        ('new UiScrollable(new UiSelector().resourceId("com.android.settings:id/dashboard")).'
         'scrollIntoView(new UiSelector().textContains("'
         + item_name + '"))')
    ConnectAppium.driver.implicitly_wait(5)
    item.click()


def _findapp_by_scroll(app_item_name):
    time.sleep(20)
    item = ConnectAppium.driver.find_element_by_android_uiautomator \
        ('new UiScrollable(new UiSelector().resourceId("android:id/list")).'
         'scrollIntoView(new UiSelector().textContains("'
         + app_item_name + '"))')
    ConnectAppium.driver.implicitly_wait(5)
    item.click()


def get_size():
    x = ConnectAppium.driver.get_window_size()['width']
    y = ConnectAppium.driver.get_window_size()['height']
    return x, y


def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[0] * 0.25)  # 终点y坐标
    ConnectAppium.driver.swipe(x1, y1, x1, y2, 1000)


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
