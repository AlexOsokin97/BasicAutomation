from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('C:/Users/Alexander/drivers/chromedriver')

def getToWebsite():
	driver.get('https://university.mongodb.com/')

def wTime(number):
	time.sleep(number)


def findSignIn():
	button = driver.find_element_by_link_text('Get Started')
	button.click()

def fillSignIn(name, last, mail, passw, comp):
	fName = driver.find_element_by_id('firstName')
	lName = driver.find_element_by_id('lastName')
	email = driver.find_element_by_id('email')
	password = driver.find_element_by_id('password')
	select_country = Select(driver.find_element_by_id('country'))
	select_job_function = Select(driver.find_element_by_id('jobfunction'))
	company = driver.find_element_by_id('company')

	wTime(2)

	for letter in name:
		fName.send_keys(letter)
		wTime(0.2)

	lName.click()
	for letter in last:
		lName.send_keys(letter)
		wTime(0.2)

	email.click()
	for character in mail:
		email.send_keys(character)
		wTime(0.2)

	password.click()
	for character in passw:
		password.send_keys(character)	
		wTime(0.2)

	select_country.select_by_visible_text('Israel')

	select_job_function.select_by_visible_text('Software Developer / Engineer')

	company.click()
	for letter in comp:
		company.send_keys(letter)

	check_protection = driver.find_element_by_id('g-recaptcha')
	check_protection.click()

	







getToWebsite()
wTime(3)
findSignIn()
fillSignIn('Mike','Johns','something@gmail.com','12345','company')

wTime(5)
driver.quit()