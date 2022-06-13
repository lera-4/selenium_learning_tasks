from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
bar = driver.find_element_by_link_text("JQuery ProgressBar")
bar.click()
button = WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, ".ui-dialog-buttonset > button")))
start_download = driver.find_element_by_id("downloadButton")
start_download.click()
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-buttonset"), "Cancel Download"))
close_btn = driver.find_element_by_css_selector(".ui-dialog-buttonset > button")
close_btn.click()
start_download = driver.find_element_by_id("downloadButton")
start_download.click()
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".progress-label"), "Complete!"))
driver.quit()