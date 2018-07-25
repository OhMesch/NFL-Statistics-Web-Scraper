import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

class TableParser:
	def __init__(self, table):
		self.table = table
		self.tableTitle = None
		self.tableRowNames = None

	def parseTable(self):
		self.setTableTitleFromDiv()
		self.setRowNames()

	def setTableTitleFromDiv(self):
		self.tableTitle = self.table.find('div').text
		print("Title is: " + self.tableTitle)

	def setRowNames(self):
		# print("Row names are:")
		a = self.table.find_all('td')
		print(a)
		for c in a:
			print(c.text)