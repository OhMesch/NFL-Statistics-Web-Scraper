import requests
import re
from bs4 import BeautifulSoup

class nflScraper:
	def __init__(self):
		self.visitsCount = 0
		self.visitsLimit = 20
		self.seenUrls = set()

	def updatevisitsCount(self):
		self.visitsCount += 1

	def visitsCountIsAcceptable(self):
		return self.visitsCount <= self.visitsLimit

	def connectToUrl(self, url):
		self.updatevisitsCount()
		if(self.visitsCountIsAcceptable()):
			code = requests.get(url)
			htmlInPlainText = code.text
			htmlSoup = BeautifulSoup(htmlInPlainText, "html.parser")
			print(htmlSoup.title.string)
			for link in htmlSoup.find_all(href=re.compile("player/|lastName")):
				cleanLink = link.get('href')
				if cleanLink not in self.seenUrls:
					print(cleanLink)
					self.seenUrls.add(cleanLink)
					# print(link.get('href'))
					# self.connectToUrl(cleanLink)

driver = nflScraper()
driver.connectToUrl("http://www.nfl.com/players/search?category=lastName&filter=A&playerType=current")