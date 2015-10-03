import os
import unittest

from appium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException
from loremipsum import get_sentences

from time import sleep

use_step_matcher("re")

@given('user on the Welcome screen')
def find_Sign_in_btn(context):
	context.driver.is_app_installed('com.evernote')
	context.driver.find_element_by_name("SIGN IN")
		
@When('I click on the Sign In button')
def click_Sign_in_Btn(context):
	el = context.driver.find_element_by_name("SIGN IN")
	el.click()

@Then('Login Screen should be presented')
def check_Login_fields(context):
	context.driver.find_element_by_name("Username or Email")

@When('I enter my Valid credentials')
def entering_credentials(context):
	textfields = context.driver.find_elements_by_class_name("android.widget.EditText")
	textfields[0].send_keys("airnes@yandex.ru")
	textfields[1].send_keys("Vfrfhjd57896")

@When('I touch Sing In button')
def touch_Sign_in_Btn(context):	
	context.driver.find_element_by_name("Sign In").click()
	
@Then('I should see All my Notes')
def check_My_Notes_presented(context):
	sleep (45) #Should be functuon in Runtime to check if Message center screen appears
	
	message_card = context.driver.find_element_by_id('com.evernote:id/message_card_layout')
	
@Given('I going to login on Android')
def user_login_flow(context):
	context.driver.launch_app()
	context.driver.is_app_installed('com.evernote')
	context.driver.find_element_by_name("SIGN IN")
	context.driver.find_element_by_name("SIGN IN").click()
	context.driver.find_element_by_name("Username or Email")
	textfields = context.driver.find_elements_by_class_name("android.widget.EditText")
	textfields[0].send_keys("airnes@yandex.ru")
	textfields[1].send_keys("Vfrfhjd57896")
	context.driver.find_element_by_name("Sign In").click()
	sleep(45) #Should be functuon in Runtime to check if Message center screen appears
	message_card = context.driver.find_element_by_id('com.evernote:id/message_card_layout')
	







	

