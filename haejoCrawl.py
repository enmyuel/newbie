from selenium import webdriver
import sys
import time

# scrapes result of searching haejo from maplestory gallery 1-2.
# this program doesn't treat strings.

sys.stdout = open('output.txt', 'w')
driver = webdriver.Firefox(executable_path="C:\\Users\\RealFirix\\Desktop\\project\\gecko\\geckodriver.exe")
driver.get("https://gall.dcinside.com/board/lists/?id=maplestory&page=1&search_pos=&s_type=search_all&s_keyword=%ED%95%B4%EC%A1%B0")   

test = driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/section[1]/article[2]/div[3]/table/tbody')
print(test.text)

time.sleep(3) # to avoid IP address ban

driver.get("https://gall.dcinside.com/board/lists/?id=maplestory&page=2&search_pos=&s_type=search_all&s_keyword=%ED%95%B4%EC%A1%B0")   
test = driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/section[1]/article[2]/div[3]/table/tbody')
print(test.text)