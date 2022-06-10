import time
from selenium import webdriver # импортируем webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
login = driver.find_element_by_css_selector("input[name='txtUsername']") # объявляем переменную login, задаём ей значение селектора поля логин
login.send_keys("Admin") # команда send_keys("значение") – нужна для ввода информации в поле
password = driver.find_element_by_name("txtPassword") # объявляем переменную password, задаём ей значение селектора поля пароль
password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find.... .send_keys(..))
login_btn = driver.find_element_by_css_selector(".button") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
login_btn.click() # команда click() – нужна для нажатия(клика) на элемент
pim = driver.find_element_by_id("menu_pim_viewPimModule")
pim.click()
time.sleep(3)
employeelist = driver.find_element_by_id("menu_pim_viewEmployeeList")
employeelist.click()
time.sleep(3)
card = driver.find_element_by_link_text("Odis")
card.click()
optGender = driver.find_element_by_id("personal_optGender_1")
optGender_disabled = optGender.get_attribute("disabled")
print("value of optGender radio button: ", optGender_disabled)
if optGender_disabled is None:
    print("Атрибута нет")
else:
    print("Атрибут есть")
nationality = driver.find_element_by_id("personal_cmbNation")
nationality_disabled = nationality.get_attribute("disabled")
print("value of nationality selector: ", nationality_disabled)
if nationality_disabled is None:
    print("Атрибута нет")
else:
    print("Атрибут есть")
edit = driver.find_element_by_id("btnSave")
edit.click()
optGender = driver.find_element_by_css_selector('[value="1"]')
optGender.click()
optGender = driver.find_element_by_id("personal_optGender_1")
optGender_checked = optGender.get_attribute("checked")
print("value of optGender approval radio button: ", optGender_checked)
if optGender_checked is not None:
    print("Радио кнопка отмечена")
else:
    print("Радио кнопка НЕ отмечена")
from selenium.webdriver.support.select import Select
nationality = driver.find_element_by_id("personal_cmbNation")
select = Select(nationality)
select.select_by_value("193")
nationality_select_Zimbabwean = nationality.get_attribute("193")
optGender = driver.find_element_by_css_selector('[value="1"]')
optGender.click()
nationality = driver.find_element_by_id("personal_cmbNation")
select = Select(nationality)
select.select_by_value("0")
save = driver.find_element_by_id("btnSave")
time.sleep(3)
save.click()