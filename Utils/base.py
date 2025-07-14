# base.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from Utils import login
from selenium.webdriver.common.action_chains import ActionChains

class BaseTest:
    def __init__(self, user_key, incognito=True):
        chrome_options = Options()
 
        if incognito:
            chrome_options.add_argument("--incognito")
 
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        time.sleep(3)
        login.login(self.driver,user_key)
        self.actions = ActionChains(self.driver)

        self.filter_manager_column_last_opened = ""
        self.filter_manager_dropdown_item_index = 1
        self.column_to_open = ""
        self.user_input = None
        # self.save_line_items_without_errors = False
        self.test_passed = True
        self.steps_count = 0

    