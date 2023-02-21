from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
path = os.getcwd()
print(path)

driver = webdriver.Edge(path+"/msedgedriver")
driver.get("https://infoeasy.cc:9015/qr?id=EizwU%2fVQhPbtMZX7k%2fTV3aV1p0RB7nft83tnPZHzIwCimU7mGva0%2bgUHoPkuXDRK&orderid=NvE0s7VJZLI%3d&name=9CfMgg8c6L%2fQjfYdYdnT50K4HDhHiH6zK3sa9Xe0G%2b8%3d")
time.sleep(10)

# choiceitems =
steak =  driver.find_element(By.XPATH, '//*[@id="menu-275"]/div/div/a[2]')
steak.click()
time.sleep(3)
  

time.sleep(15)