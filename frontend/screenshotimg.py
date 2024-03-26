from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def screenshot_img(email):
    options = Options()
    options.add_argument('--headless')

    driver=webdriver.Chrome(options = options)

    email = email.split('@')[1]

    url = f"https://{email}"

    driver.get(url)
    # driver.save_screenshot(f"{url2}.png")
    driver.get_screenshot_as_file(f'screenshots/{email}.png')

    driver.quit()

    return url
 # Take a screenshot of the entire webpage and save it to a file
    