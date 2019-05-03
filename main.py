import selenium
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import time

id = sys.argv[1]
password = sys.argv[2]
val = sys.argv[3]

def navtofeedpage():
	feedbackpage = driver.find_element_by_link_text('Course End Feedback')
	feedbackpage.click()
	time.sleep(2)


opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox()

driver.get('http://www.nitandhra.ac.in/student/auth/login')

id_box = driver.find_element_by_name('identity')
pass_box = driver.find_element_by_name('password')
submit_box = driver.find_element_by_name('submit')

id_box.send_keys(id)
pass_box.send_keys(password)
submit_box.click()

time.sleep(1.5)

navtofeedpage()

not_submitted = driver.find_elements_by_class_name('glyphicon-remove')

print(not_submitted[0].text)
while(len(not_submitted) != 0):
	try:
		print(len(not_submitted))
		course = not_submitted[0]
		course.click()
		dropboxes = driver.find_elements_by_tag_name('select')
		for options in dropboxes:
			Select(options).select_by_value(val)
		#options.select_by_value('4')
		submitfeed = driver.find_elements_by_class_name('btn-success')
		submitfeed[1].click()
		navtofeedpage()
		not_submitted = driver.find_elements_by_class_name('glyphicon-remove')
	except:
		pass

	#dropboxes.select_by_value('4')