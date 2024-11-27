import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://trytestingthis.netlify.app/")
driver.find_element(By.ID, "fname").send_keys("Rifat")
driver.find_element(By.ID, "lname").send_keys("Halim")
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
time.sleep(2)
driver.quit()
