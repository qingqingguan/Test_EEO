# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 17:45
# @Author  : qingqingguan
# @Email   : qingqing.guan@eeoa.com
# @File    : run.py
# @Software: PyCharm

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import  webdriver
from selenium.webdriver import DesiredCapabilities
from driver.Client import SeleniumClient


YAML_DIR='../data/'
from page.BasePage import BasePage
from page.MainPage import MainPage
class run(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_browser()
        return MainPage()