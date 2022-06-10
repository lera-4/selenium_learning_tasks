import time
from selenium import webdriver  # импортируем webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/WebTable.html")
switchto = driver.find_element_by_link_text("SwitchTo")
switchto.click()
alerts = driver.find_element_by_link_text("Alerts")
alerts.click()
cl_btn = driver.find_element_by_css_selector(".btn.btn-danger")
time.sleep(3)
cl_btn.click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()
time.sleep(3)
if alert_text is not None:
     print("Содержимое равно тексту I am an alert box!")
else:
     print("Ошибка")
current_url = driver.current_url
print(current_url)
second_tab = driver.execute_script('window.open();')
window_after_first = driver.window_handles[1]
print(window_after_first)
driver.switch_to.window(window_after_first)
driver.get(current_url)
btn = driver.find_element_by_link_text("Alert with OK & Cancel")
time.sleep(3)
btn.click()
cl_btn = driver.find_element_by_css_selector('.btn-primary')
cl_btn.click()
prompt = driver.switch_to.alert
prompt.dismiss()
current_url = driver.current_url
print(current_url)
second_tab = driver.execute_script('window.open();')
window_after_second = driver.window_handles[2]
print(window_after_second)
driver.switch_to.window(window_after_second)
driver.get(current_url)
textbox = driver.find_element_by_link_text("Alert with Textbox")
textbox.click()
box = driver.find_element_by_css_selector(".btn-info")
time.sleep(3)
box.click()
prompt = driver.switch_to.alert
prompt.send_keys("Ура! Задание выполнено!")
prompt.accept()
driver.quit()