import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException


@pytest.mark.usefixtures("setup")
class TestUser2():

    @pytest.mark.parametrize(
        "user, password",
        [("user2", "pass")],
    )
    def test_user2(self, user, password):
        wait = WebDriverWait(self.driver, 60)
        time.sleep(2)

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "userName")))
        self.driver.find_element(By.ID, "userName").click()
        self.driver.find_element(By.ID, "userName").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Import note")))
        self.driver.find_element(By.LINK_TEXT, "Import note").click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Add from URL")))
        self.driver.find_element(By.LINK_TEXT, "Add from URL").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportUrl")))
        self.driver.find_element(By.ID, "noteImportUrl").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportUrl")))
        self.driver.find_element(By.ID, "noteImportUrl").send_keys("https://raw.githubusercontent.com/wfau/aglais-notebooks/main/AglaisPublicExamples/SetUp_2GP53P3PZ.zpln")
        self.driver.find_element(By.ID, "noteImportName").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportName")))
        self.driver.find_element(By.ID, "noteImportName").send_keys(user + "/setup")

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportModal")))
        self.driver.find_element(By.ID, "noteImportModal").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "importNoteButton")))
        self.driver.find_element(By.ID, "importNoteButton").click()

        time.sleep(10)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, user)))
        self.driver.find_element(By.LINK_TEXT, user).click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "setup")))
        self.driver.find_element(By.LINK_TEXT, "setup").click()

        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".labelBtn:nth-child(1) > .btn:nth-child(1)")))
        element = self.driver.find_element(By.CSS_SELECTOR, ".labelBtn:nth-child(1) > .btn:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".btn > .icon-control-play")))
        self.driver.find_element(By.CSS_SELECTOR, ".btn > .icon-control-play").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn > .icon-control-play")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[3]/div/div/button[2]")))
        self.driver.find_element(By.XPATH, "//div[3]/div/div/button[2]").click()

        time.sleep(30)


        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-brand > span")))
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-brand > span").click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Import note")))
        self.driver.find_element(By.LINK_TEXT, "Import note").click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Add from URL")))
        self.driver.find_element(By.LINK_TEXT, "Add from URL").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportUrl")))
        self.driver.find_element(By.ID, "noteImportUrl").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportUrl")))
        self.driver.find_element(By.ID, "noteImportUrl").send_keys("https://raw.githubusercontent.com/wfau/aglais-notebooks/main/AglaisPublicExamples/Good%20astrometric%20solutions%20via%20ML%20Random%20Forrest%20classifier_2GQDKZ59J.zpln")
        self.driver.find_element(By.ID, "noteImportName").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportName")))
        self.driver.find_element(By.ID, "noteImportName").send_keys(user + "/ml_forrest_classifier")

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportModal")))
        self.driver.find_element(By.ID, "noteImportModal").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "importNoteButton")))
        self.driver.find_element(By.ID, "importNoteButton").click()

        time.sleep(10)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, user)))
        self.driver.find_element(By.LINK_TEXT, user).click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ml_forrest_classifier")))
        self.driver.find_element(By.LINK_TEXT, "ml_forrest_classifier").click()

        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".labelBtn:nth-child(1) > .btn:nth-child(1)")))
        element = self.driver.find_element(By.CSS_SELECTOR, ".labelBtn:nth-child(1) > .btn:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".btn > .icon-control-play")))
        self.driver.find_element(By.CSS_SELECTOR, ".btn > .icon-control-play").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn > .icon-control-play")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[3]/div/div/button[2]")))
        self.driver.find_element(By.XPATH, "//div[3]/div/div/button[2]").click()
        element = self.driver.find_element(By.ID, "versionControlDropdown")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        time.sleep(600)
        assert self.driver.find_element(By.XPATH, "//div[3]/div/div[2]/div/div[2]").text == "1724028"
