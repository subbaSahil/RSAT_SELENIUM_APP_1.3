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
        base.steps_count +=1
# Inputting into: Identification_DisplayProductNumber
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Identification_DisplayProductNumber')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Product number')]") ):
            #clicking inside grid: Identification_DisplayProductNumber
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Identification_DisplayProductNumber')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Identification_DisplayProductNumber')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Identification_DisplayProductNumber')])[1]", "",base.steps_count,"Validate that the value for Product number is '0007'.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Product number')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Product number')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Product number')])[1]", "",base.steps_count,"Validate that the value for Product number is '0007'.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Identification_DisplayProductNumber')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Identification_DisplayProductNumber')]", "",base.steps_count,"Validate that the value for Product number is '0007'.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Product number')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Product number')]", "",base.steps_count,"Validate that the value for Product number is '0007'.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Clicking button: ListPageGrid
        user_input = input("Press data to select: ")
        Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']", base.steps_count,"In the list, click the link in the selected row.")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
        base.steps_count += 1
        base.steps_count +=1
# Inputting into: StringTitle
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'StringTitle')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Title')]") ):
            #clicking inside grid: StringTitle
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'StringTitle')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'StringTitle')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'StringTitle')])[1]", "",base.steps_count,"Validate that the value for Title is '0007 : Full Finger BMX Gloves'.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Title')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Title')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Title')])[1]", "",base.steps_count,"Validate that the value for Title is '0007 : Full Finger BMX Gloves'.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'StringTitle')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'StringTitle')]", "",base.steps_count,"Validate that the value for Title is '0007 : Full Finger BMX Gloves'.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Title')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Title')]", "",base.steps_count,"Validate that the value for Title is '0007 : Full Finger BMX Gloves'.")
        Interactions.press_enter(driver, By.XPATH, "//body")
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