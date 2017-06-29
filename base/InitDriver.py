#coding=utf-8

#######################################################
# FileName:InitDriver.py
# Author:CathyZhang
# Date:2017-6-5
# Function Description:
#######################################################

from appium import webdriver
import conf.ReadConf
import requests
import json
import time


desired_caps = conf.ReadConf.read_appInfo()
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
# desired_caps['recreateChromeDriverSessions'] = 'True'
# desired_caps['autoLaunch'] = True
# desired_caps['automationName'] = 'UiAutomator2'

ip = conf.ReadConf.get_config('AppInfo', 'ip')
port = conf.ReadConf.get_config('AppInfo', 'port')
server_url = 'http://' + ip + ":" + port + '/wd/hub'


def start_driver():
    print('Start Driver...')
    driver = webdriver.Remote(server_url, desired_caps)
    time.sleep(10)
    return driver


# 判断appium server是否已启动
def is_running():
    url = server_url + '/status'
    response = requests.get(url)
    if str(response.status_code).startswith("2"):
        return True
    else:
        return False
