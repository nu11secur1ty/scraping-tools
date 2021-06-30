#!/usr/bin/python3
# Author: @nu11secur1ty
# Debug: g3ck0dr1v3r
from selenium import webdriver
import time

#enter the link to the website you want to automate login.
website_link="http://www.get-youtube-thumbnail.com/"

#enter the element for submit button by class
element_for_submit="text"

url=input("Give an target, for example: https://www.youtube.com/watch?v=x35qnqRi8As\n")

browser = webdriver.Chrome()
browser.get((website_link))	

try:
	# Inner text...
	browser.execute_script("document.querySelector('[class=\"text\"]').value = '"+url+"'") 
	time.sleep(1)
	signInButton = browser.find_element_by_class_name(element_for_submit)
	signInButton.click()
	# Convert
	time.sleep(5)
	browser.execute_script("document.querySelectorAll(\"button\")[0].click()")
	
	print("payload is deployed...\n")
except Exception as error:
	
	#### This exception occurs if the element are not found in the webpage.
	print(error)
