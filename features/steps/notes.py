import os
import unittest

from appium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSelectorException
from loremipsum import get_sentences

from time import sleep

use_step_matcher("re")

loremipsum_note = get_sentences(2)

@When('I touch Plus button')
def touch_Add_Note_Btn(context):
	context.driver.find_element_by_id('com.evernote:id/main_fab_image_view').click()

@Then('I should be able to write my Text Note')
def open_note_editor(context):
	el = context.driver.find_element_by_id('com.evernote:id/skittle_0')
	el.click()

@When('I entered my Note')
def writting_note(context):

	context.driver.find_element_by_id('com.evernote:id/check_mark')
	context.driver.find_element_by_id('com.evernote:id/title').click()
	context.driver.find_element_by_id('com.evernote:id/title').send_keys("Very New Title")
	context.driver.find_element_by_id('com.evernote:id/text').send_keys(loremipsum_note)

@Then('I should be able to save it')
def save_note(context):
	context.driver.find_element_by_id('com.evernote:id/check_mark').click()
	context.driver.find_element_by_name('Very New Title')

@Then('I reset my App')
def app_reset(context):
	context.driver.close_app()

@Then('I should see my saved Note')
def check_existing_Note(context):
	try:
		context.driver.find_element_by_name('Ready to do more with Evernote?')
	 	context.driver.find_element_by_id('com.evernote:id/tsd_dismiss_button').click()
	except NoSuchElementException:
		print ("No Premium Ad")
	context.driver.find_element_by_name('Very New Title')

@When('I touch one of saved Notes')
def open_saved_Note(context):
	context.driver.find_element_by_id('com.evernote:id/snippet_container').click()
	sleep (20) #Sleep due to poor performance of Android emulator

@Then('I should see it')
def check_opened_Note(context):
	context.driver.find_element_by_id('com.evernote:id/button_bar').click()
	sleep (10) #Sleep due to poor performance of Android emulator
	
	try:
		context.driver.find_element_by_name(loremipsum_note)
	except InvalidSelectorException:
		print ("Wrong Note displayed")










