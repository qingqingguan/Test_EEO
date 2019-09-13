# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 17:46
# @Author  : qingqingguan
# @Email   : qingqing.guan@eeoa.com
# @File    : test_login.py
# @Software: PyCharm

from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from page.MainPage import MainPage
from page.LoginPage import LoginPage
from page.run import run
import pytest

class TestLogin(object):

    @classmethod
    def setup_class(cls):
        cls.LoginPage = run.main().gotoLogin()

    @pytest.mark.parametrize("telephone, pw, msg", [
        ("15001226075", "123456", "")
    ])


    def test_login_telephone(self, telephone, pw, msg):
        self.LoginPage.loginByTelephone(telephone, pw)
        from page.MainPage import MainPage
        return MainPage()

    def teardown(self):
        sleep(3)
        self.LoginPage.driver.quit()

