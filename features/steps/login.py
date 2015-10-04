import os
import unittest

from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException
from loremipsum import get_sentences

from time import sleep

use_step_matcher("re")

userLogin = 'enterEmailAddress'
userPass = 'EnterPassword'


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
	textfields[0].send_keys(userLogin)
	textfields[1].send_keys(userPass)

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
	textfields[0].send_keys(userLogin)
	textfields[1].send_keys(userPass)
	context.driver.find_element_by_name("Sign In").click()
	sleep(45) #Should be functuon in Runtime to check if Message center screen appears
	message_card = context.driver.find_element_by_id('com.evernote:id/message_card_layout')
	
@Given('I tap Authenticate button to authorise user')
def authenticate_btn_tap(context):
	context.driver.find_element_by_id('Authenticate').click()
	sleep (15) #wait for action in interface. Shoud be a Runtime check instead of sleep	

@Then('I need to enter my credentials')
def enter_iOS_credentials(context):
	context.driver.find_element_by_class_name("UIATextField").click()
	context.driver.find_element_by_class_name("UIATextField").send_keys(userLogin)
	context.driver.find_element_by_class_name("UIASecureTextField").click()
	context.driver.find_element_by_class_name("UIASecureTextField").send_keys(userPass)
	context.driver.execute_script('UIATarget.localTarget().frontMostApp().keyboard().buttons()["Go"].tap();');
	sleep (5)
	context.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAButton[1]").click() #Workaroud as Appium can't access to web element
	sleep (5)

@Given('I going to login on iOS')
def iOS_login_flow(context):
	context.driver.launch_app()
	context.driver.find_element_by_id('Authenticate').click()
	sleep (5) #wait for action in interface	
	context.driver.find_element_by_class_name("UIATextField").click()
	context.driver.find_element_by_class_name("UIATextField").send_keys(userLogin)
	context.driver.find_element_by_class_name("UIASecureTextField").click()
	context.driver.find_element_by_class_name("UIASecureTextField").send_keys(userPass)
	context.driver.execute_script('UIATarget.localTarget().frontMostApp().keyboard().buttons()["Go"].tap();');
	sleep (5)
	context.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAButton[1]").click() #Workaroud as Appium can't access to web element
	sleep (5)
	try:
		context.driver.find_element_by_id('Create photo note')
	except NoSuchElementException:
		print ("Evernote SDK Element not found")



	

