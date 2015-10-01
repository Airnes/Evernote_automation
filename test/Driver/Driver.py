import os
import unittest

from appium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
	os.path.join(os.path.dirname(__file__), p)
)

class AndroidLoginFlow(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.1'
		desired_caps['deviceName'] = 'Nexus5'
		desired_caps['app'] = '/Users/Airness/Projects/Stanfy_Test/apps/evernote.apk'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
	def tearDown(self):
		# end the session
		self.driver.quit()

	def test_find_elements(self):
		# some delay to generate xml
		sleep(2)

		el = self.driver.find_element_by_name("SIGN IN")
		el.click()

		textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
		textfields[0].send_keys("test@user.com")
		textfields[2].send_keys("Pass")

		self.assertEqual('Appium User', textfields[0].text)
		self.assertEqual('someone@appium.io', textfields[1].text)

		self.driver.find_element_by_accessibility_id("com.evernote:id/landing_disclaimer").click()
	   

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
	unittest.TextTestRunner(verbosity=2).run(suite)





