import requests
import re
from bs4 import BeautifulSoup

class TableParser:
	def __init__(self, table):
		self.table = table
		self.tableTitle = None
		self.tableColumnNames = []
		self.tableRowValues = None

	def parseTable(self):
		self.autoSetTableTitle()
		self.autoSetColumnNames()
		self.autoFillRows()

	def autoSetTableTitle(self):
		self.tableTitle = self.table.find('div').text.strip()

	def autoSetColumnNames(self):
		tdTags = self.table.find_all('td')
		currLine = 0
		currText = tdTags[currLine].text.strip()

		while currLine < len(tdTags) and currText != "Year":
			currLine += 1
			currText = tdTags[currLine].text.strip()

		while currLine < len(tdTags) and not currText.isdigit(): #First entry is always year
			if currText: 
				self.tableColumnNames.append(currText)
			currLine += 1
			currText = tdTags[currLine].text.strip()

	def autoFillRows(self):
		tdTags = self.table.find_all('td')
		currLine = 1
		currText = tdTags[currLine].text.strip()
		while currLine < len(tdTags) and not currText.isdigit():
			currLine += 1
			currText = tdTags[currLine].text.strip()

		numColumns = len(self.tableColumnNames)
		dataCounter = 0
		currRow = []
		self.tableRowValues = []
		while currLine < len(tdTags) and currText != "TOTAL":
			if currText:
				currRow.append(currText)
				if dataCounter < numColumns - 1:
					dataCounter += 1
				else:
					self.tableRowValues.append(currRow)
					currRow = []
					dataCounter = 0
				
			currLine += 1
			currText = tdTags[currLine].text.strip()

	def getTableTitle(self):
		return(self.tableTitle)

	def getTableString(self):
		tableString = ', '.join(self.tableColumnNames) + "\n"
		for row in self.tableRowValues:
			tableString += ', '.join(row)+"\n"
		return(tableString)

	def printTableTitle(self):
		print(self.tableTitle)

	def printRowNames(self):
		print(self.tableColumnNames)

	def printTable(self):
		for row in self.tableRowValues:
			print(row)
		print('\n')