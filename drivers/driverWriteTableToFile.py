import requests
import re
from bs4 import BeautifulSoup
from TableParser import TableParser
from CSVWriter import CSVWriter
from OSWorker import OSWorker

url = "http://www.nfl.com/player/antoniobrown/2508061/careerstats"

try:
    code = requests.get(url)
    htmlInPlainText = code.text
    htmlSoup = BeautifulSoup(htmlInPlainText, "html.parser")
except requests.exceptions.RequestException as err:
    self.logger.printLn("Unable to reach {}:\n{}\n".format(url,err))

tableSet = htmlSoup.find_all("table")
newFolder = "antoniobrown"
if OSWorker.isExistingPath(newFolder):
	OSWorker.deleteFolder(newFolder)
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

print(tableObj.getTableString())