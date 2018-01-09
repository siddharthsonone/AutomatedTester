import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Locators(object):
    SPECIALITY_search = (By.CSS_SELECTOR,'input.searchTextBox__StyledInput-o0zgcl-2.jsrPpB')
    SPECIALITY_row = (By.CSS_SELECTOR,'div.searchDropdownItem__Text-wie5bb-1.dJgsXJ')
    LOCATION_search = (By.CSS_SELECTOR,'input.TakeoverInput__SearchFieldInput-fl6jub-3.gXkxDn')
    LOCATION_row = (By.CSS_SELECTOR,'div.s1d75n1w-0-dropdown-primitives__Item-mOFBU.kqLoZd')



class BaseClass(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Firefox()
    
    def test_search_loc(self, url='https://providers.geisinger.org/search', query='New' ,css_selector_1='input.TakeoverInput__SearchFieldInput-fl6jub-3.gXkxDn', css_selector_2='div.s1d75n1w-0-dropdown-primitives__Item-mOFBU.kqLoZd'):
        self.url = url
        self.query = query
        self.css_selector_1 = css_selector_1
        self.css_selector_2 = css_selector_2
        self.driver.get(url)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 
                        css_selector_1))).clear()
        self.driver.implicitly_wait(2)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 
                        css_selector_1))).send_keys(query)
        self.driver.implicitly_wait(10)
        self.results_set= []
        for results in self.driver.find_elements_by_css_selector(css_selector_2):
            
            assert(query in results.text) #query in resultspace
            assert('rgb(255, 100, 115)' in results.find_element_by_tag_name('mark').value_of_css_property('color')) #query color

            self.results_set.append([results.text ,results.find_element_by_tag_name('mark').text, results.find_element_by_tag_name('mark').value_of_css_property('color')])
        return self.results_set

    def test_search_spec(self, url='https://providers.geisinger.org/search', query='fever' ,css_selector_1='input.searchTextBox__StyledInput-o0zgcl-2.jsrPpB', css_selector_2='div.s1d75n1w-0-dropdown-primitives__Item-mOFBU.kqLoZd'):
        self.url = url
        self.query = query
        self.css_selector_1 = css_selector_1
        self.css_selector_2 = css_selector_2
        self.driver.get(url)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 
                        css_selector_1))).clear()
        self.driver.implicitly_wait(2)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 
                        css_selector_1))).send_keys(query)
        self.driver.implicitly_wait(10)
        self.results_set= []
        for results in self.driver.find_elements_by_css_selector(css_selector_2):
            
            assert(query in results.text) #query in resultspace
            assert('rgb(255, 100, 115)' in results.find_element_by_tag_name('em').value_of_css_property('color')) #query color

            self.results_set.append([results.text ,results.find_element_by_tag_name('em').text, results.find_element_by_tag_name('em').value_of_css_property('color')])
        return self.results_set



    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        


   
if __name__ == '__main__':
    unittest.main(verbosity=5)
 
