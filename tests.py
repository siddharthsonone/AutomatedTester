import unittest
from selenium import webdriver
from page import *
from scenario_launcher_page import *

path = r''


class TestMainPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        page = qa_page(self.driver)
        page.login_qa()

    def test_mock(self):
        assert 'zocdoc' in self.driver.page_source

    def test_search(self):
        page = MainPage(self.driver)
        page.enter_basic_search()
        assert 'Doctors' in self.driver.page_source

    def tearDown(self):
        self.driver.close()


class TestSigninPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        page = qa_page(self.driver)
        page.login_qa()

    def test_valid_sign_in(self):
        page = SigninPage(self.driver)
        page.perform_valid_login()
        assert self.driver.title == 'Medical Team - Zocdoc'

    def test_invalid_sign_in(self):
        page = SigninPage(self.driver)
        page.perform_invalid_login()
        assert self.driver.find_element(*SigninPageLocators.INVAILDLOGIN).text == 'Incorrect email or password.'

    def test_forgot_password(self):
        page = SigninPage(self.driver)
        page.forgot_password()
        assert self.driver.title == 'Reset Password'

    def tearDown(self):
        self.driver.close()


class TestCreateAccountPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        page = qa_page(self.driver)
        page.login_qa()

    def test_CreateAccount(self):
        page = CreateAccountPage(self.driver)
        page.fill_signup_form()
        assert self.driver.title == 'Medical Team - Zocdoc'

    def tearDown(self):
        self.driver.close()


class TestInsuranceCardCapture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
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
        time.sleep(5)
        assert 'Awesome sauce!' in self.driver.page_source

    @classmethod
    def tearDownClass(cls):
        TestInsuranceCardCapture.driver.close()


class TestSPO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        page = qa_page(cls.driver)
        page.login_qa()

    def setUp(self):
        page = SetUpSPO(TestSPO.driver)
        page.provider_setup_spo()
        time.sleep(2)

    def TestPlaceholder(self):
        pass

    @classmethod
    def tearDownClass(cls):
        TestSPO.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
