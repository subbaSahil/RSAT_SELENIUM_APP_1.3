import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.base import BaseTest
from selenium.webdriver.common.by import By
from Utils import Interactions
from Utils.screenRecorder import ScreenRecorder
import time
@pytest.mark.ui
def test():
    base = BaseTest("user1",incognito=True)
    driver = base.driver
    actions = base.actions
    recorder=ScreenRecorder()
    try:
        recorder.start()
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Product information management
        nav1 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Product information management']")
# Clicking navigation: Products
        nav2 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Products']")
# Clicking navigation: All products and product masters
        base.steps_count +=1
        nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='All products and product masters']")
        time.sleep(3)
        Interactions.assert_navigation(driver, base.steps_count, nav1, nav2, nav3)
# Inputting into: QuickFilterControl
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "0007",base.steps_count,"Use the Quick Filter to find records. For example, filter on the Product number field with a value of '0007'.")
            Interactions.press_enter(driver, By.XPATH, locator)
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "0007",base.steps_count,"Use the Quick Filter to find records. For example, filter on the Product number field with a value of '0007'.")
            Interactions.press_enter(driver, By.XPATH, locator)
        base.steps_count += 1
        Interactions.log_interaction(base.steps_count, "Validate that Product number for :  '", "validate Product number", "", "invalid")
        print("Validation step logged for: Product number")
        assert(False, "Validation failed for Product number: expected ")
        base.steps_count +=1
# Clicking button: ListPageGrid
        if Interactions.check_element_exist(driver, By.XPATH, f"//input[@value='0007']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']"):
             Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='0007']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']", base.steps_count,"In the list, click the link in the selected row.")
        else:
             Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='0007']", base.steps_count,"In the list, click the link in the selected row.")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='0007']")
        base.steps_count += 1
        Interactions.log_interaction(base.steps_count, "Validate that Title for :  '", "validate Title", "", "invalid")
        print("Validation step logged for: Title")
        assert(False, "Validation failed for Title: expected ")
# Closing the page
        base.steps_count +=1
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']", base.steps_count)
        time.sleep(1)
# Closing the page
        base.steps_count +=1
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']", base.steps_count)
        time.sleep(1)
        assert True
    except Exception as e:
        base.test_passed = False
        raise e
    finally:
        Interactions.log_interaction(" ", " ", " "," ")
        if base.test_passed:
            print("✅ Test case passed")
            Interactions.take_screenshot_on_pass(driver)
            recorder.stop_and_save()
        else:
            print("❌ Test case failed")
            Interactions.take_screenshot_on_failure(driver)
            recorder.stop_and_discard()
        driver.quit()