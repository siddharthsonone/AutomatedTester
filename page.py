import random
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import *

creds = json.load(open(r'cred.json'))
base_url = creds["server"]


class BasePage(object):
    # a class which as basic stuff that is necessary for every page
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title


class qa_page(BasePage):
    # EnterQAEnvironment

    def login_qa(self):
        self.driver.get(base_url)
        self.driver.find_element(*LandingPage.USERNAME).send_keys(LandingPage.user)
        self.driver.find_element(*LandingPage.PASSWORD).send_keys(LandingPage.password)
        self.driver.find_element(*LandingPage.SUBMIT).click()
        time.sleep(3)


class MainPage(BasePage):
    # Load the Home page of the website and perform basic checks

    def enter_basic_search(self):
        self.driver.find_element(*MainPageLocators.SPECIALITY).send_keys('Family Physicians')
        time.sleep(2)
        self.driver.find_element(*MainPageLocators.LOCATION).send_keys('10001')
        time.sleep(2)
        self.driver.find_element(*MainPageLocators.INSURANCE).click()
        time.sleep(2)
        WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(
            MainPageLocators.POPULAR_INSURANCES_VENDORS_LIST))
        self.driver.find_element(*MainPageLocators.AETNA).click()
        time.sleep(2)
        WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(
            MainPageLocators.SUBPLAN_LIST))
        self.driver.find_element(*MainPageLocators.AETNA_HMO).click()
        time.sleep(2)
        self.driver.find_element(*MainPageLocators.SEARCH).click()
        time.sleep(2)


class SigninPage(BasePage):
    # perform the validation of sign in using valid and invalid credentials

    def perform_valid_login(self):
        self.driver.get(base_url + '/signin')
        time.sleep(2)
        self.driver.find_element(*SigninPageLocators.EMAIL_ADDRESS).send_keys(SigninPageLocators.login_vaild_username)
        self.driver.find_element(*SigninPageLocators.PASSWORD).send_keys(SigninPageLocators.login_vaild_password)
        self.driver.find_element(*SigninPageLocators.SIGNIN).click()
        self.driver.implicitly_wait(120)
        time.sleep(8)

    def perform_invalid_login(self):
        self.driver.get(base_url + '/signin')
        time.sleep(2)
        self.driver.find_element(*SigninPageLocators.EMAIL_ADDRESS).send_keys(SigninPageLocators.login_invaild_username)
        self.driver.find_element(*SigninPageLocators.PASSWORD).send_keys(SigninPageLocators.login_invaild_password)
        self.driver.find_element(*SigninPageLocators.SIGNIN).click()
        self.driver.implicitly_wait(120)
        time.sleep(4)

    def forgot_password(self):
        self.driver.get(base_url + '/signin')
        time.sleep(2)
        self.driver.find_element(*SigninPageLocators.FORGOTPASSWORD).click()
        self.driver.implicitly_wait(120)
        time.sleep(2)


class CreateAccountPage(BasePage):
    # generate random first anme and last name details for users,using the random module
    first_name = random.choice(CreateAccountPageLocators.list_2)
    last_name = random.choice(CreateAccountPageLocators.list_2)
    email = first_name + '.' + last_name + '@gmail.com'

    def fill_signup_form(self):
        self.driver.get(base_url + '/createuser/details')
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.EMAIL_ADDRESS).send_keys(CreateAccountPage.email)
        self.driver.find_element(*CreateAccountPageLocators.CONFIRM_EMAIL_ADDRESS).send_keys(CreateAccountPage.email)
        self.driver.find_element(*CreateAccountPageLocators.PASSWORD_x).send_keys('Passwerd@123456')
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.FIRST_NAME).send_keys(CreateAccountPage.first_name)
        self.driver.find_element(*CreateAccountPageLocators.LAST_NAME).send_keys(CreateAccountPage.last_name)
        self.driver.find_element(*CreateAccountPageLocators.DOB_MONTH).send_keys(01)
        self.driver.find_element(*CreateAccountPageLocators.DOB_DAY).send_keys(01)
        self.driver.find_element(*CreateAccountPageLocators.DOB_YEAR).send_keys(1980)
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(CreateAccountPageLocators.PRIVACY))
        time.sleep(4)
        self.driver.find_element(*CreateAccountPageLocators.MALE_RADIOBUTTON).click()
        self.driver.find_element(*CreateAccountPageLocators.PRIVACY).click()
        self.driver.find_element(*CreateAccountPageLocators.HIPPA).click()
        self.driver.find_element(*CreateAccountPageLocators.SUBMIT).click()
        time.sleep(20)
        self.driver.implicitly_wait(120)


class InsuranceCardCapture(BasePage):
    def upload_front_image(self):
        WebDriverWait(self.driver, 200).until(EC.presence_of_element_located(ICCUploadPage.IMAGE_1_placeholder))
        front_upload = self.driver.find_element(*ICCUploadPage.IMAGE_1)
        front_upload.send_keys(r'insurance_card_front.jpg')
        time.sleep(1)

    def upload_back_image(self):
        WebDriverWait(self.driver, 200).until(EC.presence_of_element_located(ICCUploadPage.IMAGE_2_placeholder))
        back_image = self.driver.find_element(*ICCUploadPage.IMAGE_2)
        back_image.send_keys(r'insurance_card_back.PNG')
        time.sleep(1)

    def submit_cards(self):
        time.sleep(0.2)
        self.driver.find_element(*ICCUploadPage.UPLOAD_BUTTON).click()


class SponsoredActivationProcess(BasePage):
    def gotoSPOPage(self):
        self.driver.get(SponsoredActivation.url)
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located(SponsoredActivation.BUDGET_TABLE))
        self.driver.get(*SponsoredActivation.SELECT_BUDGET)
        time.sleep(1)
        self.driver.get(*SponsoredActivation.BUDGET_TABLE_ROW_CUSTOM_BUDGET).clear()
        self.driver.get(*SponsoredActivation.BUDGET_TABLE_ROW_CUSTOM_BUDGET).sendkeys(
            random.choice(SponsoredActivation.custom_budget_figures))
        self.driver.get(*SponsoredActivation.BUDGET_ACTIVATION).click()
        time.sleep(4)
        self.driver.get(SponsoredActivation.url_post_activation)
