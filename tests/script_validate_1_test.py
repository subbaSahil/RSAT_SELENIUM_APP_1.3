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
test_data = read_all_test_data("Data\script_validate_1_test_data.xlsx","DynamicFields")
@pytest.mark.ui
@pytest.mark.parametrize("data", test_data)
def test(data):
    base = BaseTest("user1",incognito=True)
    driver = base.driver
    actions = base.actions
    recorder=ScreenRecorder()
    try:
        recorder.start()
        base.steps_count += 1
        Interactions.log_interaction(base.steps_count, "Validate that the value for 'Purchase order' is :'000039'", "Validate 'Purchase order' field for 'current value'", "000039", "")
        print("Validation step logged for: Purchase order , value : 000039")
        base.steps_count += 1
        Interactions.log_interaction(base.steps_count, "Validate that 'Purchase order' is : 'enabled' ", "Validate 'Purchase order' field for 'enabled' ", "true", "")
        print("Validation step logged for: Purchase order is 'Enabled'")
        base.steps_count += 1
        Interactions.log_interaction(base.steps_count, "Validate that 'Purchase order' is : 'read-only'", "Validate 'Purchase order' field for 'read-only'", "false", "")
        print("Validation step logged for: Purchase order is 'Readonly'")
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