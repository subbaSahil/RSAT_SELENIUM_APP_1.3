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
# Clicking navigation: Accounts payable
        nav1 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Purchase orders
        nav2 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: Open prepayments
        base.steps_count +=1
        nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Open prepayments']",base.steps_count, "Go to Accounts payable > Purchase orders > Open prepayments.")
        time.sleep(3)
        Interactions.assert_navigation(driver,nav1, nav2, nav3)
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewButton']", base.steps_count,"Click New.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='New']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='New']/ancestor::button",base.steps_count,"Click New.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewPaymentJournal']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewPaymentJournal']", base.steps_count,"Click Vendor payment journal.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Vendor payment journal']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Vendor payment journal']/ancestor::button",base.steps_count,"Click Vendor payment journal.")
        base.steps_count +=1
#    "Skipping grid since it is deafault behavior of d365"
        base.steps_count +=1
# Inputting into: JournalName
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'JournalName')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
            #clicking inside grid: JournalName
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'JournalName')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'JournalName')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'JournalName')])[1]", "VendPay",base.steps_count,"In the Name field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "VendPay",base.steps_count,"In the Name field, enter or select a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'JournalName')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'JournalName')]", "VendPay",base.steps_count,"In the Name field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "VendPay",base.steps_count,"In the Name field, enter or select a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
#    "Skipping grid since previous was control was input"
        base.steps_count +=1
        base.steps_count +=1
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']",base.steps_count, "Click Save.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Inquiries']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Inquiries']", base.steps_count,"Click Inquiries.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Inquiries']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Inquiries']/ancestor::button",base.steps_count,"Click Inquiries.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='BalanceControl']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='BalanceControl']", base.steps_count,"Click Balance control.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Balance control']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Balance control']/ancestor::button",base.steps_count,"Click Balance control.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Close']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Close']",base.steps_count, "Click Close.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Close']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Close']",base.steps_count,"Click Close.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='JournalLines']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='JournalLines']",base.steps_count,"Click Lines.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='JournalLines']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='JournalLines']",base.steps_count,"Click Lines.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Lines']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Lines']",base.steps_count,"Click Lines.")
        else:
            Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
            if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='JournalLines']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='JournalLines']",base.steps_count,"Click Lines.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Lines']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Lines']",base.steps_count,"Click Lines.")
        base.steps_count +=1
#    "Skipping grid since it is deafault behavior of d365"
        base.steps_count +=1
# Inputting into: LedgerJournalTrans_AccountNum
        base.steps_count +=1
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
            #clicking inside grid: LedgerJournalTrans_AccountNum
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "checkgrid1",base.steps_count,"In the Account field, specify the desired values.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "checkgrid1",base.steps_count,"In the Account field, specify the desired values.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "checkgrid1",base.steps_count,"In the Account field, specify the desired values.")
            else:
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "checkgrid1",base.steps_count,"In the Account field, specify the desired values.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "checkgrid1",base.steps_count, "In the Account field, specify the desired values.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "checkgrid1",base.steps_count,"In the Account field, specify the desired values.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "checkgrid1",base.steps_count,"In the Account field, specify the desired values.")
            else:
                actions.move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "checkgrid1",base.steps_count,"In the Account field, specify the desired values.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonPaymProposal']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonPaymProposal']", base.steps_count,"Click Payment proposal.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Payment proposal']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Payment proposal']/ancestor::button",base.steps_count,"Click Payment proposal.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='VendPaymProposalCreate']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='VendPaymProposalCreate']", base.steps_count,"Click Create payment proposal.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Create payment proposal']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Create payment proposal']/ancestor::button",base.steps_count,"Click Create payment proposal.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OkButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OkButton']",base.steps_count, "Click OK.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']",base.steps_count,"Click OK.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CommandButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CommandButton']",base.steps_count, "Click OK.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']",base.steps_count,"Click OK.")
# Closing the page
        base.steps_count +=1
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']", base.steps_count)
        time.sleep(1)
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonCheckJournal']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonCheckJournal']", base.steps_count,"Click Validate.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Validate']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Validate']/ancestor::button",base.steps_count,"Click Validate.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CheckVoucher']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CheckVoucher']", base.steps_count,"Click Validate voucher only.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Validate voucher only']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Validate voucher only']/ancestor::button",base.steps_count,"Click Validate voucher only.")
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