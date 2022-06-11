from selenium import webdriver
import time
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
path_to_extension = r'C:\Users\lera-\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.46.2_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://demo.automationtesting.in/WebTable.html")
more = driver.find_element_by_link_text("More")
more.click()
loader = driver.find_element_by_link_text("Loader")
loader.click()

some_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".btn.btn-primary"), "Run"))

run = driver.find_element_by_id("loader")
run.click()
lorem_text = WebDriverWait(driver, 40).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".modal-body>p"), 'Lorem'))
print('Lorem найден' if lorem_text else "Lorem не найден")
save_changes_btn = WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".modal-footer > .btn.btn-primary"), "Save changes"))
print('Save changes найдена' if save_changes_btn else "Save changes не найдена")
save_changes_btn = driver.find_element_by_css_selector(".modal-footer > .btn.btn-primary")
save_changes_btn.click()
driver.quit()