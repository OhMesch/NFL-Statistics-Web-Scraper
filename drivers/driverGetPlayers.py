from nflScraper import nflScraper

driver = nflScraper()
for i in range(97,97+26):
	driver.scrapeUrlForLinks("http://www.nfl.com/players/search?category=lastName&playerType=current&d-447263-p=1&filter=%s" %chr(i))
print(driver.getPlayerLinkList())