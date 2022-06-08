
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")
login = driver.find_element_by_name("user-name")
login.send_keys("standard_user")
password = driver.find_element_by_name("password")
password.send_keys("secret_sauce")
login_btn = driver.find_element_by_name("login-button")
login_btn.click()
product1 = driver.find_element_by_name("add-to-cart-sauce-labs-backpack")
product1.click()
product2 = driver.find_element_by_name("add-to-cart-sauce-labs-bike-light")
product2.click()
product3 = driver.find_element_by_name("add-to-cart-sauce-labs-bolt-t-shirt")
product3.click()
time.sleep(3)
basket = driver.find_element_by_class_name('shopping_cart_link')
basket.click()
time.sleep(3)
items_count = driver.find_elements_by_class_name ('cart_item')
if len(items_count) == 3:
    print('В корзине 3 товара')
else:
    print ("Ошибка. Количество товаров в корзине:" + str(len(items_count)))
driver.quit()