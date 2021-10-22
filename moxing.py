
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

def get_my_validcode(browser):

    url = browser.find_element_by_xpath('//*[contains(text(),"输入下图中的字符")]/img').get_attribute('src')
    r = requests.get(url)
    with open('img/captcha.png', 'wb') as f:
        f.write(r.content)
    #screenshot_path = os.path.join('img', "screenshot.png")
    #browser.get_screenshot_as_file(screenshot_path)
    #element = browser.find_element_by_class_name('sec_code_img')

    # 自己用PS标志基准线去量（像素模式） 从截图中抠出来验证码的区域
    #captcha_path = os.path.join('img', 'captcha.png')
    #if os.path.exists(captcha_path):
    #    os.remove(captcha_path)
    #img = Image.open(screenshot_path)
    #img = img.crop((753, 1071, 1032, 1153))
    #img.save(captcha_path)
    # sec_code = ocr(img)
    sec_code = recognize('img/captcha.png')
    return sec_code


def register(userName, email, password):
    chromeOptions =  webdriver.ChromeOptions()
    url = 'http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=73021&vkey=17BD03108B60010811CAE5C2CC636000&num=1&time=30&plat=1&re=0&type=0&so=1&ow=1&spl=1&addr=&db=1'
    f = urllib.request.urlopen(url)
    proxy = f.read().decode('utf-8')
    print(proxy)
    chromeOptions.add_argument('--proxy-server=http://'+ proxy)

    c = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe', options = chromeOptions)
    try:
        c.get('https://moxing.name/forum.php?x=770409')
        c.find_element_by_xpath('//*[@id="toptb"]/div/ul/li[2]/a').click()
        c.find_element_by_xpath('//*[@id="fwin_dialog"]/table/tbody/tr[2]/td[2]/p/button[1]/span').click()
        c.find_element_by_xpath('//*[@id="zcmnam"]').send_keys(userName)
        c.find_element_by_xpath('//*[@id="yxbd"]').send_keys(email)
        c.find_element_by_xpath('//*[@id="pwdmim"]').clear()
        c.find_element_by_xpath('//*[@id="pwdmim"]').send_keys(password)
        c.find_element_by_xpath('//*[@id="pwd2mim"]').clear()
        c.find_element_by_xpath('//*[@id="pwd2mim"]').send_keys(password)
        #get_my_validcode(c)
        for i in range(12):
            time.sleep(1)
            print("已经睡眠"+ str(i) +"秒")
        c.find_element_by_xpath('//*[@id="registerformsubmit"]').submit()
        time.sleep(3)
        c.quit()
    except:
        c.quit()





for i in range (999):
    _emailType = ["@gmail.com","@163.com","@hotmail.com"]
    _randomEmail = random.choice(_emailType)
    _range = random.randint(7,10);
    _Number = "0123456789abcdefghijklmnopqrstuvwxyz"
    _randomNumber = "".join(random.choice(_Number) for i in range(_range))
    _email = _randomNumber  + _randomEmail
    print(_email)
    password = "777777SSss!"
    register(_randomNumber, _email, password)


