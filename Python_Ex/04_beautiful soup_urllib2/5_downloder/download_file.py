"""Downloder - downloadd image file"""
import urllib2

#get url 
url=raw_input("Enter the image url you want")
f = urllib2.urlopen(url)

#create new image file
jpg = open("1.png","w")
jpg.write(f.read())
jpg.close()
