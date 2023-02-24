from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


driver = webdriver.Edge()
driver.get('https://infoeasy.cc:8083/qr?id=EizwU%2fVQhPbtMZX7k%2fTV3VtQnv9EVX3E6UD06jytjxweEhclducIHIKdA%2bfmM4JP&orderid=afGbNmqB96c%3d&name=46pXnExyHESvKoNzowd7bUKrWWcBqH%2bnYM%2bMLCY2G5A%3d')
driver.maximize_window()
remark = 'ไม่ใส่อะไรทั้งสิ้น'
time.sleep(3)
# choiceitems  1
firstitems =  driver.find_element(By.XPATH, '//*[@id="menu-82"]/div/div/a[9]')
firstitems.click()
time.sleep(3)
# Click + 1
clickplus = driver.find_element(By.XPATH, '//*[@id="item-modifier"]/div[3]/div[1]/div/div/div[1]').click()
# clickplus.double_Click()
# Comment 1
sendtext = driver.find_element(By.XPATH,'//*[@id="remark"]').send_keys(remark)
# NextPage 1
time.sleep(1)
nextpage = driver.find_element(By.XPATH, '//*[@id="add-choice-btn"]').click()
time.sleep(3)
#---------------------------------------------------------------------
# loop ChooseItems
# choiceitems  2
firstitems =  driver.find_element(By.XPATH, '//*[@id="menu-82"]/div/div/a[5]').click()
time.sleep(3)
# Click +2
clickplus = driver.find_element(By.XPATH, '//*[@id="item-modifier"]/div[3]/div[1]/div/div/div[1]').click()
# Comment 2
sendtext = driver.find_element(By.XPATH,'//*[@id="remark"]').send_keys(remark)
# NextPage 2
nextpage = driver.find_element(By.XPATH, '//*[@id="add-choice-btn"]').click()
time.sleep(1)
# ClickCart
clickcart = driver.find_element(By.XPATH,'//*[@id="cart-btn"]').click()
time.sleep(1)
nextpage_2 = driver.find_element(By.XPATH,'//*[@id="add-cart"]').click()
time.sleep(1)
click_2 = driver.find_element(By.XPATH,'//*[@id="confirm-order-btn"]').click()
time.sleep(15)