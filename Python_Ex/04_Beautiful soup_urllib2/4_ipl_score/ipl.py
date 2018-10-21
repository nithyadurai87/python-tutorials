"""IPL Score - BeatifulSoup concept"""
from bs4 import BeautifulSoup
from urllib2 import urlopen
from datetime import datetime
from time import sleep
print "\n******IPL MATCH LIVE SCORE******"

#change 16395=>?, dd=>?, kxip=>?, 7th=>? ,2016=>?
while(1):
    url="http://www.cricbuzz.com/live-cricket-scores/16395/dd-vs-kxip-7th-match-indian-premier-league-2016"
    response=urlopen(url).read()
    soup=BeautifulSoup(response, "html.parser")
    score=soup.find("div",attrs={"class":"cb-scrs-wrp"})
    kkr_vs_mi = score.findChildren('div')
    for element in kkr_vs_mi:
        print element.text.strip()
    sleep(1)
    print "\n ****** Refreshed *******"


