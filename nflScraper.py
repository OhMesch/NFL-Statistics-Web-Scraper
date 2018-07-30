import requests
import re
from bs4 import BeautifulSoup
from Logger import Logger

class nflScraper:
	def __init__(self):
		self.visitsCount = 0
		self.visitsLimit = 10
		self.playerLinks = []
		self.BASE_SITE = "http://www.nfl.com"
		self.seenUrls = set()
		self.logger = Logger()

	def updatevisitsCount(self):
		self.visitsCount += 1

	def visitsCountIsAcceptable(self):
		return self.visitsCount <= self.visitsLimit

	def scrapeUrlForLinks(self, url):
		self.updatevisitsCount()
		if(self.visitsCountIsAcceptable()):
			try:
				htmlSoup = self.getHTMLFromURL(url)
			except requests.exceptions.RequestException as err:
				self.logger.printLn("Unable to reach {}:\n{}\n".format(url,err))
			else:
				#is additionalLinks used?
				#are we only looking at first page?
				additionLinks = self.getLinksFromHTML(htmlSoup)

	def getHTMLFromURL(self, url):
		code = requests.get(url)
		htmlInPlainText = code.text
		htmlSoup = BeautifulSoup(htmlInPlainText, "html.parser")
		# print(htmlSoup.title.string)
		return(htmlSoup)

	def getLinksFromHTML(self, html):
		playerLinks = []
		for link in html.find_all(href=re.compile("player/|lastName")):
			newUrl = link.get('href')
			if newUrl not in self.seenUrls:
				self.seenUrls.add(newUrl)
				self.sortLink(newUrl)

	def sortLink(self, link):
		first8Char = link[:8]
		if first8Char == "/player/":
			self.playerLinks.append(link)
		elif first8Char == "/players":
			self.scrapeUrlForLinks(self.BASE_SITE+link)
		else:
			self.logger.printLn("Unexpected link detected:\n%s\n" % link)

	def getPlayerLinkList(self):
		return(self.playerLinks)