from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\\Automation\\drivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="F:\\Automation\\drivers\\geckodriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.youtube.com")
driver.find_element_by_name("search_query").send_keys("Automation in python")
driver.find_element_by_id("search-icon-legacy").click()
