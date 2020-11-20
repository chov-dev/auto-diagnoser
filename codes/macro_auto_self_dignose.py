import time
import configparser
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

config = configparser.ConfigParser()

configName = "selfDiagnose"

config.read('자가진단설정파일(삭제 시 문제 발생).ini', encoding='CP949')

userName = config['DEFAULT']['userName']
birthDate = config['DEFAULT']['birthDate']
area = config['DEFAULT']['area']
school = config['DEFAULT']['school']
schoolType = config['DEFAULT']['schoolType']
password = config['DEFAULT']['password']

areaDic = {
    "서울특별시": "2",
    "부산광역시": "3",
    "대구광역시": "4",
    "인천광역시": "5",
    "광주광역시": "6",
    "대전광역시": "7",
    "울상광역시": "8",
    "세종특별자치시": "9",
    "경기도": "10",
    "강원도": "11",
    "충청북도": "12",
    "충청남도": "13",
    "전라북도": "14",
    "전라남도": "15",
    "경상북도": "16",
    "경상남도": "17",
    "제주특별자치도": "18"
}

schoolTypeDic = {
    "유치원": "2",
    "초등학교": "3",
    "중학교": "4",
    "고등학교": "5",
    "특수학교": "6"
}

dv = webdriver.Chrome("chromedriver.exe")
dv.get("https://hcs.eduro.go.kr/#/relogin")

elem = dv.find_element_by_id("btnConfirm2")
elem.send_keys(Keys.RETURN)

elem = dv.find_element_by_class_name("searchBtn")
elem.send_keys(Keys.RETURN)

dv.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[%s]' % areaDic[area]).click()

dv.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[%s]' % schoolTypeDic[schoolType]).click()


dv.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input').send_keys(school)

elem = dv.find_element_by_class_name("searchBtn")
elem.send_keys(Keys.RETURN)

dv.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button/span').click()

dv.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p/a/em').click()

dv.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

dv.find_element_by_xpath(
    '//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input').send_keys(userName)

dv.find_element_by_xpath(
    '//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input').send_keys(birthDate)

dv.find_element_by_xpath(
    '//*[@id="btnConfirm"]').click()

time.sleep(1)

dv.find_element_by_xpath(
    '//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys(password)

dv.find_element_by_xpath(
    '//*[@id="btnConfirm"]').click()


time.sleep(1)

dv.find_element_by_xpath(
    '//*[@id="container"]/div/section[2]/div[2]/ul/li[1]/a/span[1]').click()


time.sleep(1)

dv.find_element_by_xpath(
    '//*[@id="container"]/div/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label').click()

time.sleep(0.1)

dv.find_element_by_xpath(
    '//*[@id="container"]/div/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label').click()

time.sleep(0.1)

dv.find_element_by_xpath(
    '//*[@id="container"]/div/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label').click()

time.sleep(0.1)

dv.find_element_by_xpath(
    '//*[@id="btnConfirm"]').click()
dv.quit()
sys.exit()
