# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 17:30
# @Author  : qingqingguan
# @Email   : qingqing.guan@eeoa.com
# @File    : BasePage.py
# @Software: PyCharm

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from driver.Client import SeleniumClient
import yaml
import time
import os
class BasePage(object):

    def __init__(self):
        self.driver: WebDriver=self.getDriver()
        self.YAML_DIR = self.get_yaml_dir()

    @classmethod
    def getDriver(cls):
        cls.driver = SeleniumClient.driver
        return cls.driver


    def get_yaml_dir(self):
        YAML_DIR = os.getcwd()
        print(YAML_DIR)
        if YAML_DIR.endswith('testcase'):
            YAML_DIR = '../data/'
        else:
            YAML_DIR = 'data/'
        return YAML_DIR

    @classmethod
    def getClient(cls):
        return SeleniumClient


    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text))

    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)


    def loadSteps(self,po_path, key, **kwargs):
        file = open(po_path,'rb')
        po_data = yaml.load(file)
        po_method = po_data[key]

        for step in po_method:
            step: dict
            time.sleep(4)
            element: WebElement=self.driver.find_element(by=step['by'], value=step['locator'])
            #把action强制转换为字符串格式，并且小写
            action=str(step['action']).lower()
            if action == "click":
                element.click()
            elif action == "sendkeys":
                text=str(step['text'])
                for k,v in kwargs.items():
                    origin=text
                    text=text.replace("$%s" %k, v)
                    print("update text: %s %s " %(origin, text))
                element.send_keys(text)
            elif action == "text":
                return element.text
            elif action == 'get_attribute':
                return element.get_attribute(step['attribute'])
            else:
                print("UNKNOW COMMAND %s" % step)