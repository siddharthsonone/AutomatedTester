import json

from selenium.webdriver.common.by import By

creds = json.load(open(r'cred.json'))
base_url = creds["server"]


class PageObject(object):
    def __init__(self, driver):
        self.driver = driver


class LandingPage(object):
    creds = json.load(open(r'cred.json'))
    USERNAME = (By.XPATH, '//*[@id="txtUname"]')
    PASSWORD = (By.XPATH, '//*[@id="txtPassword"]')
    SUBMIT = (By.XPATH, '//*[@id="Button1"]')
    user = creds["server_username"]
    password = creds["server_passsword"]


class MainPageLocators(object):
    SEARCH = By.XPATH, '//*[@id="refine_search"]'
    SPECIALITY = (By.XPATH, '//*[@id="searchFieldsContainer"]/div[1]/div/div/div[1]/input')
    LOCATION = (By.XPATH, '//*[@id="searchFieldsContainer"]/div[2]/div/div/div[1]/input')
    INSURANCE = (By.XPATH, '//*[@id="searchFieldsContainer"]/div[3]/div/div/div/div/div/input')
    POPULAR_INSURANCES_VENDORS_LIST = (By.XPATH,
                                       """//*[@id="searchFieldsContainer"]
                                       /div[3]/div/div/div/div/div/
                                       div/div[3]/span/div/div/div[2]/div
                                        """)
    AETNA = (By.XPATH,
             '//*[@id="searchFieldsContainer"]/div[3]/div/div/div/div/div/div/div[3]/span/div/div/div[2]/ol/li[1]')

    SUBPLAN_LIST = (By.XPATH,
                    '//*[@id="searchFieldsContainer"]/div[3]/div/div/div/div/div/div/div[3]/span/div/div/div[2]/div')

    AETNA_HMO = (By.XPATH,
                 '//*[@id="searchFieldsContainer"]/div[3]/div/div/div/div/div/div/div[3]/span/div/div/div[2]/ol/li[1]')


class SigninPageLocators(object):
    creds = json.load(open(r'cred.json'))
    login_vaild_username = creds["username"]
    login_vaild_password = creds["password"]
    login_invaild_username = creds["username"]
    login_invaild_password = creds["password"]

    EMAIL_ADDRESS = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div[1]/div/div/div[2]/div/label[1]/div[2]/input')
    PASSWORD = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div[1]/div/div/div[2]/div/label[2]/div[2]/input')
    SIGNIN = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div[1]/div/div/div[2]/div/div[1]/button')
    INVAILDLOGIN = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div[1]/div/div/div[2]/div/span')
    FORGOTPASSWORD = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div[1]/div/div/div[2]/div/div[2]/a')


class CreateAccountPageLocators(object):
    list_2 = ['HalJordan', 'Batman', 'DickGrayson', 'Cyclone', 'Superman', 'LexLuthor', 'Joker', 'TimDrake', ]
    list_1 = ['Joker', 'LexLuthor', 'Darkseid', 'Sinestro', 'Brainiac', 'BlackAdam', 'RasalGhul', 'Deathstroke', ]

    EMAIL_ADDRESS = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[2]/div[1]/label/div[2]/input')
    CONFIRM_EMAIL_ADDRESS = (
        By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[2]/div[2]/label/div[2]/input')
    PASSWORD = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/input')
    PASSWORD_x = (By.XPATH, '//*[@type="password"]')
    FIRST_NAME = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div/input')
    LAST_NAME = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[4]/div[2]/div[1]/div[2]/div/input')
    DOB_MONTH = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[5]/div[2]/div/div[1]/div/input')
    DOB_DAY = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[5]/div[2]/div/div[2]/div/input')
    DOB_YEAR = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[5]/div[2]/div/div[3]/div/input')
    MALE_RADIOBUTTON = (
        By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[6]/div/div[2]/div/label[1]')
    FEMALE_RADIOBUTTON = (
        By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[6]/div/div[2]/div/label[2]')
    PRIVACY = (
        By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[7]/div/div/div/div[1]/div/div/label/input')
    HIPPA = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[7]/div/div/div/div[2]/div/label/input')
    SUBMIT = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div/div/div[8]/button')
    CONFIRM_LOGIN = (By.XPATH, '//*[@id="html"]/body/div[5]/div[2]/div/div/div/div[1]/div[3]/div[1]/span[1]')


class ICCUploadPage(object):
    IMAGE_1 = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div[2]/div[3]/div/label/input')
    IMAGE_1_placeholder = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div[2]/div[3]/div')
    IMAGE_2 = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div[2]/div[4]/div/label/input')
    IMAGE_2_placeholder = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div[2]/div[4]/div')
    UPLOAD_BUTTON = (By.XPATH, '//*[@id="main"]/div/main/span/div/div/div/div[2]/div[5]/button')
    PRIVACY = (By.XPATH, '//*[@id="main"]/div/footer/div[3]/div/div[1]/div/span[2]/a')
    TERMS = (By.XPATH, '//*[@id="main"]/div/footer/div[3]/div/div[1]/div/span[2]/a')


class SponsoredActivation(object):
    custom_budget_figures = ['111', '222', '333', '444', '555', '666', '777']
    url = base_url + '/provider/sponsoredresults/about'
    url_post_activation = base_url + '/provider/sponsoredresults'
    SELECT_BUDGET = (By.XPATH, '//*[@id="contentContainer"]/div[2]/div/div/div/div[1]/div/div[2]/div[3]/a')
    BUDGET_TABLE = (By.XPATH, '//*[@id="editBudget"]/div/div[2]/table')
    CUSTOM_BUDGET = (By.XPATH, '//*[@id="editBudget"]/div/div[2]/table/tbody/tr/td[4]/div[1]/input')
    BUDGET_TABLE_ROW_CUSTOM_BUDGET = (By.XPATH, '//*[@id="editBudget"]/div/div[2]/table/tbody/tr/td[4]')
    BUDGET_ACTIVATION = (By.XPATH, '//*[@id="editBudget"]/div/div[2]/table/tbody/tr/td[4]/div[3]')
    HELP = (By.XPATH, '//*[@id="contentContainer"]/div[3]/div[2]/div/a')
