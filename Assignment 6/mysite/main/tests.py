#from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class TeamFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/')
    #find the elements you need to submit form
    team_name = selenium.find_element('name','team_name')
    city = selenium.find_element('name','city')
    year_founded = selenium.find_element('name','year_founded')
  

    submit = selenium.find_element('id','submit_button')

    #populate the form with data
    team_name.send_keys('Lebron James')
    city.send_keys('Los Angeles Lakers')
    year_founded.send_keys('2001')
  

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Lebron James' in selenium.page_source