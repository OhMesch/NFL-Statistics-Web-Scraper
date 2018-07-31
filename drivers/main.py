import requests
from nflScraper import nflScraper
from bs4 import BeautifulSoup
from TableParser import TableParser
from OSWorker import OSWorker
from Logger import Logger

logger = Logger()
scraper = nflScraper(logger)
for i in range(97,97+26):
	scraper.scrapeUrlForLinks("http://www.nfl.com/players/search?category=lastName&playerType=current&d-447263-p=1&filter=%s" %chr(i))
allPlayerURLs = scraper.getPlayerLinks()

for playerURL in allPlayerURLs:
	playerURL = "http://www.nfl.com"+playerURL
	splitPlayerURL = playerURL.split("/")
	playerName = splitPlayerURL[4]
	print(playerName)
	playerCareerURL = splitPlayerURL[:-1]+["careerstats"]
	playerCareerURL = "/".join(playerCareerURL)

	try:
	    code = requests.get(playerCareerURL)
	    htmlInPlainText = code.text
	    htmlSoup = BeautifulSoup(htmlInPlainText, "html.parser")
	except requests.exceptions.RequestException as err:
		logger.printLn(err)
	else:
		tableSet = htmlSoup.find_all("table")
		newFolder = "PlayerStats/"+playerName
		if not OSWorker.isExistingPath(newFolder):
			OSWorker.createFolder(newFolder)

		for table in tableSet:
			tableObj = TableParser(table)
			tableObj.parseTable()
			tableTitle = tableObj.getTableTitle()
			tableString = tableObj.getTableString()
			newFile = newFolder+"/"+tableTitle
			if OSWorker.isExistingPath(newFile):
				OSWorker.deleteFile(newFile)
			OSWorker.createFile(newFile)
			OSWorker.appendToFile(newFile,tableString)

