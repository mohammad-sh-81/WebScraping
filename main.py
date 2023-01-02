from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import random
import os
import time
import requests
from http import cookies
import cookies
from selenium.webdriver.support import expected_conditions as EC

username = input('Please enter your user name \n')
password = input('Please enter your password \n')
hashtag = input('Please enter the hashtag you want to follow people from \n')
count = int(input('Please enter how many time you want to follow people \n'))


driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://www.instagram.com/')
driver.add_cookie({'name': 'csrftoken', 'value': 'sxFK8WsW9AQGPS92kn8RJFMxzfAxiMLq',
                  'domain': '.instagram.com', 'path': '/'})
driver.add_cookie({'name': 'rur', 'value': 'LDC\05457135012384\0541702845740:01f7991c0502304ab0d71033d3b21add768122ba676f19841369da00a06983f662c488a0',
                  'domain': '.instagram.com', 'path': '/'})
driver.add_cookie({'name': 'sessionid', 'value': '57135012384%3ADj7rmyhigCex10%3A5%3AAYeNUNGS5Uitiz3XqvXjg-vZje2MXyJP_RF1SPWOhw',
                  'domain': '.instagram.com', 'path': '/'})
driver.add_cookie({'name': 'datr', 'value': 'fkSTY0MYQ71jEBvJtzD0PiQY',
                  'domain': '.instagram.com', 'path': '/'})
driver.add_cookie({'name': 'ds_user_id', 'value': '57135012384',
                  'domain': '.instagram.com', 'path': '/'})
driver.add_cookie({'name': 'ig_did', 'value': '87AECBA5-45E0-4BFD-AA74-8C8A196FD6CC',
                  'domain': '.instagram.com', 'value': '/'})
driver.add_cookie({'name': 'ig_nrcb', 'value': '1',
                  'domain': '.instagram.com', 'path': '/'})
driver.add_cookie({'name': 'mid', 'value': 'Y5NEfwALAAGVK2gYQbbpvIW3Da6I',
                  'domain': '.instagram.com', 'path': '/'})
driver.add_cookie({'name': 'dpr', 'value': '1.25',
                  'domain': '.instagram.com', 'path': '/'})

time.sleep(10)

enter_username = driver.find_element(
    by=By.CSS_SELECTOR, value="#loginForm > div > div:nth-child(1) > div > label > input")
enter_username.send_keys(username)


enter_password = driver.find_element(
    by=By.CSS_SELECTOR, value='#loginForm > div > div:nth-child(2) > div > label > input')
enter_password.send_keys(password)

time.sleep(2)
click_login = driver.find_element(
    by=By.CSS_SELECTOR, value='#loginForm > div > div:nth-of-type(3) > button[type="submit"]')
click_login.click()

time.sleep(10)

Turn_off_save = driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
Turn_off_save.click()

time.sleep(10)

time.sleep(10)

Turn_off_notifes = driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
Turn_off_notifes.click()

time.sleep(10)

driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
time.sleep(15)
i = 0
while i < count:
    x=5
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(10)

    post = driver.find_element(
        by=By.CSS_SELECTOR, value= '#body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > main:nth-child(2) > article:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
                                    #mount_0_0_rW > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > article > div:nth-child(3) > div > div:nth-child(5) > div:nth-child(2) > a > div._aagu > div._aagw
    time.sleep(15)
    post.click()
    time.sleep(30)
    text_follow = driver.find_element(
        by=By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button')
    text=text_follow.text
    if text=="Follow":
        text_follow.click()
        time.sleep(10)
        exit_post=driver.find_element(by=By().XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div')
        exit_post.click()
        count +=1
        
    else:
        exit_post=driver.find_element(by=By().XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div')
        exit_post.click()
    x+=4

time.sleep(300)
