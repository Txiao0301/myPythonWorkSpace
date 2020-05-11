from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

# 声明浏览器
browser = webdriver.Chrome()
try:
    # 访问链接
    # browser.get('https://www.baidu.com')
    # # find_element获取单个元素
    # # find_elements获取多个元素
    # # input = browser.find_element_by_id('kw')
    # input = browser.find_element(By.ID, 'kw')
    # # 写入内容到input
    # input.send_keys('Python')
    # # 点击回车键
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))

    browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    # 切换frame
    browser.switch_to.frame('iframeResult')
    source = browser.find_element(By.CSS_SELECTOR, '#draggable')
    target = browser.find_element(By.CSS_SELECTOR, '#droppable')
    action = ActionChains(browser)
    action.drag_and_drop(source, target)
    action.perform()

    # browser.get('http://www.zhihu.com/explore')
    # # browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # # browser.execute_script('alert("To Bottom")')
    # zhihuInput = browser.find_element_by_id('Popover1-toggle')
    # print(zhihuInput.get_attribute('class'))
    # print(zhihuInput.text)
finally:
    # 关闭浏览器
    browser.close()
