import requests
import re
from bs4 import BeautifulSoup
from Logger import Logger

class nflScraper:
	def __init__(self, loggerObj):
		self.playerLinks = []
		self.BASE_SITE = "http://www.nfl.com"
		self.seenUrls = set()
		self.logger = loggerObj

	def scrapeUrlForLinks(self, url):
		try:
			htmlSoup = self.getHTMLFromURL(url)
		except requests.exceptions.RequestException as err:
			self.logger.printLn("Unable to reach {}:\n{}\n".format(url,err))
		else:
			self.getLinksFromHTML(htmlSoup)

	def getHTMLFromURL(self, url):
		code = requests.get(url)
		htmlInPlainText = code.text
		htmlSoup = BeautifulSoup(htmlInPlainText, "html.parser")
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
			newPlayerLink = link
			self.playerLinks.append(newPlayerLink)
		elif first8Char == "/players":
			nextPage = self.BASE_SITE+link
			self.scrapeUrlForLinks(nextPage)
		else:
			self.logger.printLn("Unexpected link detected:\n%s\n" % link)

	def getPlayerLinkList(self):
		return(self.playerLinks)