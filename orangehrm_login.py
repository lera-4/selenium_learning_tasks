
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/")
login = driver.find_element_by_xpath("//input[@id='txtUsername']")
login.send_keys("Admin")
password = driver.find_element_by_xpath("//input[@id='txtPassword']")
password.send_keys("admin123")
login_btn = driver.find_element_by_css_selector(".button")
login_btn.click()
driver.quit()