import json
from scenario_launcher import *
from page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
creds = json.load(open(r'cred.json'))
base_url = creds["server"]


class ScenarioLauncherCreateICC(BasePage):

    def create_link_zd(self):
        self.driver.get(InsuranceCardCaptureForZocdoc.url)
        time.sleep(4)
        self.driver.find_element(*InsuranceCardCaptureForZocdoc.GENERATE_LINK).click()
        link = WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located(InsuranceCardCaptureForZocdoc.UPLOAD_LINK))
        time.sleep(2)
        self.driver.get(base_url+link.text)

    def create_link_non_zd(self):
        self.driver.get(InsuranceCardCaptureForNonZocdoc.url)
        time.sleep(4)
        self.driver.find_element(*InsuranceCardCaptureForNonZocdoc.GENERATE_LINK)
        link = WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located(InsuranceCardCaptureForNonZocdoc.UPLOAD_LINK))
        time.sleep(2)
        self.driver.get(base_url + link.text)


class SetUpSPO(BasePage):

    doctor_name = random.choice(GeneralProviderSetup.sample_names)
    doctor_address = random.choice(GeneralProviderSetup.sample_addresses)

    def provider_setup_spo(self):
        self.driver.get(GeneralProviderSetup.url)
        time.sleep(2)
        self.driver.find_element(*GeneralProviderSetup.LOCATION_ADDRESSES).clear()
        self.driver.find_element(*GeneralProviderSetup.LOCATION_ADDRESSES).send_keys(SetUpSPO.doctor_address)
        time.sleep(0.2)
        self.driver.find_element(*GeneralProviderSetup.PROFESSIONAL_NAMES).clear()
        self.driver.find_element(*GeneralProviderSetup.PROFESSIONAL_NAMES).send_keys(
            SetUpSPO.doctor_name)
        time.sleep(0.2)
        self.driver.find_element(*GeneralProviderSetup.CHECKBOX_ADD_NOTIFICATIONS).click()
        time.sleep(0.2)
        self.driver.find_element(*GeneralProviderSetup.CHECKBOX_AD_ELIGIBLE).click()
        time.sleep(0.2)
        self.driver.find_element(*GeneralProviderSetup.SUBMIT_css_selector).click()
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located(GeneralProviderSetup.PROVIDER_LINK))
        url = self.driver.find_element(*GeneralProviderSetup.PROVIDER_LINK).get_attribute('href')
        self.driver.get(url)
