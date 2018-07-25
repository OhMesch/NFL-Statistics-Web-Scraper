import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

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
		self.printTableTitle()
		self.printRowNames()
		self.printTable()

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
		numColumns = len(self.tableColumnNames)
		self.tableRowValues = []
		tdTags = self.table.find_all('td')
		currLine = 1
		currText = tdTags[currLine].text.strip()
		while currLine < len(tdTags) and not currText.isdigit():
			currLine += 1
			currText = tdTags[currLine].text.strip()

		dataCounter = 0
		currRow = []
		while currLine < len(tdTags) and currText != "TOTAL":
			if currText:
				if dataCounter < 13:
					currRow.append(currText)
					dataCounter += 1
				else:
					self.tableRowValues.append(currRow)
					currRow = []
					dataCounter = 0
				
			currLine += 1
			currText = tdTags[currLine].text.strip()

	def printTableTitle(self):
		print(self.tableTitle)

	def printRowNames(self):
		print(self.tableColumnNames)

	def printTable(self):
		for row in self.tableRowValues:
			print(row)
		print('\n')