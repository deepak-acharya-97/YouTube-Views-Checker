from selenium import webdriver
from bs4 import BeautifulSoup
from time import *
from sys import *
#from selenium.webdriver.common.keys import *

YouTubeLink = "https://www.youtube.com/watch?v=rZfEgxCcYRQ"
outputCsvName = "youtubeviews.csv"
count=0
while True:
	driver=webdriver.Chrome("E:\\MAJOR_PROJECT_DEEPAK_ACHARYA\\CODES\\selenium\\chromedriver.exe")
	driver.get(YouTubeLink)
	sleep(10)

	html = driver.page_source
	soup = BeautifulSoup(html,"html.parser")
	myViews = soup.find("span", { "class" : "view-count style-scope yt-view-count-renderer" })
	print myViews.text
	a=open(outputCsvName,'a')
	t=strftime('%d/%m/%Y %a %H:%M:%S')
	a.write(t+','+myViews.text.split(' ')[0]+'\n')
	a.close()
	print "closing"
	driver.close()
	print "closed"
	count+=1
