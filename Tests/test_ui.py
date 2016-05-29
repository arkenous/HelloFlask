#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from nose.tools import eq_


def test_access():
    driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
    wait = WebDriverWait(driver, 5)

    driver.get('http://127.0.0.1:8080/')
    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/login', driver.current_url)
    driver.close()


def test_fail_login():
    driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
    wait = WebDriverWait(driver, 5)

    driver.get('http://127.0.0.1:8080/')
    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/login', driver.current_url)

    show_signin = driver.find_element_by_id('showSignIn')
    show_signin.click()

    wait.until(ec.visibility_of_element_located((By.ID, 'username')))
    username = driver.find_element_by_id('username')
    username.send_keys('test')

    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    password = driver.find_element_by_id('password')
    password.send_keys('test')

    wait.until(ec.visibility_of_element_located((By.ID, 'signIn')))
    signin = driver.find_element_by_id('signIn')
    signin.click()

    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/login', driver.current_url)
    driver.close()


def test_success_login():
    driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
    wait = WebDriverWait(driver, 5)

    driver.get('http://127.0.0.1:8080/')
    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/login', driver.current_url)

    show_signin = driver.find_element_by_id('showSignIn')
    show_signin.click()

    wait.until(ec.visibility_of_element_located((By.ID, 'username')))
    username = driver.find_element_by_id('username')
    username.send_keys('admin')

    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    password = driver.find_element_by_id('password')
    password.send_keys('test')

    wait.until(ec.visibility_of_element_located((By.ID, 'signIn')))
    signin = driver.find_element_by_id('signIn')
    signin.click()

    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/', driver.current_url)

    logout = driver.find_element_by_id('logout')
    logout.click()

    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/login', driver.current_url)
    driver.close()


def test_lower_conversion():
    driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
    wait = WebDriverWait(driver, 5)

    driver.get('http://127.0.0.1:8080/')
    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/login', driver.current_url)

    show_signin = driver.find_element_by_id('showSignIn')
    show_signin.click()

    wait.until(ec.visibility_of_element_located((By.ID, 'username')))
    username = driver.find_element_by_id('username')
    username.send_keys('admin')

    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    password = driver.find_element_by_id('password')
    password.send_keys('test')

    wait.until(ec.visibility_of_element_located((By.ID, 'signIn')))
    signin = driver.find_element_by_id('signIn')
    signin.click()

    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/', driver.current_url)

    input_text = driver.find_element_by_id('input-text')
    input_text.send_keys('TEST')

    change_text = driver.find_element_by_id('button')
    change_text.click()

    wait.until(ec.presence_of_all_elements_located)
    hello = driver.find_element_by_id('hello')
    eq_('test', hello.text)

    logout = driver.find_element_by_id('logout')
    logout.click()

    wait.until(ec.presence_of_all_elements_located)
    eq_('http://127.0.0.1:8080/login', driver.current_url)
    driver.close()
