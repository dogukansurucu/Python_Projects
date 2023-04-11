# Bu kodda Selenium bot konusunu ele aldım.
# Webdriver metodlarını kullanarak github hesabımla ile etkileşimde bulundum.

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)
print(driver.get_window_size())


time.sleep(2)


driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")


url = "https://github.com/dogukansurucu"
driver.get(url)

print(driver.title)
print(driver.current_url)
driver.refresh()


if "dogukansurucu" in driver.title:
    driver.save_screenshot("github-dogukansurucu.png")


url_2 = "https://github.com/dogukansurucu"
driver.get(url_2)

time.sleep(4)

driver.close()