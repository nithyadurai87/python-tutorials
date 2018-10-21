"""Dollor price and time save to file use Beautiful soup"""
from bs4 import BeautifulSoup
import urllib2
from datetime import datetime
from time import sleep

#define function to getnews
def getnews():
    url="http://timesofindia.indiatimes.com/business"
    req=urllib2.urlopen(url)
    page=req.read()
    scraping=BeautifulSoup(page)
    price=scraping.findAll("span",attrs={"class":"red14px"})[0].text
    return price

#write the details into file
with open("bseindex.out","w") as f:
    for x in range(2,100):
        sNow=datetime.now().strftime("%I:%M:%S%p")
	print sNow
	f.write("{0}, {1} \n".format(sNow,getnews()))
	sleep(1)

