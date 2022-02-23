from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(
    "/Users/jeongjun-yeong/GitHub/golfmacro/Golf/chromedriver")
driver.get("https://www.midasgolf.co.kr/")
driver.implicitly_wait(10)  # seconds


# login정보

# id =
# password =


loginclik = driver.find_element_by_link_text('로그인').click()
IdElem = driver.find_element_by_name("user_id")
PassElem = driver.find_element_by_name("user_pwd")

IdElem.send_keys(id)
PassElem.send_keys(password)

ClearLogin = driver.find_element_by_class_name(
    "btn.btn-primary.btn-lg.btn-block.fw-bold.mt-4").click()

# pop업창 삭제
elempop1 = driver.find_element_by_id(
    "HidePopupLayerButton10").click()
elempop2 = driver.find_element_by_id(
    "HidePopupLayerButton14").click()

# 예약창 클릭 넘어가기
loginclik = driver.find_element_by_link_text('예약').click()
# 예약 캘린더에서 원하는 숫자 클릭
# 마지막 tr안에 숫자로 몇주차, td안에 숫자로 무슨요일 제어 가능.
while(1):
    pick = driver.find_element_by_xpath(
        "/html/body/div[4]/section[3]/div/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/a").click()
    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        driver.refresh()
    except:
        # # table 찾기
        table = driver.find_element_by_xpath(
            "/html/body/div[4]/div/section[2]/div/div/table")

        # # tbody 찾기
        tbody = table.find_element_by_tag_name("tbody")

        # # tbody > tr > td
        rev_num = 1

        for tr in tbody.find_elements_by_tag_name("tr"):
            temp = tr.get_attribute("innerText").split()
            if(temp[1][:2] == "07"):  # 7시면서
                if(int(temp[1][3:]) >= 10):  # 10분 이상이면, 즉 7시 10분이상이면
                    if(temp[3] == "일반캐디"):
                        break
            if(temp[1][:2] == "08"):  # 8시면서
                if(int(temp[1][3:]) <= 50):  # 50분 이하이면, 즉 8시 50분아래 시간대
                    print(temp[1])
                    if(temp[3] == "일반캐디"):
                        break
            rev_num = rev_num + 1

        str_button = "/html/body/div[4]/div/section[2]/div/div/table/tbody/tr[%s]/td[5]/button" % str(
            rev_num)
        finalclick = driver.find_element_by_xpath(str_button).click()

        #lastclick = driver.find_element_by_id("btn-reservation").click()

# # 조건에 맞는 버튼 만들어서 경로 만들고


# # /html/body/div[4]/div/section[2]/div/div/table/tbody/tr[6]/td[5]/button

# # /html/body/div[4]/div/section[2]/div/div/table/tbody/tr[1]/td[5]/button

# # /html/body/div[4]/div/section[2]/div/div/table/tbody/tr[2]/td[5]/button
