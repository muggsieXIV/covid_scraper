#!/usr/bin/env python3
# coding: utf-8

from bs4 import BeautifulSoup as soup
import requests
import csv
from datetime import date

query = []

# For use of filtering dates, will need to improve for date ranges
today = date.today()
d = today.strftime("%m-%d-%y")
print("date =", d)


# CNN urls are formatted with dates, can update query parameters easily with this method
cnn_url="https://edition.cnn.com/world/live-news/coronavirus-pandemic-{}-intl/index.html".format(d)
cnn_url


# In[4]:


html = requests.get(cnn_url)


# In[5]:


bsobj = soup(html.content,'lxml')
bsobj


# In[6]:


for link in bsobj.findAll("h2"):
    
    print("Headline : {}".format(link.text))


# In[7]:


for news in bsobj.findAll('article',{'class':'sc-jqCOkK sc-kfGgVZ hQCVkd'}):
    query.append([news.text.strip()])


# In[8]:


nbc_url='https://www.nbcnews.com/health/coronavirus'


# In[9]:


r = requests.get('https://www.nbcnews.com/health/coronavirus')


# In[10]:


b = soup(r.content,'lxml')


# In[11]:


for news in b.findAll('h2'):
    query.append([news.text])


# In[12]:


links = []
for news in b.findAll('h2',{'class':'teaseCard__headline'}):
    links.append(news.a['href'])
links


# In[13]:

for link in links:
    page = requests.get(link)
    bsobj = soup(page.content)
    for news in bsobj.findAll('div',{'class':'article-body__section article-body__last-section'}):
        query.append([news.text.strip()])


print(query)
header = ['cached data']

with open('covid.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for data in query:
        writer.writerow(data)