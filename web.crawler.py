import requests
from BeautifulSoup import BeautifulSoup as bs

url = 'coopergeneral.com'
r = requests.get('http://coopergeneral.com/wireless')

soup = bs(r.content)

#print soup.prettify


for link in soup.findAll('a'):
    #print link
    #print link.get('href')
    #print link.text
    #print link.text, link.get('href')
    #if 'http' in link.get('href'):
    print "<a href='{}'>{}".format(link.get('href'), link.text)

g_data - soup.findAll('div')

