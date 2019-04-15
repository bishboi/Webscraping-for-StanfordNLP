from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#Setting up URL
nlp = "http://nlp.stanford.edu:8080/parser/"
print("Sit Back and Relax\n")
#taking input
with open('Data/data.txt', 'r') as myfile:
	corpus = myfile.read().replace('\n', '')
#Setting up Driver
driver = webdriver.Firefox()
print("Opened browser....\n")
#initializing URL
driver.get(nlp)
#Entering text in Text Area
text_area = driver.find_element_by_name("query")
text_area.send_keys(corpus)
print("Entered Text....\n")
#Clicking on submit
driver.find_element_by_name("parse").click()
#Getting element with output, stored under pre tag
text = driver.find_elements_by_id("parse")
print("Got Data....\n")
#taking element from list
for x in text:
	data = x.text
#spliting the words int the list
#data=data.replace('\n','',)
#data=data.replace(' ','',)
#close
driver.close()
print("Closed Browser....\n")
print(data)

