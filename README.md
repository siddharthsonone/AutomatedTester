# automated_tester
A small project for performing automated non exhaustive smoke level testing  using Selenium Webdriver and concepts derived from Page Object Pattern. 




### Future Considerations:

#### Get Screenshot of a page.
#### Use a function like this to get the dimensions of an element

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get('https://www.google.co.in')
google_logo = (By.ID, 'hplogo')

def get_element_dimensions(locator):
  elem = driver.find_element(*locator)
  return elem.size['height'],elem.size['width'],elem.location['x'],elem.location['x']

str(get_element_dimensions(google_logo))

#### With the location and dimensions of the element,manipulate(crop) the screenshot and save it.
#### Re-run test cases and use PIL module to compare images.


