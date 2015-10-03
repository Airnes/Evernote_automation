import os
import unittest

from appium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

def before_feature(context,feature):
	app = '/Users/Airness/Projects/Evernote_automation/apps/evernote.apk'
	context.driver = webdriver.Remote(
		command_executor='http://127.0.0.1:4723/wd/hub',
		desired_capabilities={
			'app': app,
			'platformName': 'Android',
			'platformVersion': '5.1',
			'deviceName': 'Nexus5',
			'fullReset': 'True',
			'noReset': 'False'
		})


def after_feature(context,feature):
		context.driver.quit()





