#!/usr/bin/python3
# Author: @nu11secur1ty
# Debug: g3ck0dr1v3r
from selenium import webdriver
import time

#enter the link to the website you want to automate login.
website_link="https://snapsave.app/#google_vignette"

#enter the element for submit button by class
element_for_submit="button.is-download"

# Preparing
element_for_submit0="button.is-success.is-small"
url=input("Give an target, for example: https://www.facebook.com/itisnotyouitisporn/videos/000000000000000.\n")

browser = webdriver.Chrome()
browser.get((website_link))	

try:
	### Inner text...
	browser.execute_script("document.querySelector('[name=\"url\"]').value = '"+url+"'") 
	time.sleep(1)
	signInButton = browser.find_element_by_class_name(element_for_submit)
	signInButton.click()
	# Convert
	time.sleep(15)
	browser.execute_script("document.querySelectorAll(\"button.is-success.is-small\")[0].click()")
	# Download
	time.sleep(5)
	browser.execute_script("document.querySelectorAll(\"a.button.is-success\")[1].click()")
	
	print("payload is deployed...\n")
except Exception as error:
	
	#### This exception occurs if the element are not found in the webpage.
	print(error)
