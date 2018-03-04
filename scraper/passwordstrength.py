from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import Tag, NavigableString, BeautifulSoup

# imitates a web browser
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

class PasswordStrength(object):
	def __init__(self, word):
		self.driver = webdriver.PhantomJS()
		self.word = word
	def connect(self):
		driver = self.driver
		driver.get("http://www.passwordmeter.com")

		driver.implicitly_wait(1) # wait 1 seconds
		print("Successfully connected to the page.")
	def checkWordStrength(self):
		driver = self.driver
		# waiting for the page to load
		driver.implicitly_wait(1)
		textinput = driver.find_element_by_id("passwordPwd")
		# type in words
		textinput.clear()
		textinput.send_keys(self.word)

		strength = driver.find_element_by_id("complexity")
		percentage = driver.find_element_by_id("score")
		return strength.text, percentage.text
	def close(self):
		self.driver.close()
		print("Closed window.")
	def run(self):
		self.connect()
		strength, percentage = self.checkWordStrength()
		print strength
		print percentage
		self.close()
		return strength, percentage