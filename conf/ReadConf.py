#coding=utf-8

import ConfigParser
import os
import time
import random

prjDir = os.path.split(os.path.realpath(__file__))[0]
conf_path = os.path.join(prjDir, "conf.ini")


def load_config(file_path):
    config = ConfigParser.ConfigParser()
    try:
        if os.path.exists(file_path):
            config.read(file_path)
            return config
    except:
        print "%s is not exist", file_path


def get_config(section, option):
    cf = load_config(conf_path)

    # print cf.get(section, option)
    return cf.get(section, option)


def read_appInfo():
    cf = load_config(conf_path)

    app_dict = {}

    # options = cf.options('App')
    # print options
    section = 'AppInfo'
    app_dict['platformName'] = cf.get(section, 'platformName')
    app_dict['platformVersion'] = cf.get(section, 'platformVersion')
    app_dict['deviceName'] = cf.get(section, 'deviceName')
    app_dict['appPackage'] = cf.get(section, 'appPackage')
    app_dict['appActivity'] = cf.get(section, 'appActivity')

    print app_dict
    return app_dict

# read_appInfo('conf.ini')
# get_config('AppInfo', 'ip')

