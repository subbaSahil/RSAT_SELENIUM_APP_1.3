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
        nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
        time.sleep(3)
        base.steps_count +=1
        Interactions.assert_navigation(driver, base.steps_count, nav1, nav2, nav3)
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']",base.steps_count, "Click New.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']",base.steps_count,"Click New.")
        else:
            Interactions.fail_test_case(base.steps_count,"Click New.","Click")
        base.steps_count +=1
# Inputting into: PurchTable_OrderAccount
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]") ):
            #clicking inside grid: PurchTable_OrderAccount
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_OrderAccount')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]", "JMFE-33317",base.steps_count,"In the Vendor account field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Vendor account')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]", "JMFE-33317",base.steps_count,"In the Vendor account field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Vendor account field, type a value.","Send Keys")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "JMFE-33317",base.steps_count,"In the Vendor account field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "JMFE-33317",base.steps_count,"In the Vendor account field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Vendor account field, type a value.","Send Keys")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Yes']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Yes']",base.steps_count, "Click Yes.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']",base.steps_count,"Click Yes.")
        else:
            Interactions.fail_test_case(base.steps_count,"Click Yes.","Click")
        base.steps_count +=1
# Inputting into: PurchTable_AVAOrderType
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_AVAOrderType')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Order type')]") ):
            #clicking inside grid: PurchTable_AVAOrderType
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_AVAOrderType')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_AVAOrderType')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_AVAOrderType')])[1]", "STCKPO",base.steps_count,"In the Order type field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Order type')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Order type')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Order type')])[1]", "STCKPO",base.steps_count,"In the Order type field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Order type field, type a value.","Send Keys")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_AVAOrderType')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_AVAOrderType')]", "STCKPO",base.steps_count,"In the Order type field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Order type')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Order type')]", "STCKPO",base.steps_count,"In the Order type field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Order type field, type a value.","Send Keys")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: PurchTable_InventSiteId
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventSiteId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
            #clicking inside grid: PurchTable_InventSiteId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventSiteId')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_InventSiteId')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventSiteId')])[1]", "JAXPDC",base.steps_count,"In the Site field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Site')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "JAXPDC",base.steps_count,"In the Site field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Site field, type a value.","Send Keys")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventSiteId')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventSiteId')]", "JAXPDC",base.steps_count,"In the Site field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "JAXPDC",base.steps_count,"In the Site field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Site field, type a value.","Send Keys")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: PurchTable_InventLocationId
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
            #clicking inside grid: PurchTable_InventLocationId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventLocationId')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_InventLocationId')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventLocationId')])[1]", "JAXPDC",base.steps_count,"In the Warehouse field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Warehouse')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]", "JAXPDC",base.steps_count,"In the Warehouse field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Warehouse field, type a value.","Send Keys")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]", "JAXPDC",base.steps_count,"In the Warehouse field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "JAXPDC",base.steps_count,"In the Warehouse field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Warehouse field, type a value.","Send Keys")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']",base.steps_count, "Click OK.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']",base.steps_count,"Click OK.")
        else:
            Interactions.fail_test_case(base.steps_count,"Click OK.","Click")
        base.steps_count +=1
# Clicking (default) on: Purchase
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Purchase']",base.steps_count,"On the Action Pane, click Purchase.")
#    "Skipping grid since it is deafault behavior of d365"
        base.steps_count +=1
# Inputting into: PurchLine_ItemId
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
            #clicking inside grid: PurchLine_ItemId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_ItemId')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]", "PT9083023120",base.steps_count,"In the Item number field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "PT9083023120",base.steps_count,"In the Item number field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Item number field, type a value.","Send Keys")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "PT9083023120",base.steps_count,"In the Item number field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "PT9083023120",base.steps_count,"In the Item number field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Item number field, type a value.","Send Keys")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]") ):
            #clicking inside grid: PurchLine_PurchQtyGrid
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]", "5.00", base.steps_count,"In the Quantity field, enter a number.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Quantity')])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])[1]", "5.00", base.steps_count,"In the Quantity field, enter a number.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Quantity field, enter a number.","Send Keys")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_PurchQtyGrid')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]", "5.00", base.steps_count,"In the Quantity field, enter a number.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Quantity')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]", "5.00", base.steps_count,"In the Quantity field, enter a number.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Quantity field, enter a number.","Send Keys")
            Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']",base.steps_count, "Click Save.")
# Closing the page
        base.steps_count +=1
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']", base.steps_count)
        time.sleep(1)
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Procurement and sourcing
        nav1 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Procurement and sourcing']")
# Clicking navigation: Purchase orders
        nav2 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: Purchase order confirmation
        nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Purchase order confirmation']")
# Clicking navigation: Confirm purchase orders
        nav4 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Confirm purchase orders']")
        time.sleep(3)
        base.steps_count +=1
        Interactions.assert_navigation(driver, base.steps_count, nav1, nav2, nav3, nav4)
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='AddParmTableButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='AddParmTableButton']",base.steps_count, "Click Add.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='AddParmTableButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='AddParmTableButton']",base.steps_count,"Click Add.")
        else:
            Interactions.fail_test_case(base.steps_count,"Click Add.","Click")
#    "Skipping grid since it is deafault behavior of d365"
        base.steps_count +=1
# Inputting into: PurchParmTable_PurchId
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]") ):
            #clicking inside grid: PurchParmTable_PurchId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchId')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_PurchId')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchId')])[1]", "",base.steps_count,"In the Purchase order field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase order')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Purchase order')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase order')])[1]", "",base.steps_count,"In the Purchase order field, enter or select a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Purchase order field, enter or select a value.","Send Keys")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]", "",base.steps_count,"In the Purchase order field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]", "",base.steps_count,"In the Purchase order field, enter or select a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Purchase order field, enter or select a value.","Send Keys")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: PurchParmTable_PurchId
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]") ):
            #clicking inside grid: PurchParmTable_PurchId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchId')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_PurchId')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchId')])[1]", "P0007930",base.steps_count,"In the Purchase order field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase order')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Purchase order')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase order')])[1]", "P0007930",base.steps_count,"In the Purchase order field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Purchase order field, type a value.","Send Keys")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]", "P0007930",base.steps_count,"In the Purchase order field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]", "P0007930",base.steps_count,"In the Purchase order field, type a value.")
            else:
                Interactions.fail_test_case(base.steps_count,"In the Purchase order field, type a value.","Send Keys")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']",base.steps_count, "Click OK.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']",base.steps_count,"Click OK.")
        else:
            Interactions.fail_test_case(base.steps_count,"Click OK.","Click")
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