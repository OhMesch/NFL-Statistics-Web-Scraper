import requests
import re
from bs4 import BeautifulSoup
from TableParser import TableParser

url = "http://www.nfl.com/player/antoniobrown/2508061/careerstats"

try:
    code = requests.get(url)
    htmlInPlainText = code.text
    htmlSoup = BeautifulSoup(htmlInPlainText, "html.parser")
except requests.exceptions.RequestException as err:
    self.logger.printLn("Unable to reach {}:\n{}\n".format(url,err))

# tables = pd.read_html(url)
# rec = tables[1]
# print(rec)

tableSet = htmlSoup.find_all("table")
for table in tableSet:
	tableObj = TableParser(table)
	tableObj.parseTable()

print(tableObj.getTableString())