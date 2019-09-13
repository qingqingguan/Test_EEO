# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 17:25
# @Author  : qingqingguan
# @Email   : 18229918212@163.com
# @File    : Client.py
# @Software: PyCharm

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from  selenium import  webdriver
import os
from selenium.webdriver import DesiredCapabilities
import yaml
class SeleniumClient(object):

    driver:WebDriver
    @classmethod
    def open_browser(cls) -> WebDriver:
        return cls.initDriver("open_browser")

    @classmethod
    def restart_browser(cls) -> WebDriver:
        return cls.initDriver('restart_browser')

    @classmethod
    def initDriver(cls, key):
        # 加载yaml文件
        YAML_DIR = os.getcwd()
        print(YAML_DIR)
        if YAML_DIR.endswith('testcase'):
            YAML_DIR = '../data/'
        else:
            YAML_DIR = 'data/'

        driver_data = yaml.load(open(YAML_DIR + 'driver.yaml'))
        url = driver_data[key]['url']
        implicitly_wait = driver_data[key]['implicitly_wait']
        # cls.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(implicitly_wait)
        cls.driver.get(url)
        cls.driver.maximize_window()
        return cls.driver