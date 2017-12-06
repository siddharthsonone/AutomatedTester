import unittest
from selenium import webdriver
from page import *
from scenario_launcher_page import *

path = r'C:\chromedriver.exe'


class TestInsuranceCardCapture(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(path)
        page = qa_page(cls.driver)
        page.login_qa()

    def setUp(self):
        setup = ScenarioLauncherCreateICC(TestInsuranceCardCapture.driver)
        setup.create_link_zd()

    def test_insurance_card_upload(self):
        page = InsuranceCardCapture(TestInsuranceCardCapture.driver)
        page.upload_front_image()
        page.upload_back_image()
        page.submit_cards()
        time.sleep(4)
        assert 'Awesome sauce!' in self.driver.page_source

    @classmethod
    def tearDownClass(cls):
        TestInsuranceCardCapture.driver.close()
