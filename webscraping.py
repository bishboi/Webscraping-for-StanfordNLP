#import the library used to query a website
import urllib.request
#specify the url
nlp = "http://nlp.stanford.edu:8080/corenlp/"
#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(nlp)
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Parse the html in the 'page' variable, and store it in Beautiful Soup format this will be done in lxml parsing
#print(soup)
from selenium import webdriver

browser = webdriver.Firefox()
#browser.get('http://seleniumhq.org/')