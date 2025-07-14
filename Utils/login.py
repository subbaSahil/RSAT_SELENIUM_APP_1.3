import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from getCreds import d365_preview_cred
from Utils import Interactions
from selenium.common.exceptions import NoSuchElementException
from Utils.users_credentials import credentials
def d365_login(driver, username, password):
    driver.get("https://dynamicsd365fando.operations.dynamics.com/?cmp=usmf&mi=DefaultDashboard")
    time.sleep(3)
 
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(username + Keys.RETURN)
    time.sleep(3)
 
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password + Keys.RETURN)
    time.sleep(3)
    try:
        error = driver.find_element(By.XPATH, "//div[@id='passwordError']")
        if "incorrect" in error.text.lower():
            Interactions.take_screenshot_on_failure(driver)
            raise AssertionError("❌ Test Failed: Incorrect username or password.")
    except NoSuchElementException:
        pass
 
    try:
        driver.find_element(By.ID, "idSIButton9").click()
    except:
        print("No 'Stay signed in' prompt detected.")
 
 
# def login(driver):
#     secrets = d365_preview_cred()
#     username = secrets["username"]
#     password = secrets["password"]
#     # Login
#     d365_login(driver, username, password)
#     print("Login Successful!")
 
def login(driver, user_key):
    if user_key not in credentials:
        raise ValueError(f"Unknown user key: {user_key}")
    user = credentials[user_key]
    username = user["username"]
    password = user["password"]
    d365_login(driver, username, password)
    print(f"Login Successful as {user_key}")

 