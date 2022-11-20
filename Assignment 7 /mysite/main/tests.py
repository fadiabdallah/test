#from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class ContactFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/')
    #find the elements you need to submit form
    contact_name = selenium.find_element_by_id('id_name')
    contact_profession = selenium.find_element_by_id('id_profession')
    contact_mobile_number = selenium.find_element_by_id('id_mobile_number')
    contact_tel_number = selenium.find_element_by_id('id_tel_number')
    contact_address = selenium.find_element_by_id('id_address')

    submit = selenium.find_element_by_id('submit_button')

    #populate the form with data
    contact_name.send_keys('Rana')
    contact_profession.send_keys('Engineer')
    contact_mobile_number.send_keys('78919854')
    contact_tel_number.send_keys('01649639')
    contact_address.send_keys('Beirut')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Rana' in selenium.page_source