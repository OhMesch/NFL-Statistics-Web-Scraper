import requests
from nflScraper import nflScraper
from bs4 import BeautifulSoup
from TableParser import TableParser
from OSWorker import OSWorker
from CSVWriter import CSVWriter
from Logger import Logger

class StatsBuilder:
    def __init__(self, foldername):
        self.PARENT_FOLDER = foldername
        self.logger = Logger()

    def buildStatCSV(self):
        allPlayerURLs = self.getAllPlayerURLs()

        for playerURL in allPlayerURLs:
            playerURL = "http://www.nfl.com"+playerURL
            playerName = self.getPlayerNameFromURL(playerURL)
            playerCareerURL = self.playerURLToCareerURL(playerURL)

            self.buildPlayerStats(playerCareerURL, playerName)

        self.logger.printLn("CSV Stat Building Complete")

    def getAllPlayerURLs(self):
        scraper = nflScraper(self.logger)
        for i in range(ord("a"),ord("z")+1):
            scraper.scrapeUrlForLinks("http://www.nfl.com/players/search?category=lastName&playerType=current&d-447263-p=1&filter=%s" %chr(i))
        allPlayerURLs = scraper.getPlayerLinks()
        return(allPlayerURLs)

    def getPlayerNameFromURL(self, playerURL):
        splitPlayerURL = playerURL.split("/")
        playerName = splitPlayerURL[4]
        return(playerName)

    def playerURLToCareerURL(self, playerURL):
        splitPlayerURL = playerURL.split("/")
        playerName = splitPlayerURL[4]
        playerCareerURL = splitPlayerURL[:-1]+["careerstats"]
        playerCareerURL = "/".join(playerCareerURL)
        return(playerCareerURL)

    def buildPlayerStats(self, careerURL, playerName):
        try:
            htmlSource = self.getHTMLSource(careerURL)
        except requests.exceptions.RequestException as err:
            self.logger.printLn(err)
        else:
            tableSet = htmlSource.find_all("table")
            newFolder = self.PARENT_FOLDER+"/"+playerName
            
            if not OSWorker.isExistingPath(newFolder):
                OSWorker.createFolder(newFolder)

            writer = CSVWriter(newFolder)
            for table in tableSet:
                writer.writeTableToCSV(table)

    def getHTMLSource(self, url):
        code = requests.get(url)
        htmlInPlainText = code.text
        htmlSoup = BeautifulSoup(htmlInPlainText, "html.parser")
        return(htmlSoup)
