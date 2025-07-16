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
# Clicking navigation: Procurement and sourcing
        nav1 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Procurement and sourcing']")
# Clicking navigation: Purchase orders
        nav2 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: All purchase orders
        base.steps_count +=1
        nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
        time.sleep(3)
        Interactions.assert_navigation(driver, base.steps_count,nav1, nav2, nav3)
        base.steps_count +=1
# Clicking filter manager: SystemDefinedFilterManager
        column_to_open = "Purchase order"
        open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
        filter_manager_cloumn_last_opened = ''
        for i, div in enumerate(open_divs, start=1):
            class_attr = div.get_attribute('class')
            if 'hasOpenPopup' in class_attr:
                filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[1]")
                break
        if filter_manager_cloumn_last_opened == 'Purchase order' and filter_manager_cloumn_last_opened != '':
            Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order']")
            Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order']", base.steps_count,"Open Purchase order column filter.")
        else:
            Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order']", base.steps_count,"Open Purchase order column filter.")
        base.steps_count +=1
        filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of '00000823' on the 'Purchase order' field using the 'is exactly' filter operator.")
        operator = filter_manager_data['operator']
        new_val = filter_manager_data['value']
        field_name = filter_manager_data['field_name']
        drop_down_item = "//input[contains(@aria-label,'Filter field: "+field_name+",')]/ancestor::div[@class='columnHeader-popup sysPopup']/ancestor::body/child::div[@class='sysPopup flyoutButton-flyOut layout-root-scope']//button//span[text()='"+operator+"']"
        input_field = "//input[contains(@aria-label,'Filter field: "+field_name+",')]"
        apply_button = "//input[contains(@aria-label,'Filter field: "+field_name+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button"
        dropDown_button = "//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: "+field_name+"')]]"
        Interactions.wait_and_click(driver, By.XPATH, dropDown_button)
        Interactions.wait_and_click(driver, By.XPATH, drop_down_item)
        if(Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@class,'popupShadow popupView preview')]")):
            other_element = driver.find_element(By.XPATH, "//div[text()='" + field_name + "']")
            actions.move_to_element(other_element).perform()
        if operator == 'is one of' or operator == 'matches':
            new_val = Interactions.extract_multiple_values(new_val)
            for new_val_value in new_val:
                Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val_value)
                Interactions.wait_and_click(driver, By.XPATH, apply_button)
        elif operator == 'between':
            new_val = Interactions.extract_dates(new_val)
            from_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[1]"
            to_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[2]"
            Interactions.wait_and_send_keys(driver, By.XPATH, from_date_locator, new_val[0])
            Interactions.wait_and_send_keys(driver, By.XPATH, to_date_locator, new_val[1])
        else:
            Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val)
        Interactions.wait_and_click(driver, By.XPATH, apply_button, base.steps_count,"Enter a filter value of '00000823' on the 'Purchase order' field using the 'is exactly' filter operator.")
        base.steps_count +=1
# Clicking button: Grid
        user_input = input("Press data to select: ")
        Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']", base.steps_count,"In the list, click the link in the selected row.")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
        base.steps_count +=1
# Clicking (default) on: PurchOrder
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']",base.steps_count,"On the Action Pane, click Purchase order.")
        base.steps_count +=1
# Clicking (default) on: General
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='General']",base.steps_count,"On the Action Pane, click General.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OrderReferences']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OrderReferences']",base.steps_count,"Click Related orders.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OrderReferences']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OrderReferences']",base.steps_count,"Click Related orders.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Related orders']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Related orders']",base.steps_count,"Click Related orders.")
        else:
            Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
            if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='OrderReferences']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='OrderReferences']",base.steps_count,"Click Related orders.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Related orders']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Related orders']",base.steps_count,"Click Related orders.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OkButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OkButton']",base.steps_count, "Click OK.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']",base.steps_count,"Click OK.")
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