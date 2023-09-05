from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

# Define a site to scrape 
base_url = u'https://www.cnn.com/search?q=politics&size=200'

browser.get(base_url)
time.sleep(1)

# Finds the container that contains every news article.
main_news_container = browser.find_element_by_class_name('cnn-search__results-list')

# In main container get 'a'
text_sections = main_news_container.find_elements_by_xpath("//a[@href]")

for elem in text_sections:
    if "/2022/" in elem.get_attribute("href"):
        #this is printing the link
        print(elem.get_attribute("href"))
        #this is printing the Headline
        print(elem.text)

# Find the text body_elements inside the main_news_container
body_elements = main_news_container.find_elements_by_class_name("cnn-search__result-body")

# this is how you get the 'body_elements' text
print(body_elements[1].text)
