from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#Setting up URL
nlp = "http://nlp.stanford.edu:8080/corenlp/"
print("Sit Back and Relax\n")
#taking input
with open('Data/data.txt', 'r') as myfile:
	corpus = myfile.read().replace('\n', '')
#Setting up Driver
driver = webdriver.Firefox()
print("Opened browser....\n")
#initializing URL
driver.get(nlp)
#Selecting viewing option
view = Select(driver.find_element_by_name("outputFormat"))
view.select_by_visible_text('CoNLL')
#Entering text in Text Area
text_area = driver.find_element_by_name("input")
text_area.send_keys(corpus)
print("Entered Text....\n")
#Clicking on submit
driver.find_element_by_name("Process").click()
#Getting element with output, stored under pre tag
text = driver.find_elements_by_tag_name("pre")
print("Got Data....\n")
#taking element from list
for x in text:
	data = x.text
#spliting the words int the list
data=data.replace('\n',' ',)
list1=data.split(' ')
#close
driver.close()
print("Closed Browser....\n")
k=0
main=[]
list3=[]
for x in list1:
	if x == '':
		continue
	if (k%7)!=0:
		list3.append(x)
	else:
		if k!=0:
			main.append(list3)
		list3=[]
	k+=1
#main is the 2d array of processed data with
# main[][0] words
# main[][1] be their root
# main[][2] be their pos tags
# main[][3] be their Named Entities
# main[][4] , main[][5] idk sorry 	
for v in main:
	print(v)
