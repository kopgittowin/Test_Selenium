#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from selenium_po.page.base_page import BasePage
from selenium_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _ele_name = (By.ID, 'username')
    _ele_id = (By.ID, 'memberAdd_acctid')
    _ele_phone = (By.ID, 'memberAdd_phone')

    def add_member(self, name, id, phone):
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(2)
        return ContactPage(self.driver)

    def add_member_fail(self, name, id, phone):
        self.find(*self.ele_name).send_keys(name)
        self.find(*self.ele_id).send_keys(id)
        self.find(*self.ele_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(2)
        return ContactPage(self.driver)
