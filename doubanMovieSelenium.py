from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
try:
    browser.get('https://accounts.douban.com/passport/login')
    tab = browser.find_element(By.CLASS_NAME, 'account-tab-account')
    tab.click()
    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')
    username_input.send_keys('18620623279')
    password_input.send_keys('Mr.Txiao')
    btn = browser.find_element(By.CLASS_NAME, 'btn-account')
    btn.click()
    rs = WebDriverWait(browser, 10, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'nav-user-account'))
    )
    browser.get('https://movie.douban.com/subject/26794435/comments?start=220&limit=20&sort=new_score&status=P')
    print(browser.find_element(By.ID, 'content').text)

finally:
    print('suc')
    # 关闭浏览器
    # browser.close()
