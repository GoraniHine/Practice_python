from selenium import webdriver
from selenium.webdriver.ie.options import Options

# chromedriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('./chromedriver', options=options)

# Load Page
driver.get(url='https://') # url

print(driver.current_url)

driver.close()
