#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest
from selenium_po.page.main_page import MainPage


class TestLogin:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize('name,id,phone', [('黄五', 'huangwu', '13511223155')])
    def test_contactaddmember(self, name, id, phone):
        namelist = self.main.goto_contact_page().click_add_member(). \
            add_member(name, id, phone).get_member()
        print(namelist)
        assert name in namelist

    @pytest.mark.parametrize('name,id,phone', [('黄七', 'huangqi', '13511223177')])
    def test_mainaddmember(self, name, id, phone):
        sleep(5)
        namelist = self.main.goto_add_member_page().add_member(name, id, phone).get_member()
        print(namelist)
        assert name in namelist
