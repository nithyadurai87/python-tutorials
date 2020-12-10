"""BeatifulSoup concept"""
from bs4 import BeautifulSoup
from urllib2 import urlopen
print "\n******espncricinfo.com******"

#url = raw_input("\nEnter the URL to fetch: ")
url="http://www.espncricinfo.com"

#hit the url and store the response
response=urlopen(url).read()

#pass the response to soup 
soup=BeautifulSoup(response, "html.parser")

#parse using soup to find the approriate result
score=soup.find("ul",attrs={"class":"scoreline-list"})

ind_vs_sri = score.findChild()

for element in ind_vs_sri.findAll('span'):
    print element.text.strip()

