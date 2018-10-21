"""IEEE website all links to save use Beautiful soup concept"""
from bs4 import BeautifulSoup
import urllib2

#url link
url="http://ieee.org"

#request
req=urllib2.urlopen(url)
page=req.read()

#scarpe the page
scraping=BeautifulSoup(page)
alllink=scraping.findAll("a",text=True)
print alllink
#print alllink[0]

with open("bseindex1.out","w") as f:
    for i in alllink:
        href=i.get("href")
	Name=i.string
        Name=Name.strip()
        #print href
        #print Name
	if(href!="#"):
            f.write("{0}, {1} \n".format(Name,href))

