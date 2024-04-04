import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth

from django.conf import settings


def get_my_screenshot(url):
    email_name = url
    f_email = url.replace("https://","")
    # email_name = url.split('@')[1]
    # email_name = url.replace("https://","")

    # setting up selenium
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--headless")

    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    
    driver = webdriver.Chrome(options=chrome_options)

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    # getting the url
    
    driver.get(email_name)

    # determine the size of screen
    driver.set_window_size(1920, 1080)

    # getting the location to save image
    static_dir = os.path.join(settings.BASE_DIR, "screenshots", "frontend")
    os.makedirs(static_dir, exist_ok=True)
    screenshot_path = os.path.join(static_dir, f'{f_email}.png')
    try:
        # taking the screenshot
        driver.save_screenshot(screenshot_path)
    except:
        pass
    finally:
        driver.quit()

    return screenshot_path