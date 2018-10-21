"""Baby Names Start from A use BeatifulSoup concept"""
from bs4 import BeautifulSoup
import urllib2

#url link
url="http://babynames.com/Names/A"

#request url
req=urllib2.urlopen(url)

#read the page
page=req.read()

#print page
scraping=BeautifulSoup(page)

#alllink=scraping.findAll("a",attrs={"class":"letter"})[0].text
maleName=scraping.findAll("a",attrs={"class":"M"})
femaleName=scraping.findAll("a",attrs={"class":"F"})
uniSexName=scraping.findAll("a",attrs={"class":"E"})
print maleName
#print alllink[0]

with open("baby-A-names1.out","w") as f:
    for i in alllink:
        #href=i.get("href")
	Name=i.string
        #Name=Name.strip()
        #print href
        print Name
#	if(href!="#"):
        f.write("{0}\n".format(Name))

