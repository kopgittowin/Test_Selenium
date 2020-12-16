#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID, 'kw').click()
        self.driver.find_element(By.ID, 'kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element(By.ID, 'su').click()
        self.driver.find_element(By.LINK_TEXT, '霍格沃兹测试学院 – 测试开发工程师的黄埔军校').click()


def test_wework():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    # driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.find_element_by_id('menu_contacts').click()
    sleep(3)
    driver.quit()


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    with open('data.yml', 'w', encoding='utf_8') as f:
        yaml.dump(cookies, f)
    # print(driver.get_cookies())


def test_login():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    with open('data.yml', encoding='utf_8') as f:
        yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
        driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    sleep(3)


def test_pytet():
    pass
