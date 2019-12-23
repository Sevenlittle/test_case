import subprocess

from appium import webdriver

platformName = 'Android'
platformVersion = '6.0'
deviceName = 'PE04D85550013'
appPackage = 'com.sunmi.ota'
appActivity = 'com.sunmi.ota.ui.activity.UpgradeActivity'

# 定义一个desired_caps字典来保存启动APP所需的那5个参数
class ConnectAppium:
    desired_caps = {'platformName': platformName,
                    'platformVersion': platformVersion,
                    'deviceName': deviceName,
                    'appPackage': appPackage,
                    'appActivity': appActivity,
                    'newCommandTimeout': '2000'}
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']

    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6

    @staticmethod
    def DevicesIsConnect():
        command = 'adb devices'
        pi = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        print(pi.stdout.read())

    @staticmethod
    def DisConnectAppium():
        ConnectAppium.driver.quit()