import json
import random

from selenium.webdriver.common.by import By

creds = json.load(open(r'cred.json'))
base_url = creds["server"]


class ScenarioLauncher(object):
    activator = base_url + '/test/scenariolauncher'


class GeneralProviderSetup(ScenarioLauncher):
    url = base_url + '/test/scenariolauncher#provider-setup_general-setup'
    sample_addresses = ['Onyx 3rd Floor Koregaon Park', '568 Broadway, New York, NY 10012',
                        '6991 E. Camelback Rd., B-260, Scottsdale, AZ 85251']
    sample_names = ['Galileo Galilei', 'Sir Francis Drake', 'Henry Hudson', 'Prince Henry', 'Michelangelo Falvetti',
                    'Pietro Pomponazzi', 'Nicolaus Copernicus', 'William Shakespeare']

    PROVIDER_NAME = random.choice(sample_names)
    PROVIDER_ADDRESSES = random.choice(sample_addresses)
    LOCATION_ADDRESSES = (By.NAME, 'locationAddresses')
    PROFESSIONAL_NAMES = (By.NAME, 'professionalNames')
    ADD_PROFESSIONAL = (By.ID, 'addProfessional')
    CHECKBOX_ADD_NOTIFICATIONS = (By.XPATH, '//*[@id="-provider-setup_general-setup"]/form/label[3]/input')
    CHECKBOX_AD_ELIGIBLE = (By.XPATH, '//*[@id="-provider-setup_general-setup"]/form/label[5]/input')
    CHECKBOX_ZOCDOC_JR = (By.XPATH, '//*[@id="-provider-setup_general-setup"]/form/label[8]/input')
    SUBMIT = (By.CLASS_NAME, 'button.btn.btn-primary')
    SUBMIT_css_selector = (By.CSS_SELECTOR, '#-provider-setup_general-setup > form > div.btn-toolbar > button')
    PROGRESS_BAR = (By.CLASS_NAME, 'progress progress-striped active')
    RESPONSE_TABLE = (By.XPATH, '//*[@id="-provider-setup_general-setup"]/div[2]/div')
    PROVIDER_LINK = (By.PARTIAL_LINK_TEXT, 'Go to Interface')


class InsuranceCardCaptureForZocdoc(ScenarioLauncher):
    url = base_url + '/test/scenariolauncher#insurance-card-capture_create-zd-icc-upload-link'
    PROVIDER_ID = (By.XPATH, '//*[@id="-insurance-card-capture_create-zd-icc-upload-link"]/form/label[2]/input')
    GENERATE_LINK = (By.XPATH, '//*[@id="-insurance-card-capture_create-zd-icc-upload-link"]/form/button')
    IS_VALID_TOGGLE = (By.XPATH, '//*[@id="-insurance-card-capture_create-zd-icc-upload-link"]/form/label[1]/input')
    UPLOAD_LINK = (
        By.XPATH, '//*[@id="-insurance-card-capture_create-zd-icc-upload-link"]/div[2]/div/table/tbody/tr[1]/td[2]/a')
    RESPONSE_TABLE = (
        By.XPATH, '//*[@id="-insurance-card-capture_create-zd-icc-upload-link"]/div[2]/div/table/tbody/tr[2]/td[2]')


class InsuranceCardCaptureForNonZocdoc(ScenarioLauncher):
    url = base_url + '/test/scenariolauncher#insurance-card-capture_create-non-zd-icc-upload-link'
    PROVIDER_ID = (By.XPATH, '//*[@id="-insurance-card-capture_create-non-zd-icc-upload-link"]/form/label[2]/input')
    GENERATE_LINK = (By.XPATH, '//*[@id="-insurance-card-capture_create-non-zd-icc-upload-link"]/form/button')
    UPLOAD_LINK = (
        By.XPATH,
        '//*[@id="-insurance-card-capture_create-non-zd-icc-upload-link"]/div[2]/div/table/tbody/tr[1]/td[2]/a')
    RESPONSE_TABLE = (
        By.XPATH, '//*[@id="-insurance-card-capture_create-non-zd-icc-upload-link"]/div[2]/div/table/tbody/tr[2]/td[2]')
