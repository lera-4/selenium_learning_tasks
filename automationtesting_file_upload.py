from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
path_to_extension = r'C:\Users\lera-\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.46.2_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.implicitly_wait(5)
more = driver.find_element_by_link_text("More")
more.click()
file_upload = driver.find_element_by_link_text("File Upload")
file_upload.click()
file = ('C:\\Users\\lera-\\PycharmProjects\\pythonProject\\selenium_learning_tasks\\files\\Screenshot_1.png')
upload = driver.find_element_by_id("input-4")
upload.send_keys(file)
remove = driver.find_element_by_xpath("//*[text()='Remove']")
remove.click()
file_new = ('C:\\Users\\lera-\\PycharmProjects\\pythonProject\\selenium_learning_tasks\\files\\1.txt')
upload = driver.find_element_by_id("input-4")
upload.send_keys(file_new)
error = driver.find_element_by_css_selector(".close.kv-error-close")
error.click()
file_upl_btn = driver.find_element_by_css_selector(".btn.btn-default.fileinput-upload.fileinput-upload-button")
file_upl_btn_disabled = file_upl_btn.get_attribute("disabled")
print("value: ", file_upl_btn_disabled)
if file_upl_btn_disabled is not None:
    print("Кнопка загрузки файла отключена")
else:
    print("Кнопка загрузки файла включена")
driver.quit()