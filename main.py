import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Tests(unittest.TestCase):

    def setUp(self):
        print("Testing !!!")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get('http://localhost:3000/')

    def test_add_input(self):
        self.input_field = self.driver.find_element(By.XPATH, '//header/input')
        self.input_field.clear()
        self.input_field.send_keys('Something To Do [field + ENTER]')
        time.sleep(2)
        self.input_field.send_keys(Keys.ENTER)
        time.sleep(2)
        self.list = self.driver.find_element(By.CLASS_NAME, 'list-unstyled').text
        self.assertTrue('Something To Do' in self.list)

    def test_actives(self):
        self.active_btn = self.driver.find_element(By.XPATH, "//footer/div[3]/ul/li[2]/a")
        self.first_check_box = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
        self.first_check_box.click()
        time.sleep(2)
        self.active_btn.click()
        time.sleep(2)
        self.list = self.driver.find_element(By.CLASS_NAME, 'list-unstyled').text
        self.assertFalse('Learn Javascript' in self.list)

    def test_completed(self):
        self.completed_btn = self.driver.find_element(By.XPATH, "//footer/div[3]/ul/li[3]/a")
        self.first_check_box = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
        self.first_check_box.click()
        time.sleep(2)
        self.completed_btn.click()
        time.sleep(2)
        self.list = self.driver.find_element(By.CLASS_NAME, 'list-unstyled').text
        self.assertTrue('Learn Javascript' in self.list)

    def test_undo_completed(self):
        self.completed_btn = self.driver.find_element(By.XPATH, "//footer/div[3]/ul/li[3]/a")
        self.first_check_box = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
        self.first_check_box.click()
        time.sleep(2)
        self.completed_btn.click()
        time.sleep(2)
        self.completed_first_check_box = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
        self.completed_first_check_box.click()
        time.sleep(2)
        self.list = self.driver.find_element(By.CLASS_NAME, 'list-unstyled').text
        self.assertFalse('Learn Javascript' in self.list)

    def test_search(self):
        self.search_btn = self.driver.find_element(By.XPATH, "//footer/div[1]/div/a[2]")
        self.search_btn.click()
        time.sleep(2)
        self.search_field = self.driver.find_element(By.XPATH, '//header/input')
        self.search_field.clear()
        self.search_field.send_keys('java')
        time.sleep(2)
        self.ulist = self.driver.find_element(By.CLASS_NAME, 'list-unstyled').text
        self.assertTrue('Learn Javascript' in self.ulist)
        self.assertFalse('Learn React' in self.ulist)

    def test_add_btn(self):
        self.add_btn = self.driver.find_element(By.XPATH, "//footer/div[1]/div/a[1]")
        self.add_btn.click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, '//header/input').is_displayed()

    def test_add_with_btn(self):
        self.add_btn = self.driver.find_element(By.XPATH, "//footer/div[1]/div/a[1]")
        self.add_btn.click()
        time.sleep(2)
        self.add_btn.click()
        self.add_input = self.driver.find_element(By.XPATH, '//header/input')
        self.add_input.send_keys('Something To Do [button]')
        time.sleep(2)
        self.add_input.send_keys(Keys.ENTER)
        time.sleep(2)
        self.ulist = self.driver.find_element(By.CLASS_NAME, 'list-unstyled').text
        self.assertTrue('Something To Do' in self.ulist)

    def tearDown(self):
        print("Done !!!")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
