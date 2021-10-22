import urllib.request
import urllib.parse
from selenium import webdriver
import random
from PIL import Image
import time
import os
from aip import AipOcr
from utils import get_bin_table, get_threshold, cut_noise
import traceback
from validcode_processor.splitter import split
from utils import deserialize
import cv2
import numpy as np
import requests
import json
import logging
from crawler_mobile import recognize
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def play():
    chromeOptions =  webdriver.ChromeOptions()
    #url = 'http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=73021&vkey=17BD03108B60010811CAE5C2CC636000&num=1&time=30&plat=1&re=0&type=0&so=1&ow=1&spl=1&addr=&db=1'
    #f = urllib.request.urlopen(url)
    #proxy = f.read().decode('utf-8')
    #print(proxy)
    #chromeOptions.add_argument('--proxy-server=http://'+ proxy)

    c = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe', options = chromeOptions)
    try:
        #登录
        c.get('https://splinterlands.com/')
        c.find_element_by_xpath('//*[@id="log_in_button"]/button').click()
        time.sleep(3)
        c.find_element_by_xpath('//*[@id="email"]').send_keys('2013wangyiheng@gmail.com')
        c.find_element_by_xpath('//*[@id="password"]').send_keys('8311876usm')
        c.find_element_by_xpath('//*[@id="login_dialog_v2"]/div/div/div[2]/div/div[2]/form[2]/div[3]/div/button').click()
-0        dialogClose = WebDriverWait(c, 600, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dialog_container"]/div/div/div/div[1]/button'))
        )
        c.find_element_by_xpath('//*[@id="dialog_container"]/div/div/div/div[1]/button').click()
        #play
        time.sleep(3)
        c.find_element_by_xpath('//*[@id="play_now"]/div/div/div/div/button').click()
        c.find_element_by_xpath('//*[@id="battle_category_btn"]').click()
        #wait for ready
        time.sleep(3)
        readyForBtl = WebDriverWait(c, 600, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dialog_container"]/div/div/div/div[2]/div[3]/div[2]/button'))
        )
        while(1>0):
            c.find_element_by_xpath('//*[@id="dialog_container"]/div/div/div/div[2]/div[3]/div[2]/button').click()
            time.sleep(3)
            point = c.find_element_by_xpath('//*[@id="page_container"]/div/div[2]/div/div[3]/div/div/div').text
            battle(c, point);
            battleBtn = WebDriverWait(c, 600, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="btnRumble"]'))
            )
            battleBtn.click()
            c.find_element_by_xpath('//*[@id="btnSkip"]').click()
    except:
        print("there is an error")

def battle(webdriver, point):
    deathPhySum3 = webdriver.find_element_by_xpath('//*[@id="starter-49-wJK45"]/img')

    deathPhySum3.click()

    time.sleep(5)
    deathFront5 = webdriver.find_element_by_xpath('//*[@id="starter-50-DK1sk"]/img')

    deathRange4 = webdriver.find_element_by_xpath('//*[@id="starter-51-snvKq"]/img')

    deathBack3 = webdriver.find_element_by_xpath('//*[@id="starter-47-TXTRq"]/img')

    death1 = webdriver.find_element_by_xpath('//*[@id="starter-136-aghzF"]/img')

    death2 = webdriver.find_element_by_xpath('//*[@id="starter-52-XBxWG"]/img')

    range6 =  webdriver.find_element_by_xpath('//*[@id="starter-47-TXTRq"]/img')

    deathRange3 = webdriver.find_element_by_xpath('//*[@id="starter-46-r7LrT"]/img')

    range4 = webdriver.find_element_by_xpath('//*[@id="starter-63-BOc5d"]/img')

    range5 = webdriver.find_element_by_xpath('//*[@id="starter-195-MmFIY"]/img')

    deathFront7 = webdriver.find_element_by_xpath('//*[@id="starter-140-fTVpN"]/img')

    range6_2 = webdriver.find_element_by_xpath('//*[@id="starter-65-34p5p"]/img')

    front8 = webdriver.find_element_by_xpath('//*[@id="starter-190-8nVnu"]/img')

    if point == '12': #9
        deathFront5.click()
        deathRange4.click()
    if point == '13': #10
        deathFront5.click()
        deathRange4.click()
        death1.click()
    if point == '14': #11
        deathFront5.click()
        deathRange4.click()
        death2.click()
    if point == '15': #12
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
    if point == '16': #13
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        death1.click()
    if point == '17': #14
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        death2.click()
    if point == '18': #15
        deathFront5.click()
        deathRange4.click()
        range6.click()
    if point == '19': #16
        deathFront5.click()
        deathRange4.click()
        range6.click()
        death1.click()
    if point == '20': #17
        deathFront5.click()
        deathRange4.click()
        range6.click()
        death2.click()
    if point == '21':  #18
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range6.click()
    if point == '22': #19
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range6.click()
        death1.click()
    if point == '23': #20
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range6.click()
        death2.click()
    if point == '24': #21
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range6.click()
        deathRange3.click()
    if point == '25': #22
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range6.click()
        range4.click()
    if point == '26': #23
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range5.click()
        range6.click()
    if point == '27': #24
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range5.click()
        range6.click()
        death1.click()
    if point == '28': #25
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range5.click()
        range6.click()
        death2.click()
    if point == '29': #26
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range5.click()
        range6.click()
        deathRange3.click()
    if point == '30': #27
        deathFront5.click()
        deathRange4.click()
        deathBack3.click()
        range5.click()
        range6.click()
        range4.click()
    if point == '99': #99
        deathFront7.click()
        range6.click()
        range6_2.click()
        range5.click()
        deathRange4.click()
        front8.click()
    webdriver.find_element_by_xpath('//*[@id="page_container"]/div/div[1]/div/button').click()

play();