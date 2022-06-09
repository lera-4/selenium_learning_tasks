import time
from selenium import webdriver # импортируем webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
first_name = driver.find_element_by_tag_name("[ng-model= 'FirstName']")
first_name.send_keys("ivan")
last_name = driver.find_element_by_tag_name("[ng-model= 'LastName']")
last_name.send_keys("ivanov")
email = driver.find_element_by_tag_name("[ng-model= 'EmailAdress']")
email.send_keys("ivanov@mail.ru")
phone = driver.find_element_by_tag_name("[ng-model= 'Phone']")
phone.send_keys("1111213456")
option = driver.find_element_by_css_selector("[value='Male']")
option.click()
from selenium.webdriver.support.select import Select
element = driver.find_element_by_id("countries")
select = Select(element)
select.select_by_visible_text("Select Country")
from selenium.webdriver.support.select import Select
element1 = driver.find_element_by_id("yearbox")
select = Select(element1)
select.select_by_visible_text("1980")
from selenium.webdriver.support.select import Select
element1 = driver.find_element_by_tag_name("[ng-model='monthbox']")
select = Select(element1)
select.select_by_visible_text("July")
from selenium.webdriver.support.select import Select
element1 = driver.find_element_by_id("daybox")
select = Select(element1)
select.select_by_visible_text("5")
password = driver.find_element_by_id("firstpassword")
password.send_keys("aB789456123")
confirm_password = driver.find_element_by_id("secondpassword")
confirm_password.send_keys("123456789aB")
file = ('C:\\Users\\lera-\\PycharmProjects\\pythonProject\\selenium_learning_tasks\\files\\Screenshot_1.png')
upload = driver.find_element_by_id("imagesrc")
upload.send_keys(file)
driver.execute_script("window.scrollBy(0, 300);")
submit = driver.find_element_by_id("submitbtn")
submit.click()
time.sleep(3)
driver.quit()




