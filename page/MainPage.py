# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 17:36
# @Author  : qingqingguan
# @Email   : qingqing.guan@eeoa.com
# @File    : MainPage.py
# @Software: PyCharm

from selenium.webdriver import ActionChains
from page.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from page.LoginPage import LoginPage
class MainPage(BasePage):

     def gotoLogin(self):
          time.sleep(3)
          print('跳到登录页面')
          self.loadSteps('../data/MainPage.yaml','gotoLogin')
          return LoginPage()
