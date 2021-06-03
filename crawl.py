from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re

# Seoul
URL = "http://dreamtree.shinhancard.com/waf/opendatam"

# 드라이버 로드 후 URL 접속
driver = webdriver.Firefox(executable_path='/home/enmyuel/project/app/geckodriver')
driver.get(URL)

# 지역구 설정 후 검색버튼 클릭
select = Select(driver.find_element_by_id('MNST_DPT_CD'))
select.select_by_visible_text('서울시 마포구')

search_button = driver.find_element_by_class_name("btn_sear")
search_button.click()

#크롤링 후 결과 가다듬고 출력
franchisee = driver.find_elements_by_xpath("/html/body/div/form/div[2]/table/tbody")
mapo = []
for i in franchisee:
    mapo.append(i.text.split('\n'))
for i in mapo:
    for j in range(len(i)):
        if j % 3 == 1:
            y = re.findall(" \d.*", mapo[0][j])
            if len(y) != 0:
                mapo[0][j] = y[0].lstrip()
            else:
                del mapo[0][-1]

dat = []
for i in mapo:
    for j in range(len(i)):
        if j % 3 != 2:
            k = mapo[0][j].find(".")
            temp = mapo[0][j]
            temp = temp[k+1:]
            dat.append(temp)

driver.close()

file = open("data.txt", 'w')
for i in dat:
    file.write(i + "\n")
file.close()
