#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium_po.page.base_page import BasePage


class ContactPage(BasePage):

    def click_add_member(self):

        from selenium_po.page.add_member_page import AddMemberPage
        ele = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
        self.wait_for_click(ele, 10)
        while True:
            self.find(By.CSS_SELECTOR, '.ww_operationBar .js_add_member').click()
            element = self.finds(By.ID, 'username')
            if len(element) > 0:
                break

        return AddMemberPage(self.driver)

    def get_member(self):

        eles = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        name_list = []
        for value in eles:
            name_list.append(value.get_attribute("title"))
        return name_list
