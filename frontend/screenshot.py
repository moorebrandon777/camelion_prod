import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .models import MyScreenshots

start_time = time.time()

options = Options()
options.add_argument('--headless')

driver=webdriver.Chrome(options = options)

# the_email = "contact@hmb-online.com"
# email = the_email.split('@')[1]
# url = f"https://{email}"

url = 'https://learnwithhasan.com'
email = 'learnwithhasan.com'

driver.get(url)

driver.save_screenshot(f"frontend/screenshots/{email}.png")
# img = driver.get_screenshot_as_file(f'screenshots/{email}.png')

d_screenshot = f'frontend/screenshots/{email}.png'

# save_screenshot = MyScreenshots.objects.create(name=email, screenshot=d_screenshot)


elapsed = "%s seconds" % (time.time() - start_time)

driver.quit()

print("Done In", elapsed, email)
# print("Done In", elapsed, email, save_screenshot.screenshot.url)