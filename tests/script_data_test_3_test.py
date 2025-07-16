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
test_data = read_all_test_data("Data\\script_data_test_3_test_data.xlsx","DynamicFields")

@pytest.mark.ui
@pytest.mark.parametrize("data", test_data)
def test(data):
    base = BaseTest("user1",incognito=True)
    driver = base.driver
    actions = base.actions
    recorder=ScreenRecorder()
    
    try:
        recorder.start()
        relation = data['Customer relation/MarkupAutoTable_AccountRelation']
        description = data['Charge description/MarkupAutoTable_MarkupAutoTableDescription']
        charges = data['Charges code/MarkupAutoLine_MarkupCode']
        value = data['Charges value/MarkupAutoLine_Value']
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts receivable
        nav1 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
# Clicking navigation: Charges setup
        nav2 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Charges setup']")
# Clicking navigation: Auto charges
        base.steps_count +=1
        nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Auto charges']")
        time.sleep(3)
        Interactions.assert_navigation(driver,base.steps_count,nav1, nav2, nav3)
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']",base.steps_count, "Click New.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']",base.steps_count,"Click New.")
        base.steps_count +=1
# Inputting into: MarkupAutoTable_AccountRelation
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'MarkupAutoTable_AccountRelation')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Customer relation')]") ):
            #clicking inside grid: MarkupAutoTable_AccountRelation
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'MarkupAutoTable_AccountRelation')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'MarkupAutoTable_AccountRelation')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'MarkupAutoTable_AccountRelation')])[1]", relation,base.steps_count,"In the Customer relation field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer relation')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Customer relation')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Customer relation')])[1]", relation,base.steps_count,"In the Customer relation field, enter or select a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'MarkupAutoTable_AccountRelation')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'MarkupAutoTable_AccountRelation')]", relation,base.steps_count,"In the Customer relation field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer relation')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer relation')]", relation,base.steps_count,"In the Customer relation field, enter or select a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        base.steps_count +=1
#    "Skipping grid selection due input in the ancestor"
        base.steps_count +=1
# Inputting into: MarkupAutoTable_MarkupAutoTableDescription
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'MarkupAutoTable_MarkupAutoTableDescription')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Charge description')]") ):
            #clicking inside grid: MarkupAutoTable_MarkupAutoTableDescription
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'MarkupAutoTable_MarkupAutoTableDescription')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'MarkupAutoTable_MarkupAutoTableDescription')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'MarkupAutoTable_MarkupAutoTableDescription')])[1]", description,base.steps_count,"In the Charge description field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Charge description')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Charge description')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Charge description')])[1]", description,base.steps_count,"In the Charge description field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'MarkupAutoTable_MarkupAutoTableDescription')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'MarkupAutoTable_MarkupAutoTableDescription')]", description,base.steps_count,"In the Charge description field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Charge description')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Charge description')]", description,base.steps_count,"In the Charge description field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        base.steps_count +=1
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']",base.steps_count, "Click Save.")
        base.steps_count +=1
#    "Skipping grid since it is deafault behavior of d365"
        base.steps_count +=1
# Inputting into: MarkupAutoLine_MarkupCode
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'MarkupAutoLine_MarkupCode')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Charges code')]") ):
            #clicking inside grid: MarkupAutoLine_MarkupCode
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'MarkupAutoLine_MarkupCode')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'MarkupAutoLine_MarkupCode')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'MarkupAutoLine_MarkupCode')])[1]", charges,base.steps_count,"In the Charges code field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Charges code')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Charges code')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Charges code')])[1]", charges,base.steps_count,"In the Charges code field, enter or select a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'MarkupAutoLine_MarkupCode')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'MarkupAutoLine_MarkupCode')]", charges,base.steps_count,"In the Charges code field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Charges code')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Charges code')]", charges,base.steps_count,"In the Charges code field, enter or select a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Clicking button: Grid
        user_input = input("Press data to select: ")
        Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']", base.steps_count,"In the list, select row 3.")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
        base.steps_count +=1
#    "Skipping grid selection due input in the ancestor"
        base.steps_count +=1
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'MarkupAutoLine_Value')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Charges value')]") ):
            #clicking inside grid: MarkupAutoLine_Value
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'MarkupAutoLine_Value')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'MarkupAutoLine_Value')])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'MarkupAutoLine_Value')])[1]",value, base.steps_count,"In the Charges value field, enter a number.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Charges value')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Charges value')])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Charges value')])[1]", value, base.steps_count,"In the Charges value field, enter a number.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'MarkupAutoLine_Value')]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'MarkupAutoLine_Value')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'MarkupAutoLine_Value')]", value, base.steps_count,"In the Charges value field, enter a number.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Charges value')]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Charges value')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Charges value')]", value, base.steps_count,"In the Charges value field, enter a number.")
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