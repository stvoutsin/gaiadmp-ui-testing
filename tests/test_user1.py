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
import random
import string
import settings

@pytest.mark.usefixtures("setup")
class TestUser1():

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @pytest.mark.parametrize(
        "user, password",
        [(settings.username, settings.password)],
    )
    def test_user1(self, user, password):
        wait = WebDriverWait(self.driver, 60)
        time.sleep(2)

        setup_notebook_name = "setup_" + self.get_random_string(6)
        classifier_notebook_name = "ml_classifier_" + self.get_random_string(6)

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "userName")))
        self.driver.find_element(By.ID, "userName").click()
        self.driver.find_element(By.ID, "userName").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Import note")))
        time.sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Import note").click()
        time.sleep(3)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Add from URL")))
        self.driver.find_element(By.LINK_TEXT, "Add from URL").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportUrl")))
        self.driver.find_element(By.ID, "noteImportUrl").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportUrl")))
        self.driver.find_element(By.ID, "noteImportUrl").send_keys("https://raw.githubusercontent.com/wfau/aglais-notebooks/main/Public%20Examples/1.%20Start%20here.zpln")
        self.driver.find_element(By.ID, "noteImportName").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportName")))
        self.driver.find_element(By.ID, "noteImportName").send_keys("Users/" + user + "/" + setup_notebook_name)

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportModal")))
        self.driver.find_element(By.ID, "noteImportModal").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "importNoteButton")))
        self.driver.find_element(By.ID, "importNoteButton").click()

        time.sleep(10)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Users")))
        self.driver.find_element(By.LINK_TEXT, "Users").click()

        time.sleep(2)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, user)))
        self.driver.find_element(By.LINK_TEXT, user).click()

        time.sleep(2)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, setup_notebook_name)))
        self.driver.find_element(By.LINK_TEXT, setup_notebook_name).click()

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

        time.sleep(20)

        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-brand > span")))
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-brand > span").click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Import note")))
        self.driver.find_element(By.LINK_TEXT, "Import note").click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Add from URL")))
        self.driver.find_element(By.LINK_TEXT, "Add from URL").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportUrl")))
        self.driver.find_element(By.ID, "noteImportUrl").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportUrl")))
        self.driver.find_element(By.ID, "noteImportUrl").send_keys("https://raw.githubusercontent.com/wfau/aglais-notebooks/main/Public%20Examples/7.%20Good%20astrometric%20solutions%20via%20ML%20Random%20Forest%20classifier.zpln")
        self.driver.find_element(By.ID, "noteImportName").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportName")))
        self.driver.find_element(By.ID, "noteImportName").send_keys("Users/" +  user + "/" + classifier_notebook_name)

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "noteImportModal")))
        self.driver.find_element(By.ID, "noteImportModal").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "importNoteButton")))
        self.driver.find_element(By.ID, "importNoteButton").click()

        time.sleep(10)

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Users")))
        self.driver.find_element(By.LINK_TEXT, "Users").click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, user)))
        self.driver.find_element(By.LINK_TEXT, user).click()

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, classifier_notebook_name)))
        self.driver.find_element(By.LINK_TEXT, classifier_notebook_name).click()

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

        time.sleep(550)
        assert self.driver.find_element(By.CSS_SELECTOR, "#paragraph_1661761989954_2120199763_control > .ng-binding").text == "FINISHED"

