#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Locators:

    SPECIALITY_search = (By.CSS_SELECTOR,
                         'input.searchTextBox__StyledInput-o0zgcl-2')
    SPECIALITY_row = (By.CSS_SELECTOR,
                      'div.searchDropdownItem__Text-wie5bb-1.dJgsXJ')
    SPECIALITY_container = (By.XPATH,
                            '/html/body/div/main/div[1]/section/form/div[1]/div[2]/div[3]'
                            )
    SPECIALITY_row_xpath = (By.XPATH,
                            '/html/body/div/main/div[1]/section/form/div[1]/div[2]/div[3]/div[1]/div[1]'
                            )
    SPECIALITY_row_xpath_all = (By.XPATH,
                                '/html/body/div/main/div[1]/section/form/div[1]/div[2]/div[3]/div/div/div'
                                )
    Default_LOCATION = (By.XPATH, '/html/body/div/main/section/h1/a')
    LOCATION_search = (By.CSS_SELECTOR,
                       'input.TakeoverInput__SearchFieldInput-fl6jub-3')
    LOCATION_row = (By.CSS_SELECTOR,
                    'div.s1d75n1w-0-dropdown-primitives__Item-mOFBU.kqLoZd'
                    )
    LOCATION_conatiner = (By.XPATH,
                          '/html/body/div/main/div[1]/section/form/div[2]/div/div/div[2]/div[3]'
                          )
    LOCATION_row_xpath = (By.XPATH,
                          '/html/body/div/main/div[1]/section/form/div[2]/div/div/div[2]/div/div[1]'
                          )
    LOCATION_row_xpath_all = (By.XPATH,
                              '/html/body/div/main/div[1]/section/form/div[2]/div/div/div[2]/div/div'
                              )

    SEARCH_BOX = (By.XPATH,
                  '/html/body/div/main/div[1]/section/form/div[1]/div[2]/div/input'
                  )
    LOCATION_BOX = (By.XPATH,
                    '/html/body/div/main/div[1]/section/form/div[2]/div/div/div/div[1]/input'
                    )
    INSURANCE_BOX = (By.XPATH,
                     '/html/body/div/main/div[1]/section/form/div[3]/div/div/input'
                     )
    HEADER = (By.XPATH, '/html/body/div/main/div[1]/section')
    FOOTER = (By.XPATH, '/html/body/div/main/footer/section')
    FILTER = (By.XPATH, '/html/body/div/main/div[2]/div[2]/div[2]/div')
    PAGINATION = (By.XPATH, '/html/body/div/main/div[2]/nav/a[8]')
    PAGINATION_number = (By.XPATH, '/html/body/div/main/div[2]/nav/a[2]'
                         )
    FILTER_button = (By.XPATH,
                     '/html/body/div/main/div[2]/div[2]/div[2]/div/button'
                     )
    FILTER_toggle = (By.XPATH,
                     '/html/body/div/main/div[2]/div[2]/div[2]/div/button[1]/svg'
                     )
    FILTER_dissmiss = (By.XPATH,
                       '/html/body/div/main/div[2]/div[2]/div[2]/div/button[2]'
                       )
    FILTER_PANE = (By.XPATH,
                   '/html/body/div/main/div[2]/div[3]/aside/div/div/div[2]/div[1]/div/div[2]'
                   )
    FILTER_RAIO_TODAY = (By.XPATH,
                         '/html/body/div/main/div[2]/div[3]/aside/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/label[2]/div/input'
                         )


class LoadPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://providers.geisinger.org/search')
        cls.driver.maximize_window()

    def test_load(self):
        self.driver.find_element(*Locators.HEADER)

        WebDriverWait(self.driver,
                      30).until(EC.presence_of_element_located(Locators.HEADER))

        # headerloaded

        WebDriverWait(self.driver,
                      30).until(EC.presence_of_element_located(Locators.FOOTER))

        # footerloaded

        footer_text = self.driver.find_element(*Locators.FOOTER).text
        assert 'Zocdoc' in footer_text
        assert 'Geisinger' in footer_text
        header_text = self.driver.find_element(*Locators.HEADER).text
        assert 'Zocdoc' in footer_text
        assert 'Geisinger' in footer_text

    def test_default(self):
        assert 'Danville' \
            in self.driver.find_element(*Locators.Default_LOCATION).text

    def test_filter(self):

        WebDriverWait(self.driver,
                      30).until(EC.visibility_of_element_located(Locators.FILTER))
        count_filter = \
            self.driver.find_element(*Locators.FILTER_button).text
        assert 'refine matches' == count_filter

        # interact

        self.driver.find_element(*Locators.FILTER_button).click()
        assert 'close' \
            in self.driver.find_element(*Locators.FILTER_dissmiss).text

        # checking close

        self.filter_criterias = []
        for filter_options in \
            self.driver.find_elements(*Locators.FILTER_PANE):
            self.filter_criterias.append(filter_options.text)
            list_ = self.filter_criterias[0].encode('ascii', 'ignore'
                    ).split('\n')
        assert 'any day' in list_
        assert 'today' in list_
        assert 'next 3 days' in list_
        assert 'special hours' in list_
        assert 'doctor\'s gender' in list_
        assert 'languages spoken' in list_

        # incremetcount

        self.driver.find_element(*Locators.FILTER_RAIO_TODAY).click()
        assert 'close' \
            in self.driver.find_element(*Locators.FILTER_dissmiss).text
        time.sleep(5)
        self.driver.find_element(*Locators.FILTER_dissmiss).click()

        WebDriverWait(self.driver,
                      30).until(EC.invisibility_of_element_located(Locators.FILTER_PANE))
        assert 'refine (1 applied)' \
            == self.driver.find_element(*Locators.FILTER_button).text

    def test_pagination(self):
        self.driver.refresh()
        self.driver.find_element(*Locators.PAGINATION).click()
        self.driver.refresh()
        time.sleep(3)

        assert '2' \
            == self.driver.find_element(*Locators.PAGINATION_number).text

    def test_seacrh(self):
        self.driver.find_element(*Locators.SEARCH_BOX).send_keys('Fever'
                )
        time.sleep(2)
        self.results = []
        for result in \
            self.driver.find_elements(*Locators.SPECIALITY_row_xpath_all):
            if 'Fever' in result.text:

                assert 'rgb(255, 100, 115)' \
                    in result.find_element_by_tag_name('em'
                        ).value_of_css_property('color')
                self.results.append([result.text,
                                    result.find_element_by_tag_name('em'
                                    ).text,
                                    result.find_element_by_tag_name('em'
                                    ).value_of_css_property('color')])
            else:
                self.results.append([result.text])
                pass

        return self.results

    def test_location(self):
        self.driver.find_element(*Locators.LOCATION_BOX).clear()
        self.driver.find_element(*Locators.LOCATION_BOX).send_keys('New'
                )
        time.sleep(3)
        self.results = []

        for location in \
            self.driver.find_elements(*Locators.LOCATION_row_xpath_all):
            if 'New' in location.text:

                assert 'rgb(255, 100, 115)' \
                    in location.find_element_by_tag_name('mark'
                        ).value_of_css_property('color')
                self.results.append([location.text,
                                    location.find_element_by_tag_name('mark'
                                    ).text,
                                    location.find_element_by_tag_name('mark'
                                    ).value_of_css_property('color')])
            else:

                self.results.append([location.text])
                pass

        return self.results

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=5)


            
