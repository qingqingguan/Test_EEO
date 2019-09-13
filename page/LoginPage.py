# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 17:38
# @Author  : qingqingguan
# @Email   : qingqing.guan@eeoa.com
# @File    : LoginPage.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from page.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
class LoginPage(BasePage):
    _error_message=('xxx')

    #手机号密码登录
    def loginByTelephone(self, account, password):
        self.driver.implicitly_wait(10)
        self.loadSteps("../data/LoginPage.yaml", "loginByTelephone", var1=account, var2=password)
        return self







