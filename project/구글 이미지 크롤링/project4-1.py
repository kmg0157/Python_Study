from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(ChromeDriverManager().install())

URL='https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)

elem=driver.find_element_by_css_selector( "#sbtc > div > div.a4bIc > input " )
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)