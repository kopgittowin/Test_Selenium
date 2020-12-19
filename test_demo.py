#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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


def test_addmember():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    with open('data.yml', encoding='utf_8') as f:
        yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
        driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.find_element_by_id('menu_contacts').click()
    ele = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(ele))
    while True:
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id('username')
        if len(element) > 0:
            break
    driver.find_element_by_id('username').send_keys('黄二')
    driver.find_element_by_id('memberAdd_acctid').send_keys('kopnum2')
    driver.find_element_by_id('memberAdd_phone').send_keys(13611223345)
    driver.find_element_by_css_selector('.js_btn_save').click()
    sleep(2)
    eles = driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
    name_list = []
    for value in eles:
        # 获取元素属性title的值，存入list内
        # print(value.get_attribute("title"))
        name_list.append(value.get_attribute("title"))
    # 断言目标名字是否在列表内
    assert "黄二" in name_list
    print(name_list)
