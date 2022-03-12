from selenium import webdriver
import time

# driver = webdriver.Chrome("./chromedriver/chromedriver.exe")
# driver.get('https://nid.naver.com/nidlogin.login')

# id = 'cornchip9250'
# pw = 'sandbox1132'

# driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
# time.sleep(5)
# driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
# time.sleep(5)
# driver.find_element_by_xpath('//+[@id="frmNidLogin"]/fieldset/input').click()
# time.sleep(5)

# driver.close()

driver = webdriver.Chrome("./chromedriver/chromedriver.exe")
driver.get("https://www.opinet.co.kr/searRgSelect.do")
driver.get("https://www.opinet.co.kr/searRgSelect.do")
# 두번 해야지 잘 됨 ??

gu_list_raw = driver.find_elements_by_xpath("""//*[@id="SIGUNGU_NM0"]""")
gu_list = gu_list_raw.find_elements_by_tag_name('option')
# gu_list_raw = driver.find_element(by=By.XPATH, value="""//*[@id="SIGUNGU_NM0"]""")

gu_names = [option.get_attribute("value") for option in gu_list]
gu_names.remove('')
gu_names

element = driver.find_elements_by_id('SIGUNGU_NMO')
element.send_keys(gu_names[0])

xpath = """//*[@id="SIGUNGU_NM0"]"""
element_sel_gu = driver.find_elements_by_xpath(xpath).click()
