from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def open_page(driver, url):
    driver.get(url)

def click(id,driver):
    get_element_by_ID(id=id, driver=driver).click()
def get_element_by_ID(id, driver):
    return driver.find_element(By.ID, id)

def send_key(id, driver, text):
    element=get_element_by_ID(id=id, driver=driver)
    element.clear()
    element.send_keys(text)



def login(login, password):
    send_key(id="user-name", driver=driver, text=login)
    send_key(id="password", driver=driver, text=password)
    click(id="login-button", driver=driver)


driver = get_driver()
open_page(driver, URL)
login(login=LOGIN, password=PASSWORD)
