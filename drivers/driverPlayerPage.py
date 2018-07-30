import requests
import re
from bs4 import BeautifulSoup

url = "http://www.nfl.com/player/antoniobrown/2508061/profile"
try:
	code = requests.get(url)
	htmlInPlainText = code.text
	htmlSoup = BeautifulSoup(htmlInPlainText, "html.parser")
	print(htmlSoup.title.string)
except requests.exceptions.RequestException as err:
	self.logger.printLn("Unable to reach {}:\n{}\n".format(url,err))
for link in htmlSoup.find_all():
	# link = link.get('href')
	if link:
		print(link)
print(htmlSoup.find('pos').text)