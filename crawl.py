from selenium import webdriver
from selenium.webdriver.support.ui import Select

mapo = []

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

# 1번째 가맹점 크롤링 후 출력
franchisee = driver.find_elements_by_xpath("/html/body/div/form/div[2]/table/tbody/tr[1]/td[1]")

for value in franchisee:
    mapo.append(value.text.split('\n'))

print(mapo[0][0])