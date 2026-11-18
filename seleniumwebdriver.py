from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.find_element(By.ID, "userName").send_keys("Harsha Baiju")
driver.find_element(By.ID, "userEmail").send_keys("harsha@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Thrissur")
driver.find_element(By.ID, "permanentAddress").send_keys("Kerala")
driver.find_element(By.ID, "submit").click()
time.sleep(2)
output = driver.find_element(By.ID, "output")
print(output.text)
driver.quit()