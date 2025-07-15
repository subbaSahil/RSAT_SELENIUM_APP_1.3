import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.base import BaseTest
from selenium.webdriver.common.by import By
from Utils import Interactions
from Utils.screenRecorder import ScreenRecorder
import time
from Utils.getExcelData import read_all_test_data
test_data = read_all_test_data("Data\\script_data_test_1_test_data.xlsx","DynamicFields")

# test_data = 
@pytest.mark.ui
@pytest.mark.parametrize("data", test_data)
def test(data):
    base = BaseTest("user1",incognito=True)
    driver = base.driver
    actions = base.actions
    recorder=ScreenRecorder()
    try:
        recorder.start()
        dimension = data['Dimension value/GroupValue']
        description = data['Description/GroupDescription']
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: General ledger
        nav1 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='General ledger']")
# Clicking navigation: Chart of accounts
        nav2 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Chart of accounts']")
# Clicking navigation: Dimensions
        nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Dimensions']")
# Clicking navigation: Financial dimensions
        base.steps_count +=1
        nav4 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Financial dimensions']")
        time.sleep(3)
        Interactions.assert_navigation(driver,base.steps_count,nav1, "123", nav3, nav4)
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Close']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Close']",base.steps_count, "Click Close.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Close']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Close']",base.steps_count,"Click Close.")
# Inputting into: QuickFilter
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilter')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilter')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "cargo",base.steps_count,"Use the Quick Filter to find records. For example, filter on the Dimension name field with a value of 'cargo'.")
            Interactions.press_enter(driver, By.XPATH, locator)
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "cargo",base.steps_count,"Use the Quick Filter to find records. For example, filter on the Dimension name field with a value of 'cargo'.")
            Interactions.press_enter(driver, By.XPATH, locator)
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='DimensionValueDetails']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='DimensionValueDetails']",base.steps_count,"Click Dimension values.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='DimensionValueDetails']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='DimensionValueDetails']",base.steps_count,"Click Dimension values.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Dimension values']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Dimension values']",base.steps_count,"Click Dimension values.")
        else:
            Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
            if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='DimensionValueDetails']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='DimensionValueDetails']",base.steps_count,"Click Dimension values.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Dimension values']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Dimension values']",base.steps_count,"Click Dimension values.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']",base.steps_count, "Click New.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']",base.steps_count,"Click New.")
        base.steps_count +=1
# Inputting into: GroupValue
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'GroupValue')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Dimension value')]") ):
            #clicking inside grid: GroupValue
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'GroupValue')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'GroupValue')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'GroupValue')])[1]", dimension,base.steps_count,"In the Dimension value field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Dimension value')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Dimension value')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Dimension value')])[1]", dimension,base.steps_count,"In the Dimension value field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GroupValue')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'GroupValue')]", dimension,base.steps_count,"In the Dimension value field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Dimension value')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Dimension value')]", dimension,base.steps_count,"In the Dimension value field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: GroupDescription
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'GroupDescription')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Description')]") ):
            #clicking inside grid: GroupDescription
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'GroupDescription')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'GroupDescription')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'GroupDescription')])[1]", description,base.steps_count,"In the Description field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Description')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]", description,base.steps_count,"In the Description field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GroupDescription')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'GroupDescription')]", description,base.steps_count,"In the Description field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Description')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Description')]", description,base.steps_count,"In the Description field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        base.steps_count +=1
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']",base.steps_count, "Click Save.")
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